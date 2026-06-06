import os
import json

def build_index(path, ignore_dirs=None):
    if ignore_dirs is None:
        ignore_dirs = {'.git', '.github', '.vscode'}
    
    entries = []
    
    # Get sorted items in the directory
    try:
        items = sorted(os.listdir(path))
    except OSError:
        return []
    
    for item in items:
        full_path = os.path.join(path, item)
        
        # Skip hidden files and ignored directories
        if item.startswith('.') or item in ignore_dirs:
            continue
            
        if os.path.isdir(full_path):
            # Recursively build for directories
            sub_entries = build_index(full_path, ignore_dirs)
            if sub_entries:
                # Add folder as {name: [contents]}
                entries.append({item: sub_entries})
        
        elif item.lower().endswith('.md'):
            # Only add Markdown files
            entries.append(item)
            
    return entries

def main():
    root_path = "."
    print(f"Generating index.json for: {os.path.abspath(root_path)}")
    
    index_data = build_index(root_path)
    
    with open("index.json", "w", encoding="utf-8") as f:
        json.dump(index_data, f, indent=2, ensure_ascii=False)
        
    print("Success! index.json has been created.")

if __name__ == "__main__":
    main()
