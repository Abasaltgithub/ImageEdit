import os
from PIL import Image, ImageDraw, ImageOps

# Set the directory path where the images are located
directory = "/Users/abasaltbahrami/Downloads/Magnet pics/"

# Loop through all files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):

        # Open the image file
        img_path = os.path.join(directory, filename)
        img = Image.open(img_path)

        # Create a mask image for the circle crop
        size = min(img.size)
        mask = Image.new("L", (size, size), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + (size, size), fill=255)

        # Apply the mask to the image
        cropped_img = ImageOps.fit(img, mask.size, centering=(0.5, 0.5))
        cropped_img.putalpha(mask)

        # Save the cropped image with a new filename
        cropped_filename = os.path.splitext(filename)[0] + "_cropped.png"
        cropped_path = os.path.join(directory, cropped_filename)
        cropped_img.save(cropped_path)

print("Done!")
