import os
import cv2
from datetime import datetime


def create_video_from_tiff(folder_path, output_folder, fps=1):
    # Get a list of all TIFF files in the folder
    tiff_files = [file for file in os.listdir(
        folder_path) if file.endswith(".tif")]
    if not tiff_files:
        raise ValueError("No TIFF files found in the specified folder.")

    # Sort the files alphabetically to maintain the order in the video
    tiff_files.sort()

    # Read the first TIFF image to get its dimensions
    first_tiff = cv2.imread(os.path.join(folder_path, tiff_files[0]))
    height, width, _ = first_tiff.shape

    # Define the video writer
    fourcc = cv2.VideoWriter_fourcc(*'avc1')  # Specify H.264 codec

    # Generate a unique filename with date and time stamp
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_video_filename = f"video_{timestamp}.mp4"
    output_video_path = os.path.join(output_folder, output_video_filename)

    video_writer = cv2.VideoWriter(
        output_video_path, fourcc, fps, (width, height))

    # Iterate through TIFF images and write them to the video
    for tiff_file in tiff_files:
        image_path = os.path.join(folder_path, tiff_file)
        image = cv2.imread(image_path)

        # Ensure all images have the same dimensions as the first image
        if image.shape != first_tiff.shape:
            raise ValueError(
                "All TIFF images should have the same dimensions.")

        video_writer.write(image)

    # Release the video writer and close the video file
    video_writer.release()


if __name__ == "__main__":
    folder_path = "/Users/abasaltbahrami/My Drive/Company/My research/Colding/B0"
    output_folder = "/Users/abasaltbahrami/My Drive/Company/My research/Colding/Videos"
    create_video_from_tiff(folder_path, output_folder, fps=1)
    print("Video created successfully.")
