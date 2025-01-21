import os
import pandas as pd
from datasets import load_dataset, Dataset
from transformers import AutoTokenizer, AutoModelForTokenClassification, TrainingArguments, Trainer
from transformers import DataCollatorForTokenClassification
from sklearn.metrics import precision_recall_fscore_support
import torch

# Set dataset path
DATA_PATH = "../data/processed/labeled_data.conll"

# Load dataset
def load_conll_dataset(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        data = {"tokens": [], "labels": []}
        tokens, labels = [], []
        for line in f:
            if line.strip() == "":
                if tokens:
                    data["tokens"].append(tokens)
                    data["labels"].append(labels)
                    tokens, labels = [], []
            else:
                token, label = line.strip().split()
                tokens.append(token)
                labels.append(label)
        return Dataset.from_dict(data)

# Tokenize dataset
def tokenize_and_align_labels(examples, tokenizer, label_to_id):
    tokenized_inputs = tokenizer(
        examples["tokens"],
        truncation=True,
        is_split_into_words=True,
        padding=True,
    )
    labels = []
    for i, label in enumerate(examples["labels"]):
        word_ids = tokenized_inputs.word_ids(batch_index=i)
        aligned_labels = [-100 if word_id is None else label_to_id[label[word_id]] for word_id in word_ids]
        labels.append(aligned_labels)
    tokenized_inputs["labels"] = labels
    return tokenized_inputs

# Load data and labels
dataset = load_conll_dataset('data/processed/labeled_data.conll')

# Check the number of samples in the dataset
print(f"Number of samples in dataset: {len(dataset)}")

# If the dataset has more than 1 sample, perform the split
if len(dataset) > 1:
    # Split the dataset into train and validation sets (90% train, 10% validation)
    train_test_split = dataset.train_test_split(test_size=0.1) 
    train_dataset = train_test_split['train']
    validation_dataset = train_test_split['test']
else:
    print("Warning: Not enough samples to split. Using the full dataset for training.")
    train_dataset = dataset
    validation_dataset = dataset

# Define model and tokenizer
model_name = "xlm-roberta-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForTokenClassification.from_pretrained(model_name, num_labels=7)

# Label mapping
label_list = ["O", "B-Product", "I-Product", "B-LOC", "I-LOC", "B-PRICE", "I-PRICE"]
label_to_id = {label: i for i, label in enumerate(label_list)}
id_to_label = {i: label for label, i in label_to_id.items()}

# Tokenize dataset
tokenized_train_dataset = train_dataset.map(
    lambda x: tokenize_and_align_labels(x, tokenizer, label_to_id),
    batched=True,
)
tokenized_validation_dataset = validation_dataset.map(
    lambda x: tokenize_and_align_labels(x, tokenizer, label_to_id),
    batched=True,
)

# Set training arguments (modified to save the model)
training_args = TrainingArguments(
    output_dir="./models/fine_tuned_model",  # Save to 'models' folder
    evaluation_strategy="steps",
    learning_rate=2e-5,
    per_device_train_batch_size=16,
    num_train_epochs=3,
    save_steps=1000, 
    logging_dir="../results/logs",
)

# Trainer API
data_collator = DataCollatorForTokenClassification(tokenizer)
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_train_dataset,
    eval_dataset=tokenized_validation_dataset,
    tokenizer=tokenizer,
    data_collator=data_collator,
)

# Train and evaluate
trainer.train()
results = trainer.evaluate()
print(results)

# Save model (explicitly call save_model)
trainer.save_model("./models/fine_tuned_model")