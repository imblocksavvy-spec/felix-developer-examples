# Prediction-market research

Paste this into a Felix-enabled MCP client:

```text
Find active prediction markets related to Bitcoin that resolve within the next
seven days. Use search_markets and return only canonical Felix instruments.

For each candidate, show:
- the exact question and resolution deadline
- YES and NO prices
- liquidity and current minimum size
- the source freshness and tradeability state
- the major ambiguity or resolution risk

Then choose the most liquid candidate and preview a $25 YES order. Show the
estimated fill, fees, collateral, funding path, and execution eligibility.
Do not authorize or place a trade.
```

This workflow uses real market data and stops at the preview boundary.
