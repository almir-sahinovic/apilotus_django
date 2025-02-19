#clear_migrations.py
"""
Run this file from a Django =1.8 project root.
Removes all migration files from all apps in a project.
"""
from unipath import Path

this_file = Path(__file__).absolute()
current_dir = this_file.parent + '\\apps'
dir_list = current_dir.listdir()

for paths in dir_list:
    migration_folder = paths.child('migrations')
    if migration_folder.exists():
        list_files = migration_folder.listdir()
        for files in list_files:
            split = files.components()
            if split[-1] != Path('__init__.py') and split[-1] != Path('__pycache__'):
                files.remove()
