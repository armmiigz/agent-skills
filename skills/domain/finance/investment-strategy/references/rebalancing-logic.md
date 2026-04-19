# Rebalancing Logic Reference

How to calculate and execute portfolio rebalancing for the Finance MVP.

## 1. Drift Calculation
`Drift = Abs(CurrentWeight - TargetWeight)`

## 2. Rebalancing Trigger
- **Time-based**: Rebalance every quarter (90 days).
- **Threshold-based**: Rebalance if any asset drift > 5%.

## 3. Trade Execution Logic (Pseudo-code)
```typescript
function calculateTrades(portfolio, targets) {
  const totalValue = portfolio.reduce((sum, asset) => sum + asset.value, 0);
  
  return portfolio.map(asset => {
    const targetValue = totalValue * targets[asset.id];
    const diff = targetValue - asset.value;
    
    return {
      assetId: asset.id,
      action: diff > 0 ? 'BUY' : 'SELL',
      amount: Math.abs(diff)
    };
  });
}
```

## 4. Considerations
- **Taxes**: Selling might trigger capital gains taxes. Favor "Buy-only" rebalancing by putting new contributions into underweight assets first.
- **Transaction Costs**: Avoid small trades that cost more in fees than the benefit of rebalancing.
