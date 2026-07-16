import os
import io

base_path = r"d:\TuMinhDucWorkshop\workshop-site\content"

def update_alwaysopen(folder):
    for ext in ["_index.md", "_index.vi.md"]:
        filepath = os.path.join(base_path, folder, ext)
        if os.path.exists(filepath):
            with io.open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            if "alwaysopen:" not in content:
                content = content.replace("---\n\n", "alwaysopen: true\n---\n\n")
                with io.open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)

update_alwaysopen("1-Worklog")
update_alwaysopen("3-BlogsPosted")
update_alwaysopen("4-EventParticipated")

print("Added alwaysopen: true to menus")
