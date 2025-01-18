<<<<<<< HEAD
# Script for preprocessing text

=======
>>>>>>> task-2
import json
import re

# Load raw data
with open('data/raw/telegram_data.json', 'r', encoding='utf-8') as f:
    raw_data = json.load(f)

<<<<<<< HEAD
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
=======
# Preprocess a single message
def preprocess_message(msg):
    text = msg.get('text', '')  # Default to an empty string if 'text' is None
    text = re.sub(r"http\S+|www\S+", "", text)  # Remove URLs
    text = re.sub(r"[^\w\s]", "", text)  # Remove punctuation
    text = re.sub(r"\s+", " ", text).strip()  # Normalize whitespace

    return {
        'channel': msg.get('channel'),
        'sender': msg.get('sender'),
        'text': text,
        'timestamp': msg.get('timestamp')
    }

# Preprocess all messages
>>>>>>> task-2
processed_data = [preprocess_message(msg) for msg in raw_data]

# Save processed data
with open('data/processed/preprocessed_telegram_data.json', 'w', encoding='utf-8') as f:
    json.dump(processed_data, f, ensure_ascii=False, indent=4)

<<<<<<< HEAD
print("Data preprocessing complete.")
=======
print("Preprocessed data saved successfully!")
>>>>>>> task-2
