import os
import json
import shutil
import click
from click_aliases import ClickAliasedGroup

from datetime import datetime, timedelta
from collections import defaultdict

from .commands.index_manager import save_index, create_index
from .commands.schedule_manager import create_review_schedule, copy_files, save_review_schedule
from .utils.index_tags import create_tags_index, save_tags_index
from .utils.index_unique_tags import create_unique_tags_list
from .commands.note_manager import create_markdown_note
from .commands.folder_manager import create_folder, delete_folder
from .commands.init_manager import init_default, init_blank, init_basic_structure, create_folder_structure, return_project_path
from .utils.config import get_config_parameter
