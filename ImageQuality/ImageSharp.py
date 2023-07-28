import os
from PIL import Image, ImageFilter


def sharpen_image(input_path, output_folder, sharpen_factor=2):
    try:
        # Open the input image
        input_image = Image.open(input_path)

        # Apply the sharpening filter
        sharpened_image = input_image.filter(
            ImageFilter.UnsharpMask(radius=2, percent=1000))

        # Create the output directory if it doesn't exist
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Get the filename without the path
        filename = os.path.basename(input_path)

        # Create a new image with both input and output side by side
        combined_image = Image.new(
            "RGB", (input_image.width * 2, input_image.height))
        combined_image.paste(input_image, (0, 0))
        combined_image.paste(sharpened_image, (input_image.width, 0))

        # Save the combined image for visual comparison
        combined_image_path = os.path.join(
            output_folder, f"sharp_{filename}")
        combined_image.save(combined_image_path)

        print(
            f"Combined image saved to: {combined_image_path}\n")
    except Exception as e:
        print(f"Error processing '{input_path}': {e}")


if __name__ == "__main__":
    input_folder = "/Users/abasaltbahrami/My Drive/InCor - Brazil/Microscope_Images/EntoCells"
    output_folder = input_folder

    # Get a list of all image files in the input folder
    image_files = [f for f in os.listdir(
        input_folder) if f.endswith((".bmp", ".jpg", ".png"))]

    # Process each image in the list
    for image_file in image_files:
        input_image_path = os.path.join(input_folder, image_file)
        sharpen_image(input_image_path, output_folder)
