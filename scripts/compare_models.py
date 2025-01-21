import time
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline
from datasets import load_dataset, load_metric

# Define models to compare
MODELS = ["xlm-roberta-base", "distilbert-base-multilingual-cased", "bert-base-multilingual-cased"]

# Load dataset
dataset = load_dataset("conll2003")  # Replace with your dataset
metric = load_metric("seqeval")

def evaluate_model(model_name, dataset):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForTokenClassification.from_pretrained(model_name, num_labels=9)
    ner_pipeline = pipeline("ner", model=model, tokenizer=tokenizer)

    start_time = time.time()
    predictions = []
    references = []

    for item in dataset["validation"]:
        tokens = item["tokens"]
        labels = item["ner_tags"]

        # Tokenize input
        inputs = tokenizer(tokens, is_split_into_words=True, return_tensors="pt", truncation=True, padding=True)
        outputs = ner_pipeline(inputs["input_ids"][0])
        
        # Collect predictions and references
        predictions.append([pred["entity"] for pred in outputs])
        references.append(labels)

    elapsed_time = time.time() - start_time

    # Calculate metrics
    results = metric.compute(predictions=predictions, references=references)
    return results, elapsed_time

# Compare models
results = {}
for model_name in MODELS:
    print(f"Evaluating model: {model_name}")
    results[model_name] = evaluate_model(model_name, dataset)

# Print results
for model_name, (metrics, time_taken) in results.items():
    print(f"\nModel: {model_name}")
    print(f"Metrics: {metrics}")
    print(f"Time taken: {time_taken:.2f} seconds")
