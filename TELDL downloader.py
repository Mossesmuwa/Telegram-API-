import argparse
from telethon.sync import TelegramClient
from colorama import Fore, init
import sys, os

# Telegram credentials
api_id = 1234567
api_hash = 'your_api_hash_here'
phone = '+2567xxxxxxx'

# Init color
init(autoreset=True)

def show_progress(current, total):
    percent = current * 100 / total
    bar = ('█' * int(percent // 5)).ljust(20)
    sys.stdout.write(f"\r{Fore.YELLOW}Downloading: |{bar}| {percent:.1f}%")
    sys.stdout.flush()

def banner():
    print(Fore.CYAN + r"""
 _______        _        _                                  
|__   __|      (_)      | |                                 
   | | ___  ___ _ ______| |__   ___  ___ ___  ___ __ _ _ __ 
   | |/ _ \/ __| |______| '_ \ / _ \/ __/ __|/ __/ _` | '__|
   | |  __/\__ \ |      | | | |  __/\__ \__ \ (_| (_| | |   
   |_|\___||___/_|      |_| |_|\___||___/___/\___\__,_|_|   
                                                          
        TELEGRAM VIDEO DOWNLOADER
""")

def main():
    parser = argparse.ArgumentParser(description='Download Telegram videos by message ID')
    parser.add_argument('--channel', '-c', help='Telegram channel or group username (with or without @)', required=True)
    parser.add_argument('--ids', '-i', help='Comma-separated message IDs to download', required=True)

    args = parser.parse_args()
    channel = args.channel.strip()
    if not channel.startswith('@'):
        channel = '@' + channel
    try:
        message_ids = [int(x.strip()) for x in args.ids.split(',')]
    except ValueError:
        print(Fore.RED + "Invalid message ID(s).")
        sys.exit(1)

    banner()

    with TelegramClient('session', api_id, api_hash) as client:
        for msg_id in message_ids:
            try:
                message = client.get_messages(channel, ids=msg_id)
                if message and message.video:
                    print(Fore.BLUE + f"\n📦 Found video in message {msg_id}")
                    filename = f"video_{msg_id}.mp4"
                    client.download_media(message, file=filename, progress_callback=show_progress)
                    print(Fore.GREEN + f"\n✅ Download complete: {filename}")
                else:
                    print(Fore.YELLOW + f"\n⚠️ No video found in message {msg_id}")
            except Exception as e:
                print(Fore.RED + f"\n❌ Error: {e}")

if __name__ == '__main__':
    main()
