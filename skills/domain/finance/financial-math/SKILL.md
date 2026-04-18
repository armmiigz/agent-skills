---
name: financial-math
description: Core mathematical formulas and implementation rules for finance. Covers Time Value of Money (TVM), CAGR, XIRR, and precision handling in code.
metadata:
  version: "1.0"
  triggers:
    - "calculate CAGR"
    - "calculate XIRR"
    - "TVM formula"
    - "finance math"
    - "compounding calculation"
---

# Financial Mathematics

## 1. Compound Annual Growth Rate (CAGR)
The mean annual growth rate of an investment over a specified period of time longer than one year.
- **Formula**: `((Ending Value / Beginning Value) ^ (1 / Number of Years)) - 1`
- **Use Case**: Comparing the performance of different assets over time.

## 2. Extended Internal Rate of Return (XIRR)
The internal rate of return for a series of cash flows that may not be periodic.
- **Why it matters**: Standard IRR assumes regular intervals (monthly/yearly). XIRR is essential for real-world investments where you buy/sell at irregular dates.
- **Calculation**: Requires iterative numerical methods (like Newton-Raphson). Usually handled by libraries (Excel, Python's `scipy` or `numpy-financial`).

## 3. Time Value of Money (TVM)
The concept that money available at the present time is worth more than the identical sum in the future.
- **Future Value (FV)**: `PV * (1 + r)^n`
- **Present Value (PV)**: `FV / (1 + r)^n`
- **Use Case**: Retirement planning (how much will my $100k be worth in 20 years?).

## 4. Real vs. Nominal Returns
- **Inflation Impact**: Returns must be adjusted for inflation to see the "Real" purchasing power.
- **Fisher Equation**: `(1 + Nominal Rate) = (1 + Real Rate) * (1 + Inflation Rate)`

## Implementation Rules (for Developers)
1. **Never use Floating Point for Money**: Use integers (cents/satang) or decimal libraries (e.g., `Decimal` in Python, `decimal.js` in JS) to avoid rounding errors (`0.1 + 0.2 !== 0.3`).
2. **Rounding**: Follow standard financial rounding (Round half to even/Banker's rounding) unless specified otherwise.
3. **Periodicity**: Be consistent with time units (e.g., if rate is annual, `n` must be in years).

## Verification Checklist
- [ ] Calculations handle inflation if looking at long-term projections.
- [ ] Floating point math is avoided for currency totals.
- [ ] XIRR is used for portfolios with irregular cash flows.
- [ ] Formula inputs (rates, periods) are validated for consistency.
