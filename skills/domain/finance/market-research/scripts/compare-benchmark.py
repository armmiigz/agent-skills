import argparse

def calculate_performance_diff(asset_return, benchmark_return):
    """
    Calculates the 'Alpha' (performance over benchmark).
    """
    alpha = asset_return - benchmark_return
    return alpha

def generate_summary(asset_name, asset_return, benchmark_name, benchmark_return):
    alpha = calculate_performance_diff(asset_return, benchmark_return)
    status = "OUTPERFORMED" if alpha > 0 else "UNDERPERFORMED"
    
    print(f"--- Investment Research Summary ---")
    print(f"Asset: {asset_name} ({asset_return}%)")
    print(f"Benchmark: {benchmark_name} ({benchmark_return}%)")
    print(f"Result: {asset_name} {status} the benchmark by {abs(alpha):.2f}%")
    print(f"----------------------------------")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compare asset return against a benchmark")
    parser.add_argument("--asset", required=True, help="Asset name")
    parser.add_argument("--asset_return", type=float, required=True, help="Asset annual return (%)")
    parser.add_argument("--benchmark", required=True, help="Benchmark name")
    parser.add_argument("--benchmark_return", type=float, required=True, help="Benchmark annual return (%)")
    
    args = parser.parse_args()
    generate_summary(args.asset, args.asset_return, args.benchmark, args.benchmark_return)
