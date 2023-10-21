import os
import subprocess


def convert_and_rename(source_folder, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for filename in os.listdir(source_folder):
        if filename.lower().endswith('.heic'):
            heic_path = os.path.join(source_folder, filename)
            jpeg_path = os.path.join(
                destination_folder, os.path.splitext(filename)[0] + '.jpg')

            # Convert HEIC to JPEG using heif-convert command-line tool
            subprocess.run(["heif-convert", heic_path, jpeg_path])

            # Remove the original HEIC file
            os.remove(heic_path)


if __name__ == "__main__":
    heic_input_directory = "/Users/abasaltbahrami/Downloads/HEIC"
    jpeg_output_directory = "/Users/abasaltbahrami/Downloads/HEIC"

    convert_and_rename(heic_input_directory, jpeg_output_directory)
    print("Conversion and renaming complete.")
