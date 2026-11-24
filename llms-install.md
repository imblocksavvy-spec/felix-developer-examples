# Install Felix MCP

Use these steps when helping a developer connect Felix to an MCP client.

## Option 1: hosted server (any OS)

The developer creates a key in the Felix app (https://app.felix.trade, Developers, then API keys). Never ask them to paste the key into chat; they add it to their client configuration themselves.

Claude Code:

```bash
claude mcp add --transport http felix https://mcp.felix.trade/mcp \
  --header "Authorization: Bearer fk_YOUR_KEY"
```

Clients that take JSON:

```json
{
  "mcpServers": {
    "felix": {
      "url": "https://mcp.felix.trade/mcp",
      "headers": { "Authorization": "Bearer fk_YOUR_KEY" }
    }
  }
}
```

## Option 2: local server with on-device signing

Requires Node.js 20.10 or newer, on macOS, Windows or Linux. The developer reviews https://felix.trade/legal, then runs this in their own terminal:

```bash
npx -y --package felix-mcp@2.0.136 \
  felix-keys onboard --accept-terms --client none
```

The owner identity, credential, and recovery material stay in the system credential store: Keychain on macOS, protected storage on Windows, the keyring on Linux, or an encrypted file only the user can read when no keyring exists. Do not ask the developer to paste any key, recovery code, seed phrase, signature, or signed transaction into chat, source control, a URL, or a log.

Then use this stdio configuration:

```json
{
  "mcpServers": {
    "felix": {
      "command": "npx",
      "args": ["-y", "felix-mcp@2.0.136"]
    }
  }
}
```

## Verify the read-only path

Restart the MCP client, then ask the agent:

```text
Call get_status and quote BTC. Do not place a trade.
```

Installing the MCP does not fund an account or grant live trading. The owner authorizes live trading separately, and every live action stays inside the limits the owner signed.
