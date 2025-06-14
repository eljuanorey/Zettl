from zettl import *

def create_markdown_note(folder_path, note_title, naming_convention="%m%d%Y-%H%M.md"):
    # Create the folder if it doesn't exist
    if not os.path.exists(folder_path) and folder_path != "":
        os.makedirs(folder_path)

    # Get the current date and time
    now = datetime.now()

    # Create the filename for the note
    filename = now.strftime(naming_convention)

    # Construct the full path to the file
    file_path = os.path.join(folder_path, filename)

    # Open the file and write the title
    with open(file_path, "w") as f:
        f.write("# "+ note_title + "\n")

    with open(file_path, "r+") as f:
        f.seek(0, 2)  # Go to the end of the file
        f.write(f"Created: {now.strftime('%m/%d/%Y %H:%M')}")
    
    with open(file_path, "r+") as f:
        f.seek(0, 2)  # Go to the end of the file
        f.write(f"\n\n### Tags\n #tag1 #tag2 #tag3")

    # Print a message indicating success
    print(f"Note created: {file_path}")

