from telethon.sync import TelegramClient
import os, sys

# Replace with your credentials
api_id = 1234567  # <-- Your real API ID
api_hash = 'your_api_hash_here'  # <-- Your API Hash
phone = '+2567xxxxxxx'  # <-- Your phone number

# Progress bar function
def show_progress(current, total):
    percent = current * 100 / total
    bar = ('█' * int(percent // 5)).ljust(20)
    sys.stdout.write(f"\rDownloading: |{bar}| {percent:.1f}%")
    sys.stdout.flush()

# --- User Inputs ---
channel = input("Enter the channel/group username (with or without @): ").strip()
if not channel.startswith('@'):
    channel = '@' + channel

user_input = input("Enter message ID(s) to download (separated by commas): ")
message_ids = [int(x.strip()) for x in user_input.split(',') if x.strip().isdigit()]

# --- Telegram Client ---
with TelegramClient('session', api_id, api_hash) as client:
    for msg_id in message_ids:
        try:
            message = client.get_messages(channel, ids=msg_id)
            if message and message.video:
                print(f"\nFound video in message {msg_id}")
                filename = f"video_{msg_id}.mp4"
                client.download_media(message, file=filename, progress_callback=show_progress)
                print(f"\n✅ Download complete: {filename}")
            else:
                print(f"\n⚠️ No video found in message {msg_id}")
        except Exception as e:
            print(f"\n❌ Error downloading message {msg_id}: {e}")