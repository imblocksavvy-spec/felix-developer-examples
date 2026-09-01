# Safe MCP workflow order

Use this order when connecting a new MCP client or evaluating a new Felix release.

## 1. Verify the runtime and account

```text
Read felix://getting-started.
Call get_status and get_custody_recovery_status.
Require recovery ready and report the active account and current limits.
Do not authorize or place a trade.
```

## 2. Resolve instruments instead of guessing

```text
Use search_markets for Bitcoin. Return the canonical instruments, venue,
tradeability, minimum size, liquidity, and data freshness for each candidate.
Do not authorize or place a trade.
```

## 3. Preview the full money path

```text
Preview a $25 long position in the selected canonical instrument.
Show estimated fill, fees, collateral, funding requirements, execution
eligibility, and every owner action that would be required. Do not place it.
```

## 4. Review authority separately

```text
Show the exact proposed markets, contracts, spend ceiling, position ceiling,
expiry, and emergency controls. Explain what the agent can and cannot do.
Do not authorize anything until the owner explicitly approves those terms.
```

## 5. Reconcile after an authorized action

```text
Read the operation status, current positions, fills, PnL, and money map.
Treat a submitted request as unconfirmed until the venue and Felix state agree.
Do not repeat an ambiguous request with a new idempotency key.
```
