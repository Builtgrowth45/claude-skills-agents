"""
Discord channel scraper for sentiment analysis.
Reads message history from specified channels using a bot token.

Requirements:
    pip install discord.py aiohttp

Usage:
    DISCORD_BOT_TOKEN=your_token python scraper.py
"""

import asyncio
import csv
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

import discord

GUILD_IDS = []       # Leave empty to scrape all guilds the bot is in
CHANNEL_IDS = []     # Leave empty to scrape all text channels in each guild
LIMIT = 10_000       # Max messages per channel (None = all history)
OUTPUT_DIR = Path("output")


def clean_message(msg: discord.Message) -> dict:
    return {
        "id": str(msg.id),
        "channel_id": str(msg.channel.id),
        "channel_name": msg.channel.name,
        "guild_id": str(msg.guild.id) if msg.guild else None,
        "guild_name": msg.guild.name if msg.guild else None,
        "author_id": str(msg.author.id),
        "author_name": str(msg.author),
        "created_at": msg.created_at.isoformat(),
        "content": msg.content,
        "attachments": [a.url for a in msg.attachments],
        "reactions": [{"emoji": str(r.emoji), "count": r.count} for r in msg.reactions],
        "reply_to": str(msg.reference.message_id) if msg.reference else None,
    }


async def scrape_channel(channel: discord.TextChannel, limit: int | None) -> list[dict]:
    messages = []
    try:
        async for msg in channel.history(limit=limit, oldest_first=True):
            if msg.content:  # skip empty / attachment-only messages
                messages.append(clean_message(msg))
    except discord.Forbidden:
        print(f"  [skip] No permission: #{channel.name}")
    except discord.HTTPException as e:
        print(f"  [error] #{channel.name}: {e}")
    return messages


def save_json(data: list[dict], path: Path) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def save_csv(data: list[dict], path: Path) -> None:
    if not data:
        return
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        for row in data:
            # Flatten list fields for CSV
            row = row.copy()
            row["attachments"] = "; ".join(row["attachments"])
            row["reactions"] = "; ".join(
                f"{r['emoji']}x{r['count']}" for r in row["reactions"]
            )
            writer.writerow(row)


class ScraperClient(discord.Client):
    def __init__(self, guild_ids: list[int], channel_ids: list[int], limit: int | None):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(intents=intents)
        self.target_guild_ids = guild_ids
        self.target_channel_ids = channel_ids
        self.limit = limit

    async def on_ready(self):
        print(f"Logged in as {self.user} ({self.user.id})")
        OUTPUT_DIR.mkdir(exist_ok=True)

        guilds = (
            [g for g in self.guilds if g.id in self.target_guild_ids]
            if self.target_guild_ids
            else list(self.guilds)
        )

        all_messages: list[dict] = []

        for guild in guilds:
            print(f"\nGuild: {guild.name} ({guild.id})")
            channels = (
                [c for c in guild.text_channels if c.id in self.target_channel_ids]
                if self.target_channel_ids
                else guild.text_channels
            )

            guild_messages: list[dict] = []
            for channel in channels:
                print(f"  Scraping #{channel.name}...")
                msgs = await scrape_channel(channel, self.limit)
                print(f"    {len(msgs)} messages collected")
                guild_messages.extend(msgs)

            # Per-guild files
            slug = guild.name.lower().replace(" ", "_")
            save_json(guild_messages, OUTPUT_DIR / f"{slug}.json")
            save_csv(guild_messages, OUTPUT_DIR / f"{slug}.csv")
            print(f"  Saved {len(guild_messages)} messages for {guild.name}")
            all_messages.extend(guild_messages)

        # Combined output
        save_json(all_messages, OUTPUT_DIR / "all_messages.json")
        save_csv(all_messages, OUTPUT_DIR / "all_messages.csv")
        print(f"\nDone. Total: {len(all_messages)} messages → {OUTPUT_DIR}/")
        await self.close()


def main():
    token = os.environ.get("DISCORD_BOT_TOKEN")
    if not token:
        print("Error: set DISCORD_BOT_TOKEN environment variable")
        sys.exit(1)

    guild_ids = [int(x) for x in os.environ.get("GUILD_IDS", "").split(",") if x.strip()]
    channel_ids = [int(x) for x in os.environ.get("CHANNEL_IDS", "").split(",") if x.strip()]
    limit = int(os.environ.get("MESSAGE_LIMIT", LIMIT))

    client = ScraperClient(guild_ids, channel_ids, limit)
    client.run(token)


if __name__ == "__main__":
    main()
