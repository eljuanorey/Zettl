from zettl import *

# Basic Commands group

@click.group(cls=ClickAliasedGroup)
def cli():
    pass

@cli.command(name="update-index", aliases=["upind"])
def call_update_index():
    folder_paths = get_config_parameter("data/config.json", "notes_folders")
    
    create_unique_tags_list("data/index_tags.json", "data/index_unique_tags.txt")

    index_tags = create_tags_index(folder_paths)
    save_tags_index(index_tags, "data/index_tags.json")

    index, index_of_index = create_index(folder_paths)
    save_index(index, index_of_index, "index", "index.md")

@cli.command(name="update-review-schedule", aliases=["uprev"])
def call_update_review_schedule():
    folder_paths = get_config_parameter("data/config.json", "notes_folders")
    
    review_schedule = create_review_schedule(folder_paths)
    save_review_schedule(review_schedule, "review-schedule", "review-schedule.md")
    copy_files(review_schedule, folder_paths, "to-review")

@cli.command(name="init")
@click.option('--blank', '-b', is_flag=True, help='Create a blank project.')
def call_init(blank):
    
    project_path = return_project_path()
    
    if blank:
        init_basic_structure(project_path)
        init_blank(project_path)
    else:
        init_basic_structure(project_path)
        init_default(project_path)
    
    folder_paths = get_config_parameter(project_path + "/data/config.json", "notes_folders")
    create_folder_structure(project_path, directory_structure=folder_paths)

# New commands group

@cli.group(cls=ClickAliasedGroup)
def new():
    pass

@new.command(name="note", aliases=["nn"])
@click.argument('folder_path', type=str)
@click.argument('note_title', type=str)
def note(folder_path, note_title):
    naming_convention = get_config_parameter("data/config.json", "notes_naming")
    if isinstance(naming_convention, (list, tuple)):
        naming_convention = naming_convention[0] if naming_convention else "%m%d%Y-%H%M.md"
    create_markdown_note(folder_path, note_title, naming_convention)

@new.command(name="folder", aliases=["nf"])
@click.argument('folder_name', type=str)
@click.argument('folder_path', type=str, required=False)
def folder(folder_name, folder_path):
    create_folder(folder_name, folder_path)

if __name__ == "__main__":
    cli()
