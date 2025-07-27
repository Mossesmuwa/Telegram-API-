#!/bin/bash

echo "[+] Installing TELDL..."

# Install Python packages
pip install -r requirements.txt

# Install the launcher
sudo cp teldl /usr/local/bin/
sudo chmod +x /usr/local/bin/teldl

# Install man page
sudo cp teldl.1 /usr/share/man/man1/
sudo mandb

echo "[✔] Installation complete!"
echo "You can now run 'teldl --help' or 'man teldl'"
