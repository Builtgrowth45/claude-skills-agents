#!/usr/bin/env bash
# Linux/macOS setup helper for discord-scraper
set -e

if [ ! -d "discord-scraper" ]; then
  git clone https://github.com/dfrnoch/discord-scraper.git
fi

cd discord-scraper

if [ ! -f requirements.txt ]; then
  echo "requirements.txt not found. Ensure you are in the discord-scraper directory."
  exit 1
fi

pip install -r requirements.txt

if [ ! -f config.json ]; then
  echo '{"token": ""}' > config.json
  echo "Created config.json — add your Discord token before running."
fi

echo "Setup complete. Edit config.json with your token, then run: python main.py"
