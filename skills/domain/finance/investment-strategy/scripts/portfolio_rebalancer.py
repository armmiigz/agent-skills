import json

def calculate_rebalance(current_values, target_percentages):
    """
    Calculates buy/sell amounts to reach target allocation.
    current_values: {"stocks": 6000, "bonds": 4000}
    target_percentages: {"stocks": 0.7, "bonds": 0.3}
    """
    total_value = sum(current_values.values())
    rebalance_plan = {}
    
    for asset, target_pct in target_percentages.items():
        current_val = current_values.get(asset, 0)
        target_val = total_value * target_pct
        diff = target_val - current_val
        
        rebalance_plan[asset] = {
            "current_value": current_val,
            "target_value": target_val,
            "adjustment": diff,
            "action": "BUY" if diff > 0 else "SELL" if diff < 0 else "NONE"
        }
        
    return {
        "total_value": total_value,
        "plan": rebalance_plan
    }

# Example Usage
if __name__ == "__main__":
    # Current portfolio drifted: Stocks became 80%, Bonds 20%
    current = {"stocks": 8000, "bonds": 2000}
    # Target: 60/40
    target = {"stocks": 0.6, "bonds": 0.4}
    
    result = calculate_rebalance(current, target)
    print(json.dumps(result, indent=2))
