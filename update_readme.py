import utils.session
import os

# Paths to ignore
IGNORE_DIRS = {'.git', '.github', '__pycache__'}

def list_projects(base_path='.'):
    projects = {}
    for root, dirs, files in os.walk(base_path):
        # Skip ignored directories and nested utils or hidden folders
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS and not d.startswith('.')]
        if root == base_path:
            continue  # Skip root
        category = os.path.basename(root)
        py_files = [f for f in files if f.endswith('.py')]
        if py_files:
            projects[category] = py_files
    return projects

def generate_readme(projects):
    header = """# 🧠 Deep Learning Models

Automatically generated list of deep learning projects.  
Every time you push new models, this README updates automatically.

---

## 📂 Repository Structure
"""
    structure = "```\nDeep-Learning-Models/\n"
    for category, files in projects.items():
        structure += f"├── {category}/\n"
        for f in files:
            structure += f"│   └── {f}\n"
    structure += "└── README.md\n```\n\n"

    table_header = "## 📊 Project List\n\n| Category | Model | Description |\n|-----------|--------|-------------|\n"
    table_rows = ""
    for category, files in projects.items():
        for f in files:
            table_rows += f"| **{category}** | {f} | - |\n"
    table = table_header + table_rows + "\n"

    footer = """---

## 🧩 Technologies
- Python 3.10 
- TensorFlow / Keras / PyTorch  
- NumPy, Pandas, Matplotlib  

---

✅ *This README is auto-generated via `update_readme.py`*
"""
    return header + structure + table + footer


if __name__ == "__main__":
    projects = list_projects('.')
    readme_content = generate_readme(projects)

    with open('README.md', 'w') as f:
        f.write(readme_content)

    print("✅ README.md updated successfully.")
