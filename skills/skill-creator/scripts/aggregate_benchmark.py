import json
import os
import sys
from datetime import datetime

def aggregate_benchmark(workspace_path):
    """
    Aggregates grading.json and timing.json from eval directories.
    """
    benchmark_data = {
        "timestamp": datetime.now().isoformat(),
        "evals": [],
        "summary": {
            "total_evals": 0,
            "pass_rate": 0,
            "avg_duration": 0
        }
    }

    total_passed = 0
    total_assertions = 0
    total_duration = 0

    if not os.path.exists(workspace_path):
        print(f"Error: Workspace path {workspace_path} does not exist.")
        return

    # Iterate through eval-X directories
    eval_dirs = [d for d in os.listdir(workspace_path) if d.startswith("eval-")]
    for eval_dir in sorted(eval_dirs):
        eval_path = os.path.join(workspace_path, eval_dir)
        
        # We look for 'with_skill' results
        with_skill_path = os.path.join(eval_path, "with_skill")
        if not os.path.exists(with_skill_path):
            continue

        grading_file = os.path.join(with_skill_path, "grading.json")
        timing_file = os.path.join(with_skill_path, "timing.json")

        eval_result = {
            "id": eval_dir,
            "passed": False,
            "duration_ms": 0,
            "score": 0
        }

        if os.path.exists(grading_file):
            with open(grading_file, 'r') as f:
                grading = json.load(f)
                assertions = grading.get("expectations", [])
                passed_count = sum(1 for a in assertions if a.get("passed"))
                eval_result["score"] = f"{passed_count}/{len(assertions)}"
                eval_result["passed"] = passed_count == len(assertions)
                total_passed += passed_count
                total_assertions += len(assertions)

        if os.path.exists(timing_file):
            with open(timing_file, 'r') as f:
                timing = json.load(f)
                eval_result["duration_ms"] = timing.get("duration_ms", 0)
                total_duration += eval_result["duration_ms"]

        benchmark_data["evals"].append(eval_result)

    # Calculate summary
    if total_assertions > 0:
        benchmark_data["summary"]["pass_rate"] = (total_passed / total_assertions) * 100
    if len(benchmark_data["evals"]) > 0:
        benchmark_data["summary"]["avg_duration"] = total_duration / len(benchmark_data["evals"])
    benchmark_data["summary"]["total_evals"] = len(benchmark_data["evals"])

    # Save outputs
    with open(os.path.join(workspace_path, "benchmark.json"), 'w') as f:
        json.dump(benchmark_data, f, indent=2)

    print(f"Benchmark aggregated: {workspace_path}/benchmark.json")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python aggregate_benchmark.py <workspace_path>")
    else:
        aggregate_benchmark(sys.argv[1])
