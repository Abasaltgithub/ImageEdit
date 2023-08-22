from PIL import Image
import os


def compress_images(input_dir, output_dir, compression_quality):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.lower().endswith('.jpg'):
            img_path = os.path.join(input_dir, filename)
            img = Image.open(img_path)

            output_path = os.path.join(output_dir, filename)
            img.save(output_path, quality=compression_quality)

    print("Image compression completed.")


if __name__ == "__main__":
    jpeg_output_directory = "/Users/abasaltbahrami/Downloads/Receipts/jpeg_images"
    output_directory_compressed = "/Users/abasaltbahrami/Downloads/Receipts/compressed_images"
    compression_quality = 30  # Adjust the compression quality (0-100)

    compress_images(jpeg_output_directory,
                    output_directory_compressed, compression_quality)
