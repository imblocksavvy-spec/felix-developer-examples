<p align="center">
  <img src="https://felix.trade/launch-assets/felix-developer-mark-128.png" width="88" height="88" alt="Felix" />
</p>

<h1 align="center">Felix developer examples</h1>

Agentic trading infrastructure for everyone. Connect an AI agent to one Felix account for crypto perpetuals, prediction markets and options, through MCP or the REST API.

## Connect in one line

Create a key in the [Felix app](https://app.felix.trade) under Developers, then add the hosted MCP server.

Claude Code:

```bash
claude mcp add --transport http felix https://mcp.felix.trade/mcp \
  --header "Authorization: Bearer fk_YOUR_KEY"
```

Cursor (`~/.cursor/mcp.json`) and any client that can send a header:

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

To sign on your own machine instead, install the local server:

```bash
npm install --global felix-mcp@latest
```

Its `create_account` tool lets an agent open its own account. The owner key stays on the machine, outside model context.

## Trade real money through the API

1. Register without the app: `POST /v1/register/challenge`, sign it with the owner wallet, then `POST /v1/register` returns a key.
2. Bind the owner, fund the Arc home with USDC, and finish setup.
3. Mint an owner-signed live key and place your first order with `POST /v1/orders`.

Every step is in [Registration](https://felix.trade/docs/api/registration). You can rehearse in simulation mode first.

## Agent frameworks

- [OpenAI Agents SDK](frameworks/openai-agents/agent.py)
- [LangChain and LangGraph](frameworks/langchain/agent.py)

Both connect to the hosted MCP server with your key. Run them with `FELIX_API_KEY` set.

## Install as an agent plugin

This repository follows the Agent Plugins 1.0 standard and also includes a
Cursor-specific manifest. The root `plugin.json`, root `mcp.json`, and
`.cursor-plugin/plugin.json` install the exact public Felix MCP release without
storing a credential in the repository.

Before installing the plugin in Cursor, VS Code, or GitHub Copilot, run guided
onboarding without modifying another client's configuration:

```bash
npx -y --package felix-mcp@latest \
  felix-keys onboard --accept-terms --client none
```

For Claude Desktop, use `--client claude` instead so onboarding can write the
Claude configuration for you.

Onboarding keeps the owner identity, Felix credential, and recovery material in
your system credential store. Installing the plugin does not fund an account or grant live
execution authority.

In VS Code, run `Chat: Install Plugin From Source` and enter:

```text
https://github.com/imblocksavvy-spec/felix-developer-examples
```

The same package can be submitted to Cursor Marketplace and loaded by other
Agent Plugins compatible clients.

## Try a workflow

- [Map Bitcoin across fragmented markets](prompts/cross-market-btc-map.md)
- [Prediction-market research](prompts/prediction-market-research.md)
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

## Links

- MCP package: [felix-mcp on npm](https://www.npmjs.com/package/felix-mcp)
- OpenAPI: [felix.trade/openapi.json](https://felix.trade/openapi.json)
- API base URL: `https://api.felix.trade`
- Documentation: [felix.trade/docs](https://felix.trade/docs)
- Runtime status: [felix.trade/status](https://felix.trade/status)
- Machine-readable guide: [felix.trade/llms.txt](https://felix.trade/llms.txt)

## Safety

Trading involves risk, including total loss. These examples are technical integration references, not investment advice. Read the [risk disclosure](https://felix.trade/legal/risk) and [custody model](https://felix.trade/legal/custody) before funding an account or granting execution authority.

## License

[MIT](LICENSE)
