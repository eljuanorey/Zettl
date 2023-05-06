from zettl import *

def extract_tags_from_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        tags_index = content.find("### Tags")
        if tags_index == -1:
            return []
        tags_text = content[tags_index:]
        tags_lines = tags_text.split("\n")[1:]
        tags = [tag.strip() for tag in tags_lines if tag.strip()]
        return tags

def transform_tags(tag_list):
    return [tag.strip() for tag_string in tag_list for tag in tag_string.split("#") if tag]

def create_tags_index(folder_paths):
    tags_index = defaultdict(list)
    for folder_path in folder_paths:
        for root, _, files in os.walk(folder_path):
            for filename in files:
                if filename.endswith(".md"):
                    file_path = os.path.join(root, filename)
                    tags = extract_tags_from_file(file_path)
                    tags = transform_tags(tags)
                    tags_index[filename].extend(tags)
    # remove empty or duplicate tags
    tags_index = {filename: list(set(tags)) for filename, tags in tags_index.items() if tags}
    return tags_index

def save_tags_index(tags_index, export_path):
    with open(export_path, "w", encoding="utf-8") as f:
        json.dump(tags_index, f, indent=4, ensure_ascii=False)