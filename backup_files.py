import shutil
import os
from datetime import datetime

def backup_files(source_folder, backup_folder):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    dest = os.path.join(backup_folder, f"backup_{timestamp}")
    shutil.copytree(source_folder, dest)
    print(f"🗂️ Backup completed: {dest}")

# Example usage
# backup_files("/path/to/source", "/path/to/backup")
