from zettl import *

def create_folder(name, path):
    if not path:
        path = os.getcwd()
        
    folder_path = os.path.join(path, name)
    
    if os.path.exists(folder_path):
        click.echo(f"Folder '{name}' already exists at '{folder_path}'")
        return
    else:
        os.makedirs(folder_path, exist_ok=True)
        click.echo(f"Folder '{name}' created at '{folder_path}'")

def delete_folder(name, path):
    if not path:
        path = os.getcwd()
    
    folder_path = os.path.join(path, name)
    
    if os.path.exists(folder_path):  
        if not click.confirm(f"Are you sure you want to delete folder '{name}' at '{folder_path}'?"):
            return
        
        shutil.rmtree(folder_path)
        click.echo(f"Folder '{name}' deleted from '{folder_path}'")
    else:
        click.echo(f"Folder '{name}' does not exist at '{folder_path}'")
