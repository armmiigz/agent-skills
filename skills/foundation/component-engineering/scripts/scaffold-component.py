import os
import argparse

def scaffold_component(name, path):
    target_dir = os.path.join(path, name)
    os.makedirs(target_dir, exist_ok=True)
    
    files = {
        "index.ts": f"export * from './{name}';",
        f"{name}.tsx": f"export const {name} = () => <div>{name}</div>;",
        f"{name}.stories.tsx": f"import {{ {name} }} from './{name}';\nexport default {{ component: {name} }};",
        f"{name}.test.tsx": f"import {{ render }} from '@testing-library/react';\nimport {{ {name} }} from './{name}';\ntest('renders', () => {{ render(<{name} />); }});"
    }
    
    for filename, content in files.items():
        with open(os.path.join(target_dir, filename), "w") as f:
            f.write(content)
            
    print(f"Component {name} created at {target_dir}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", required=True)
    parser.add_argument("--path", default="apps/web/src/components")
    args = parser.parse_args()
    scaffold_component(args.name, args.path)
