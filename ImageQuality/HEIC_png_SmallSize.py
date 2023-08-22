import os
from wand.image import Image


def convert_heic_to_jpeg(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.endswith(".heic"):
            input_path = os.path.join(input_dir, filename)
            output_filename = os.path.splitext(filename)[0] + ".jpg"
            output_path = os.path.join(output_dir, output_filename)

            with Image(filename=input_path) as img:
                img.format = 'jpeg'
                img.save(filename=output_path)


def resize_images(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.endswith(".jpg"):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)

            with Image(filename=input_path) as img:
                img.resize(int(img.width * 0.33), int(img.height * 0.33))
                img.save(filename=output_path)


if __name__ == "__main__":
    heic_input_directory = "/Users/abasaltbahrami/Downloads/heic_images"
    jpeg_output_directory = "/Users/abasaltbahrami/Downloads/jpeg_images"
    resized_output_directory = "/Users/abasaltbahrami/Downloads/smaller_jpeg_images"

    convert_heic_to_jpeg(heic_input_directory, jpeg_output_directory)
    resize_images(jpeg_output_directory, resized_output_directory)

    print("Image conversion and resizing complete.")
