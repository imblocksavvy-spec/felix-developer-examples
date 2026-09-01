import { felix } from "./felix-client.mjs";

const symbol = (process.argv[2] ?? "BTC").toUpperCase();
if (!/^[A-Z0-9._:-]{1,32}$/.test(symbol)) throw new Error("Invalid symbol.");

const code = `def think(ctx):
    price = ctx.price("${symbol}")
    if price is None:
        return {"action": "hold", "reason": "price unavailable"}
    return {"action": "hold", "reason": "collecting baseline"}`;

const result = await felix("/v1/backtests", {
  method: "POST",
  idempotencyKey: `example-${symbol.toLowerCase()}-baseline-v1`,
  body: {
    name: `${symbol} baseline`,
    strategy: { config: { code } },
    markets: [symbol],
    interval: "1h",
    bars: 250,
    capital: 100,
    detail: "summary",
  },
});

console.log(JSON.stringify(result, null, 2));
