# Direct API examples

These dependency-free Node.js examples use the Felix REST API directly.

Requirements:

- Node.js 20.10 or newer
- A Felix API key loaded from an application secret manager

Never paste a Felix key into source code, a prompt, a chat, a URL, or a committed environment file.

## Research

```bash
export FELIX_API_KEY="<load from your secret manager>"
node research.mjs BTC
```

The script checks runtime status and returns the current quote plus bounded research. It does not submit an order.

## Backtest

```bash
export FELIX_API_KEY="<load from your secret manager>"
node backtest.mjs BTC
```

The script submits a fixed manual strategy with a stable idempotency key. It does not deploy an agent or authorize execution.
