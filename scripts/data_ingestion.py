from telethon.sync import TelegramClient
import json

# Configuration
API_ID = '25466824'
API_HASH = 'f13acb9c667058fd14308c84236152bd'
PHONE_NUMBER = '+251703028979'
CHANNELS = [
    "@qnashcom",
    "@Fashiontera",
    "@kuruwear",
    "@gebeyaadama",
    "@MerttEka",
    "@forfreemarket"
]

# Initialize Telegram Client
client = TelegramClient('session_name', API_ID, API_HASH)

# Connect to Telegram
client.connect()
if not client.is_user_authorized():
    client.send_code_request(PHONE_NUMBER)
    client.sign_in(PHONE_NUMBER, input('Enter the code: '))

# Fetch and save messages
messages = []
for channel in CHANNELS:
    print(f"Fetching messages from channel: {channel}")
    for message in client.iter_messages(channel, limit=100):
        if message.text:  # Skip messages with no text
            messages.append({
                'channel': channel,
                'sender': message.sender_id,
                'text': message.text,
                'timestamp': message.date.isoformat()  # Convert datetime to string
            })

# Log the number of messages fetched
print(f"Total messages fetched: {len(messages)}")

# Save to file
try:
    with open('data/raw/telegram_data.json', 'w', encoding='utf-8') as f:
        json.dump(messages, f, ensure_ascii=False, indent=4)
    print("Data successfully saved to data/raw/telegram_data.json.")
except Exception as e:
    print(f"Error saving data: {e}")
