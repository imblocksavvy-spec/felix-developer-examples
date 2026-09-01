# Crypto risk review

Paste this into a Felix-enabled MCP client:

```text
Quote BTC and ETH, inspect the current account money map, and explain every
active account limit. Then compare current trend, volatility, and funding data
for the two assets.

Return:
- source timestamps and freshness
- current price and spread
- the dominant trend and volatility regime
- any unavailable data source
- the maximum action allowed by the current account policy

Do not authorize, fund, or place a trade.
```

Unavailable state must remain unavailable and must not be interpreted as zero.
