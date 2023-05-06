from zettl import *

def create_unique_tags_list(import_path, export_path):
    # Read in JSON file
    with open(import_path, "r") as f:
        data = json.load(f)

    # Create set of unique tags
    unique_tags = set()
    for tags in data.values():
        unique_tags.update(tags)

    # Write unique tags to file
    with open(export_path, "w") as f:
        for tag in sorted(unique_tags):
            f.write(tag + "\n")
