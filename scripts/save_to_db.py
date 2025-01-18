# Script for saving data into a database

import sqlite3
import json

# Load processed data
with open('data/processed/preprocessed_telegram_data.json', 'r', encoding='utf-8') as f:
    processed_data = json.load(f)

# Connect to SQLite database
conn = sqlite3.connect('data/database/telegram_data.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    channel TEXT,
    text TEXT,
    timestamp TEXT
)
''')

# Insert data
for msg in processed_data:
    cursor.execute('''
    INSERT INTO messages (channel, text, timestamp)
    VALUES (?, ?, ?)
    ''', (msg['channel'], msg['text'], msg['timestamp']))

# Commit and close
conn.commit()
conn.close()

print("Data successfully saved to the database.")
