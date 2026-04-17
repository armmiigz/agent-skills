import json
import os
import sys

def generate_review(workspace_path, output_file="review.html"):
    """
    Generates a static HTML review report for evaluation results.
    """
    if not os.path.exists(workspace_path):
        print(f"Error: Workspace path {workspace_path} does not exist.")
        return

    benchmark_file = os.path.join(workspace_path, "benchmark.json")
    benchmark = {}
    if os.path.exists(benchmark_file):
        with open(benchmark_file, 'r') as f:
            benchmark = json.load(f)

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Skill Evaluation Review - {os.path.basename(workspace_path)}</title>
        <style>
            body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica; line-height: 1.6; padding: 2rem; background: #f9f9f9; }}
            .container {{ max-width: 1000px; margin: 0 auto; background: white; padding: 2rem; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
            h1 {{ border-bottom: 2px solid #eee; padding-bottom: 0.5rem; }}
            .summary {{ background: #eef7ff; padding: 1rem; border-radius: 4px; margin-bottom: 2rem; }}
            .eval-card {{ border: 1px solid #ddd; border-radius: 4px; padding: 1rem; margin-bottom: 1.5rem; }}
            .status-pass {{ color: green; font-weight: bold; }}
            .status-fail {{ color: red; font-weight: bold; }}
            pre {{ background: #f4f4f4; padding: 1rem; overflow-x: auto; border: 1px solid #ccc; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Skill Evaluation Review</h1>
            <div class="summary">
                <strong>Pass Rate:</strong> {benchmark.get('summary', {}).get('pass_rate', 0):.1f}% | 
                <strong>Total Evals:</strong> {benchmark.get('summary', {}).get('total_evals', 0)}
            </div>
    """

    eval_dirs = [d for d in os.listdir(workspace_path) if d.startswith("eval-")]
    for eval_dir in sorted(eval_dirs):
        eval_path = os.path.join(workspace_path, eval_dir)
        with_skill_path = os.path.join(eval_path, "with_skill")
        
        # Try to find output files
        output_data = ""
        output_dir = os.path.join(with_skill_path, "outputs")
        if os.path.exists(output_dir):
            files = os.listdir(output_dir)
            if files:
                output_data = f"Output Files: {', '.join(files)}"

        html_content += f"""
            <div class="eval-card">
                <h3>{eval_dir}</h3>
                <p>Status: <span class="{'status-pass' if 'pass' in eval_dir else ''}">{eval_dir}</span></p>
                <div class="output">
                    <pre>{output_data or "No output data found."}</pre>
                </div>
            </div>
        """

    html_content += """
        </div>
    </body>
    </html>
    """

    output_path = os.path.join(workspace_path, output_file)
    with open(output_path, 'w') as f:
        f.write(html_content)

    print(f"Review report generated: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python generate_review.py <workspace_path>")
    else:
        generate_review(sys.argv[1])
