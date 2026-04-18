from decimal import Decimal, getcontext

# Set precision for financial calculations
getcontext().prec = 28

def calculate_cagr(beginning_value, ending_value, years):
    """
    CAGR = ((EV / BV) ^ (1 / n)) - 1
    """
    bv = Decimal(str(beginning_value))
    ev = Decimal(str(ending_value))
    n = Decimal(str(years))
    
    cagr = (ev / bv) ** (Decimal('1') / n) - Decimal('1')
    return float(cagr)

def calculate_future_value(present_value, annual_rate, years):
    """
    FV = PV * (1 + r)^n
    """
    pv = Decimal(str(present_value))
    r = Decimal(str(annual_rate))
    n = Decimal(str(years))
    
    fv = pv * (Decimal('1') + r) ** n
    return float(fv)

def calculate_real_return(nominal_rate, inflation_rate):
    """
    Real Rate = ((1 + Nominal) / (1 + Inflation)) - 1
    """
    n = Decimal(str(nominal_rate))
    i = Decimal(str(inflation_rate))
    
    real = ((Decimal('1') + n) / (Decimal('1') + i)) - Decimal('1')
    return float(real)

# Example Usage
if __name__ == "__main__":
    # $10,000 growing to $25,000 in 10 years
    print(f"CAGR: {calculate_cagr(10000, 25000, 10):.2%}")
    
    # $100,000 at 7% for 20 years
    print(f"FV: ${calculate_future_value(100000, 0.07, 20):,.2f}")
    
    # 10% nominal return with 3% inflation
    print(f"Real Return: {calculate_real_return(0.10, 0.03):.2%}")
