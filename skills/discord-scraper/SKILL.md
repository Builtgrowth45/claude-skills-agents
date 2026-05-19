---
name: Discord Scraper Setup
description: This skill should be used when the user asks to "set up discord scraper", "install discord scraper", "scrape discord messages", "configure discord message scraper", "set up dfrnoch/discord-scraper", or wants to extract and save Discord channel or DM messages to text files using the discord-scraper tool.
version: 0.1.0
---

# Discord Scraper Setup

## Overview

Discord Scraper (github.com/dfrnoch/discord-scraper) is a Python-based selfbot tool that extracts messages from Discord channels or DMs and saves them as text files, organized by channel name.

> **Warning:** Discord selfbots violate Discord's Terms of Service. Users risk account suspension or permanent ban. Proceed only with full awareness of this risk.

## Prerequisites

- Python 3.x installed
- A Discord user account token
- Git (optional, for cloning)

## Setup Workflow

### Step 1: Obtain the Project

Clone or download the repository:

```bash
git clone https://github.com/dfrnoch/discord-scraper.git
cd discord-scraper
```

### Step 2: Configure `config.json`

Edit `config.json` in the project root and set the Discord user token:

```json
{
  "token": "YOUR_DISCORD_TOKEN_HERE"
}
```

To obtain a Discord token, the user must extract it from the Discord web client's local storage or network requests — this is a manual step the user performs in their browser.

### Step 3: Install Dependencies

On Windows, run the provided batch file:

```bat
install.bat
```

On other platforms, install Python dependencies manually:

```bash
pip install -r requirements.txt
```

### Step 4: Run the Scraper

On Windows:

```bat
start.bat
```

On other platforms:

```bash
python main.py
```

### Step 5: Issue the Scrape Command

Once the selfbot is running and connected, send the following command in the target Discord channel or DM:

```
!scrape <number_of_messages>
```

For example, to scrape 500 messages:

```
!scrape 500
```

### Step 6: Locate Output

Scraped messages are saved to:

```
scraped/<channel-name>/
```

Each file in that directory contains the extracted messages in plain text format.

## Platform-Specific Notes

### Windows

The `install.bat` and `start.bat` scripts handle the full workflow. Double-click or run from the terminal.

### Linux / macOS

No batch scripts are provided. Install dependencies with `pip install -r requirements.txt` and launch with `python main.py` (or `python3 main.py` depending on the system).

## Troubleshooting

- **Bot does not respond to `!scrape`**: Confirm the token in `config.json` is correct and the bot connected successfully (check terminal output for login confirmation).
- **Import errors on startup**: Re-run `pip install -r requirements.txt` inside the project directory.
- **Empty output files**: Verify the account has read access to the target channel.
- **Rate limiting**: Discord may throttle large scrape requests. Use smaller message counts and wait between requests.

## Additional Resources

- **`references/token-guide.md`** — How to find your Discord token safely
- **`references/tos-warning.md`** — Summary of Discord ToS risks and safer alternatives
- **`scripts/setup.sh`** — Linux/macOS setup helper script
