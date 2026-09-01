<p align="center">
  <img src="https://felix.trade/launch-assets/felix-developer-mark-128.png" width="88" height="88" alt="Felix Trade" />
</p>

<h1 align="center">Felix developer examples</h1>

Practical starting points for connecting AI agents to Felix through MCP or the direct API.

Felix provides owner-controlled trading infrastructure across supported prediction markets, crypto markets, and options. These examples begin with market data, account inspection, and backtests. Real-money execution exists only after separate owner authorization and remains subject to the account policy and current runtime state.

## Start with MCP

Requires Node.js 20.10 or newer on macOS.

```bash
npx -y --package felix-mcp@2.0.108 \
  felix-keys onboard --accept-terms --client claude
```

Review the [Felix terms](https://felix.trade/legal) before running onboarding. The owner identity and Felix credentials stay in macOS Keychain and outside model context.

After reconnecting your MCP client, start with:

```text
Read felix://getting-started. Call get_status and get_custody_recovery_status.
Require recovery ready, verify the active account, and quote BTC.
Do not authorize or place a trade.
```

Client configuration examples:

- [Claude Desktop](mcp/claude-desktop.json)
- [Cursor](mcp/cursor.json)
- [Codex](mcp/codex-config.toml)

### Cursor Marketplace package

This repository is also structured as a Cursor Plugin. The checked-in
`.cursor-plugin/plugin.json` and root `mcp.json` install the exact public Felix
MCP release without storing a credential in the repository.

Before connecting through Cursor, run guided onboarding with the Cursor client
selected:

```bash
npx -y --package felix-mcp@2.0.108 \
  felix-keys onboard --accept-terms --client cursor
```

Onboarding keeps the owner identity, Felix credential, and recovery material in
macOS Keychain. Installing the plugin does not fund an account or grant live
execution authority.

## Try a workflow

- [Map Bitcoin across fragmented markets](prompts/cross-market-btc-map.md)
- [Prediction-market research](prompts/polymarket-research.md)
- [Crypto risk review](prompts/crypto-risk-review.md)
- [Backtest before authorization](prompts/backtest-first-strategy.md)
- [Safe MCP workflow order](mcp/workflows.md)

The cross-market map is the best first example. It searches prediction markets, perpetuals, and options through the same Felix connection, then compares canonical instruments and read-only order previews without placing a trade.

## Use the API directly

The direct examples expect a Felix credential from your application secret manager. Never put a key, owner key, recovery code, seed phrase, signature, or signed transaction in a prompt, repository, URL, or log.

```bash
export FELIX_API_KEY="<load from your secret manager>"
node api/node/research.mjs BTC
node api/node/backtest.mjs BTC
```

See [api/node/README.md](api/node/README.md) for details.

## Current release

- MCP package: `felix-mcp@2.0.108`
- API base URL: `https://api.felix.trade`
- Documentation: [felix.trade/docs](https://felix.trade/docs)
- Runtime status: [felix.trade/status](https://felix.trade/status)
- Machine-readable guide: [felix.trade/llms.txt](https://felix.trade/llms.txt)

Pin the exact package version while validating an installation. Runtime status is the authority for current capabilities and venue availability.

## Safety

Trading involves risk, including total loss. These examples are technical integration references, not investment advice. Read the [risk disclosure](https://felix.trade/legal/risk) and [custody model](https://felix.trade/legal/custody) before funding an account or granting execution authority.

## License

[MIT](LICENSE)
