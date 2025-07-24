
# Telegram File Downloader Script (Termux + Python)

This script allows you to download files (videos, documents, etc.) from a specific Telegram group or channel using the Telegram API. It runs in **Termux** on Android, using Python and `telethon`.

## 📌 Features

- Download media from Telegram groups or channels
- Supports filtering by message ID
- Progress and completion messages
- Customizable group/channel and message input

---

## 🧰 Requirements

- Termux (Android)
- Python (≥ 3.10 recommended)
- Telegram API credentials (API ID and API Hash)
- `telethon` Python library

---

## ⚙️ Setup Instructions

1. **Install Python and pip:**
   ```bash
   pkg update && pkg install python -y
