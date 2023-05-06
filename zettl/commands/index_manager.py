from zettl import *

def create_index(folder_paths, index_tags_path="data/index_tags.json"):
    index = "# Index\n\n"
    index_of_index = {}
    
    with open(index_tags_path, "r", encoding="utf-8") as tags_file:
        tags_data = json.load(tags_file)

    for folder_path in folder_paths:
        for dirpath, _, filenames in os.walk(folder_path):
            for filename in filenames:
                if filename.endswith(".md"):
                    filepath = os.path.join(dirpath, filename)
                    with open(filepath, "r", encoding="utf-8") as f:
                        md_title = ""
                        for line in f:
                            if line.startswith("# "):
                                md_title = line[2:].strip()
                                break
                        if not md_title:
                            md_title = filename[:-3].title()

                        relative_path = os.path.join("..",os.path.relpath(filepath))
                        index += f"- [{filename[:-3]}]({relative_path}) : {md_title}\n"

                        if filename in tags_data:
                            tags_list = tags_data[filename]
                            for tag in tags_list:
                                if tag not in index_of_index:
                                    index_of_index[tag] = f"\n# {tag.title()}\n\n"
                                index_of_index[tag] += f"- [{filename[:-3]}]({relative_path}) : {md_title}\n"

    return index, index_of_index

def save_index(index, index_of_index, file_path, file_name):
    with open(os.path.join(file_path, file_name), "w", encoding="utf-8") as f:
        f.write(index)
        for tag_index in index_of_index.values():
            f.write(tag_index)

