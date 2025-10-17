from PIL import Image
from PIL.ExifTags import TAGS
import os

def rename_photos_by_date(folder_path):
    for filename in os.listdir(folder_path):
        if filename.lower().endswith((".jpg", ".jpeg")):
            path = os.path.join(folder_path, filename)
            img = Image.open(path)
            exif_data = img.getexif()
            for tag, value in exif_data.items():
                if TAGS.get(tag) == "DateTimeOriginal":
                    date = value.replace(":", "").replace(" ", "_")
                    new_name = f"{date}.jpg"
                    os.rename(path, os.path.join(folder_path, new_name))
                    print(f"Renamed {filename} → {new_name}")
                    break
    print("📸 All photos renamed by date!")

# Example usage
# rename_photos_by_date("/path/to/photos")
