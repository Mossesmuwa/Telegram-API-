# TELDL - Telegram Video Downloader (Linux CLI Style) by MM100


`teldl` is a command-line utility for downloading videos from Telegram messages using the Telethon API. It mimics the look and feel of real Linux tools like `zphisher`, `youtube-dl`, etc.

---

## 📚 Table of Contents
- [✅ Features](#-features)
- [🔧 Requirements](#-requirements)
- [📝 Telegram API Setup](#-telegram-api-setup)
- [📦 Installation (Linux/Termux)](#-installation-linuxtermux)
- [📘 Usage](#-usage)
- [📁 Files Included](#-files-included)
- [🖼️ Demo](#-demo)
- [👨‍💻 Author](#-author)
- [🛡️ License](#-license)

---

## ✅ Features

- Download videos by message ID from Telegram channels or groups
- CLI argument interface (`--channel`, `--ids`)
- Looks like a native Linux utility
- Colored terminal UI with progress bar
- Includes manual (`man teldl`) and launcher script
- Works in both **Linux** and **Termux**

---

## 🔧 Requirements

- Python 3.7+
- [`telethon`](https://pypi.org/project/telethon/)
- [`colorama`](https://pypi.org/project/colorama/)

Install with:

```bash
pip install -r requirements.txt
