# Finding Your Discord Token

A Discord user token is required for `config.json`. This is your personal account token — treat it like a password.

## Method: Browser DevTools (Web Client)

1. Open Discord in a browser (discord.com/app).
2. Press `F12` (or `Ctrl+Shift+I` / `Cmd+Option+I`) to open DevTools.
3. Go to the **Network** tab.
4. Reload the page or interact with Discord (send a message).
5. In the filter box, type `api`.
6. Select any API request in the list.
7. Under **Request Headers**, find the `Authorization` header.
8. The value is your token.

## Security Reminders

- Never share your token with anyone.
- Never commit it to a public repository.
- Paste the token only into the local `config.json` file.
- If a token is ever exposed, immediately change your Discord password (this invalidates the token).

## Invalidating a Compromised Token

Change your Discord account password. This immediately revokes the current token and generates a new one.
