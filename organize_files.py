import os
import shutil

def organize_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            file_ext = filename.split('.')[-1].lower()
            target_dir = os.path.join(folder_path, file_ext.upper())
            os.makedirs(target_dir, exist_ok=True)
            shutil.move(file_path, os.path.join(target_dir, filename))
    print("✅ Files have been organized successfully!")

# Example usage
# organize_folder("/path/to/your/Downloads")
