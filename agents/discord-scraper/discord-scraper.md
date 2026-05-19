# Discord Channel Scraper

Collects message history from Discord channels via the Bot API and exports to JSON + CSV for sentiment analysis.

## Setup

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure your bot
In the Discord Developer Portal:
- **Bot** tab → enable **Message Content Intent**
- Copy your **Bot Token** (Bot tab → Reset Token)
- Invite the bot to your server with `bot` + `Read Message History` scopes

### 3. Run

```bash
# Scrape all channels in all guilds the bot is in
DISCORD_BOT_TOKEN=your_token_here python scraper.py

# Scrape specific guilds/channels
DISCORD_BOT_TOKEN=your_token \
GUILD_IDS=123456789,987654321 \
CHANNEL_IDS=111222333 \
MESSAGE_LIMIT=5000 \
python scraper.py
```

### Environment variables

| Variable | Default | Description |
|---|---|---|
| `DISCORD_BOT_TOKEN` | required | Bot token from Developer Portal |
| `GUILD_IDS` | all guilds | Comma-separated guild IDs to target |
| `CHANNEL_IDS` | all channels | Comma-separated channel IDs to target |
| `MESSAGE_LIMIT` | 10000 | Max messages per channel (`0` = unlimited) |

## Output

Files are saved to `output/`:
- `<guild_name>.json` / `<guild_name>.csv` — per-guild exports
- `all_messages.json` / `all_messages.csv` — combined export

### Message schema

```json
{
  "id": "message snowflake",
  "channel_id": "...",
  "channel_name": "general",
  "guild_id": "...",
  "guild_name": "My Gaming Community",
  "author_id": "...",
  "author_name": "username#0000",
  "created_at": "2024-01-15T12:34:56+00:00",
  "content": "message text",
  "attachments": [],
  "reactions": [{"emoji": "👍", "count": 3}],
  "reply_to": null
}
```

## Sentiment Analysis

Load the CSV directly into pandas:

```python
import pandas as pd
df = pd.read_csv("output/all_messages.csv", parse_dates=["created_at"])

# Example: analyze with transformers
from transformers import pipeline
sentiment = pipeline("sentiment-analysis")
df["sentiment"] = df["content"].apply(lambda t: sentiment(t[:512])[0]["label"])
```
