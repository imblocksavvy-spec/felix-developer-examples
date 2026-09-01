# Backtest before authorization

Paste this into a Felix-enabled MCP client:

```text
Read felix://strategy/examples and write a simple BTC trend strategy using only
documented ctx helpers. Run a bounded historical backtest with 1-hour bars.

Report:
- the exact strategy code
- the effective parameters and historical data coverage
- total return, maximum drawdown, fees, and number of trades
- whether historical validity is valid or degraded
- every limitation that would matter before live use

Do not deploy an agent, authorize execution, fund an account, or place a trade.
```

A backtest result is evidence about one historical specification, not a promise of future performance.
