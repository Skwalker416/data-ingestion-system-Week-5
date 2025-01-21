from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline
from datasets import load_dataset

# Load fine-tuned model
model_name = "./xlm-roberta-ner"  # Path to saved model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForTokenClassification.from_pretrained(model_name)

# Create NER pipeline
ner_pipeline = pipeline("ner", model=model, tokenizer=tokenizer)

# Load validation dataset
dataset = load_dataset("conll2003", split="validation")  # Replace with your dataset

# Evaluate predictions
for example in dataset["tokens"][:5]:  # Evaluate on a few samples
    predictions = ner_pipeline(example)
    print(f"Text: {example}")
    print(f"Predictions: {predictions}")
