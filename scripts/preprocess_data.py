# Script for preprocessing text

import json
import re

# Load raw data
with open('data/raw/telegram_data.json', 'r', encoding='utf-8') as f:
    raw_data = json.load(f)

# Preprocessing function
def preprocess_message(message):
    text = message.get('text', '')
    # Remove URLs
    text = re.sub(r"http\S+|www\S+", "", text)
    # Normalize text (e.g., whitespace, punctuation)
    text = re.sub(r"\s+", " ", text).strip()
    return {
        'channel': message['channel'],
        'text': text,
        'timestamp': message['timestamp']
    }

# Apply preprocessing
processed_data = [preprocess_message(msg) for msg in raw_data]

# Save processed data
with open('data/processed/preprocessed_telegram_data.json', 'w', encoding='utf-8') as f:
    json.dump(processed_data, f, ensure_ascii=False, indent=4)

print("Data preprocessing complete.")
