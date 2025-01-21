import shap
import torch
from transformers import AutoTokenizer, AutoModelForTokenClassification

# Load the fine-tuned model
MODEL_NAME = "xlm-roberta-base"  # Replace with your best-performing model
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForTokenClassification.from_pretrained(MODEL_NAME)

# Example text
example_text = "በአዲስ አበባ እንግዳ ቤት ዋጋ አንድ ሺ ብር ነው።"

# Tokenize input
inputs = tokenizer(example_text, return_tensors="pt")

# SHAP explanation
explainer = shap.Explainer(model, tokenizer)
shap_values = explainer(example_text)

# Visualize SHAP
shap.plots.text(shap_values)

# Additional Interpretability with LIME
from lime.lime_text import LimeTextExplainer
explainer = LimeTextExplainer(class_names=["O", "B-LOC", "B-PRICE", "B-PRODUCT"])
explanation = explainer.explain_instance(
    example_text,
    lambda x: model(**tokenizer(x, return_tensors="pt")).logits.detach().numpy(),
    num_features=6,
)
explanation.show_in_notebook()
