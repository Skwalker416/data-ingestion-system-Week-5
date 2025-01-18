# Script for labeling messages in CoNLL format

import json

# Load processed data
with open('data/processed/preprocessed_telegram_data.json', 'r', encoding='utf-8') as f:
    processed_data = json.load(f)

# Example labeling function
def label_message(message):
    tokens = message['text'].split()
    labeled_tokens = []
    for token in tokens:
        if "ተሸጋጭ" in token:  # Example condition for product names
            labeled_tokens.append(f"{token} B-Product")
        elif "በብር" in token:  # Example condition for prices
            labeled_tokens.append(f"{token} B-PRICE")
        else:
            labeled_tokens.append(f"{token} O")
    return labeled_tokens

# Label data
labeled_data = []
for msg in processed_data[:30]:  # Label only 30 messages as an example
    labeled_tokens = label_message(msg)
    labeled_data.append("\n".join(labeled_tokens) + "\n")

# Save to file
with open('data/samples/labeled_data.conll', 'w', encoding='utf-8') as f:
    f.writelines(labeled_data)

print("Data labeling complete.")
