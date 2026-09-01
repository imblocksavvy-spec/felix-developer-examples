# Map Bitcoin across fragmented markets

Use this prompt after completing Felix MCP onboarding. It produces a read-only map of Bitcoin exposure across prediction markets, perpetuals, and options without authorizing or placing a trade.

```text
Read felix://getting-started, then call get_status.

Search for Bitcoin instruments in each supported market category:

1. Call search_markets with q "bitcoin", kind "pm", and limit 10.
2. Call search_markets with q "BTC", kind "crypto", and limit 10.
3. Call search_markets with q "BTC", kind "option", and limit 20.

Keep only canonical instruments that the current runtime reports as tradeable.
For each category, choose the strongest available candidate and report:

- canonical instrument and venue
- what exposure it represents
- current price or quote
- minimum size
- available liquidity and data freshness
- collateral or settlement currency
- any runtime restriction or missing capability

If preview_order is available for a candidate, preview a $25 buy without
submitting it. Include estimated fill, fees, collateral, total owner debit,
execution eligibility, and the exact reason when it is not executable.

Finish with a compact table comparing prediction markets, perpetuals, and
options. Separate facts returned by Felix from your own interpretation.
Do not authorize, fund, place, or close any trade.
```

Relevant guides:

- [Prediction markets](https://felix.trade/prediction-markets-mcp?utm_source=github&utm_medium=example&utm_campaign=developer_infrastructure&utm_content=cross_market_btc)
- [Perpetual markets](https://felix.trade/perpetuals-mcp?utm_source=github&utm_medium=example&utm_campaign=developer_infrastructure&utm_content=cross_market_btc)
- [Options markets](https://felix.trade/options-trading-mcp?utm_source=github&utm_medium=example&utm_campaign=developer_infrastructure&utm_content=cross_market_btc)
- [Felix setup](https://felix.trade/start?utm_source=github&utm_medium=example&utm_campaign=developer_infrastructure&utm_content=cross_market_btc)

