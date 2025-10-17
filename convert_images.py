from PIL import Image
import os

def convert_images(folder_path, output_format="JPEG"):
    for filename in os.listdir(folder_path):
        if filename.lower().endswith((".png", ".jpg", ".jpeg")):
            img_path = os.path.join(folder_path, filename)
            img = Image.open(img_path)
            new_filename = os.path.splitext(filename)[0] + "." + output_format.lower()
            img.convert("RGB").save(os.path.join(folder_path, new_filename), output_format)
    print("🖼️ All images converted successfully!")

# Example usage
# convert_images("/path/to/images", "JPEG")
