# Discord Terms of Service — Selfbot Risk Summary

## What Is a Selfbot?

A selfbot is a bot that logs in using a regular user account token (as opposed to a bot token issued through the Discord Developer Portal). Discord's API was not designed for automated user accounts.

## TOS Violation

Discord's Terms of Service explicitly prohibit:

> "Using third-party software or modifying the client to automate actions, including automated messaging, scraping, or accessing APIs in ways not permitted."

Running a selfbot — including discord-scraper — falls under this prohibition.

## Possible Consequences

- **Account warning** — first-time or low-activity cases.
- **Temporary suspension** — moderate automation detected.
- **Permanent ban** — repeated violations or if another user reports the account.

## Risk Factors That Increase Ban Likelihood

- Scraping large numbers of messages quickly (triggers rate-limit alarms).
- Scraping channels you do not own or administer.
- Another user noticing the automated behavior and reporting the account.

## Safer Alternatives

If the goal is to archive your own server's messages, consider:

- **Official Data Request**: Discord lets users download their own data at User Settings → Privacy & Safety → Request all of my data.
- **Discord Bot (official)**: Create a bot application at discord.com/developers and add it to a server you own. Bots operate within TOS and have explicit permission scopes.
- **DiscordChatExporter**: An open-source tool that uses bot tokens and respects rate limits. Available at github.com/Tyrrrz/DiscordChatExporter.

## Acknowledgement

Proceed with discord-scraper only after fully understanding and accepting these risks.
