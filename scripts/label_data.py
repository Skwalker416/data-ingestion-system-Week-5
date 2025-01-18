<<<<<<< HEAD
# Script for labeling messages in CoNLL format

import json
=======
import json
import re
>>>>>>> task-2

# Load processed data
with open('data/processed/preprocessed_telegram_data.json', 'r', encoding='utf-8') as f:
    processed_data = json.load(f)

# Example labeling function
def label_message(message):
    tokens = message['text'].split()
    labeled_tokens = []
<<<<<<< HEAD
    for token in tokens:
        if "ተሸጋጭ" in token:  # Example condition for product names
            labeled_tokens.append(f"{token} B-Product")
        elif "በብር" in token:  # Example condition for prices
            labeled_tokens.append(f"{token} B-PRICE")
        else:
            labeled_tokens.append(f"{token} O")
=======

    for token in tokens:
        # Example conditions for labeling
        if re.search(r"\d+ብር", token):  # Price detection
            labeled_tokens.append(f"{token} B-PRICE")
        elif "አዲስ" in token or "ቦሌ" in token:  # Location keywords
            labeled_tokens.append(f"{token} B-LOC")
        elif "ሱሪ" in token or "ኮፍያ" in token:  # Product-related words
            labeled_tokens.append(f"{token} B-Product")
        else:
            labeled_tokens.append(f"{token} O")  # Outside any entity
    
>>>>>>> task-2
    return labeled_tokens

# Label data
labeled_data = []
for msg in processed_data[:30]:  # Label only 30 messages as an example
    labeled_tokens = label_message(msg)
<<<<<<< HEAD
    labeled_data.append("\n".join(labeled_tokens) + "\n")

# Save to file
with open('data/samples/labeled_data.conll', 'w', encoding='utf-8') as f:
    f.writelines(labeled_data)

print("Data labeling complete.")
=======
    labeled_data.append("\n".join(labeled_tokens) + "\n\n")  # Separate messages with blank lines

# Save labeled data in CoNLL format
output_file = 'data/samples/labeled_data.conll'
with open(output_file, 'w', encoding='utf-8') as f:
    f.writelines(labeled_data)

print(f"Labeled data saved in CoNLL format at: {output_file}")
>>>>>>> task-2
