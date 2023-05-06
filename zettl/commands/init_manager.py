from zettl import *

def return_project_path(path='', name='zettlekasten'):
    project_path = os.path.join(path, name)
    return project_path 

def create_folder_structure(project_path, directory_structure=[]):
    # Create the project directory structure
    
    for folder in directory_structure:
        os.makedirs(os.path.join(project_path, folder))

    # Print a success message
    click.echo(f"Project initialized at {project_path}.")


def init_basic_structure(project_path):
    
    if os.path.exists(project_path):
        click.echo(f"Directory {project_path} already exists.")
        return

    # Create the default directorys
    
    os.makedirs(os.path.join(project_path, 'data'))
    os.makedirs(os.path.join(project_path, 'index'))
    os.makedirs(os.path.join(project_path, 'review-schedule'))
    os.makedirs(os.path.join(project_path, 'to-review'))

    # Create the default files
    
    with open(os.path.join(project_path + '\\data', 'index_tags.json'), 'w') as f:
        f.write("""{ }""")
    
    with open(os.path.join(project_path + '\\data', 'index_unique_tags.txt'), 'w') as f:
        f.write("""{ }""")
    
    with open(os.path.join(project_path + '\\index', 'index.md'), 'w') as f:
        f.write("""# Index""")
    
    with open(os.path.join(project_path + '\\review-schedule', 'review-schedule.md'), 'w') as f:
        f.write("""# Review Schedule""")

def init_default(project_path):
    with open(os.path.join(project_path + '\\data', 'config.json'), 'w') as f:
        f.write(""" 
{
    "_comment1": "this is for the folders that you want to store the notes in",
    "notes_folders": [
        "fleeting-notes",
        "literature-notes",
        "permanent-notes",
        "project-notes"
    ],
    "_comment2": "Notes naming comvention, for defult: MMDDYYYY-HHMM.md",
    "notes_naming": [
        "%m%d%Y-%H%M.md"
    ]
}             
""")

def init_blank(project_path):
    with open(os.path.join(project_path + '\\data', 'config.json'), 'w') as f:
        f.write(""" 
{
    "_comment1": "this is for the folders that you want to store the notes in",
    "notes_folders": [
    ],
    "_comment2": "Notes naming comvention, for defult: MMDDYYYY-HHMM.md",
    "notes_naming": [
        "%m%d%Y-%H%M.md"
    ]
}             
""")

def create_folder_structure(project_path, directory_structure=[]):    
    for folder in directory_structure:
        os.makedirs(os.path.join(project_path, folder))
