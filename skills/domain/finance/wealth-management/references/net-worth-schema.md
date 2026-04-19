# Net Worth Data Schema

Use this schema to structure financial data for analysis.

## 1. Assets (What you own)
- **Cash & Equivalents**: Checking, Savings, Emergency Fund.
- **Investments**: Stocks, Bonds, Mutual Funds, ETFs, Crypto.
- **Retirement**: 401k, IRA, Provident Fund.
- **Real Estate**: Primary Residence, Investment Property.
- **Business**: Equity in personal business.

## 2. Liabilities (What you owe)
- **Short-term**: Credit card debt, Personal loans.
- **Long-term**: Mortgage, Student loans, Car loans.

## 3. Data Structure (JSON Example)
```json
{
  "timestamp": "2024-04-19",
  "assets": {
    "cash": 50000,
    "investments": 150000,
    "real_estate": 450000
  },
  "liabilities": {
    "mortgage": 300000,
    "credit_card": 0
  },
  "net_worth": 350000
}
```
