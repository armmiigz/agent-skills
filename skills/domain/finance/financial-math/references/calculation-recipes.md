# Financial Calculation Recipes

Standard formulas for the Finance MVP.

## 1. CAGR (Compound Annual Growth Rate)
`((EndValue / StartValue) ^ (1 / Years)) - 1`

## 2. Real Return (Inflation Adjusted)
`((1 + NominalReturn) / (1 + InflationRate)) - 1`

## 3. Rule of 72 (Doubling Time)
`72 / AnnualInterestRate`

## 4. Savings Goal (Monthly Contribution)
`PMT(Rate, Periods, 0, FutureValue)`
- **Note**: Use a library like `financial` or `mathjs` for PMT functions to ensure precision.

## 5. Implementation Tip
Always use `Decimal` or `BigInt` for currency to avoid floating-point errors (e.g., `0.1 + 0.2 !== 0.3`).
