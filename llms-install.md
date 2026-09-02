# Install Felix MCP

Use these steps when helping a developer connect Felix to an MCP client.

## Requirements

- macOS
- Node.js 20.10 or newer
- A local terminal outside model context

## 1. Review terms and create the local identity

The developer should review https://felix.trade/legal, then run this command in
their own terminal:

```bash
npx -y --package felix-mcp@2.0.108 \
  felix-keys onboard --accept-terms --client none
```

Felix stores the owner identity, credential, and recovery material in macOS
Keychain. Do not ask the developer to paste any key, recovery code, seed phrase,
signature, or signed transaction into chat, source control, a URL, or a log.

Claude Desktop users may choose `--client claude` instead so onboarding writes
the Claude configuration automatically.

## 2. Configure the MCP client

Use this stdio configuration:

```json
{
  "mcpServers": {
    "felix": {
      "command": "npx",
      "args": ["-y", "felix-mcp@2.0.108"]
    }
  }
}
```

VS Code can install the complete Agent Plugin by running
`Chat: Install Plugin From Source` and entering:

```text
https://github.com/imblocksavvy-spec/felix-developer-examples
```

## 3. Verify the read-only path

Restart the MCP client, then ask the agent:

```text
Read felix://getting-started. Call get_status and get_custody_recovery_status.
Require recovery ready, verify the active account, and quote BTC.
Do not authorize or place a trade.
```

Installing the MCP does not fund an account or grant live execution authority.
The owner must separately authorize any live capability, and every live action
remains subject to the account policy and current runtime state.
