import os
import argparse

def create_spec_scaffold(feature_id, feature_name):
    base_path = f"specs/{feature_id}-{feature_name}"
    files = {
        "plan.md": f"# Plan: {feature_name}\n\nTechnical strategy and architecture...",
        "spec.md": f"# Spec: {feature_name}\n\nUser stories and requirements...",
        "data-model.md": f"# Data Model: {feature_name}\n\nEntities and schemas...",
        "research.md": f"# Research: {feature_name}\n\nTechnical research and benchmarks...",
        "tasks.md": f"# Tasks: {feature_name}\n\nTODO list and tests..."
    }
    
    os.makedirs(base_path, exist_ok=True)
    os.makedirs(os.path.join(base_path, "contracts"), exist_ok=True)
    
    for filename, content in files.items():
        with open(os.path.join(base_path, filename), "w") as f:
            f.write(content)
            
    print(f"Scaffold created at: {base_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scaffold a new spec folder")
    parser.add_argument("--id", required=True, help="Feature ID (e.g., 001)")
    parser.add_argument("--name", required=True, help="Feature name (e.g., portfolio-manager)")
    
    args = parser.parse_args()
    create_spec_scaffold(args.id, args.name)
