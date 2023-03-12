from PIL import Image
import os

# Define the path to your image directory
image_dir = "/Users/abasaltbahrami/Downloads/events_website"

# Loop through all files in the directory
for filename in os.listdir(image_dir):
    if filename.endswith(".jpg") or filename.endswith(".png"):

        # Open the image using Pillow
        img = Image.open(os.path.join(image_dir, filename))

        # Resize the image to have a width of 100
        wpercent = (100 / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((100, hsize), Image.LANCZOS)

        # Save the processed image with a new filename
        img.save(os.path.join(image_dir, "processed_" + filename))
