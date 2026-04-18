import json
from datetime import datetime

def calculate_net_worth(data):
    """
    Calculates total assets, total liabilities, and net worth.
    Input data format:
    {
        "assets": {"cash": 1000, "stocks": 5000, ...},
        "liabilities": {"credit_card": 200, "loan": 1000, ...}
    }
    """
    total_assets = sum(data.get("assets", {}).values())
    total_liabilities = sum(data.get("liabilities", {}).values())
    net_worth = total_assets - total_liabilities
    
    return {
        "timestamp": datetime.now().isoformat(),
        "total_assets": total_assets,
        "total_liabilities": total_liabilities,
        "net_worth": net_worth,
        "debt_to_asset_ratio": (total_liabilities / total_assets) if total_assets > 0 else 0
    }

# Example Usage
if __name__ == "__main__":
    my_finances = {
        "assets": {
            "savings": 50000,
            "brokerage": 120000,
            "crypto": 15000,
            "home_value": 350000
        },
        "liabilities": {
            "mortgage": 280000,
            "car_loan": 12000,
            "credit_card": 1500
        }
    }
    
    result = calculate_net_worth(my_finances)
    print(json.dumps(result, indent=2))
