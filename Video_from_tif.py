import os
import cv2
from PIL import Image
import numpy as np


def is_black_frame(frame, threshold=10):
    # Compute the mean pixel value of the frame
    mean_value = np.mean(frame)
    # Check if the mean pixel value is below the threshold
    return mean_value < threshold


def create_video_from_images(image_folder, output_video_path, video_fps=10):
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.tif')]
    image_files.sort()

    if len(image_files) == 0:
        raise ValueError("No .tif images found in the provided folder.")

    first_image = Image.open(os.path.join(image_folder, image_files[0]))
    width, height = first_image.size

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter(
        output_video_path, fourcc, video_fps, (width, height))

    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)
        frame = np.array(Image.open(image_path))

        # Check if the frame is a black frame
        if is_black_frame(frame):
            continue  # Skip black frames

        video_writer.write(frame)

    video_writer.release()


if __name__ == "__main__":
    image_folder_path = "/Users/abasaltbahrami/My Drive/Company/My research/Colding/B0"
    output_video_path = "/Users/abasaltbahrami/My Drive/Company/My research/Colding/Videos/video_output.mp4"
    create_video_from_images(image_folder_path, output_video_path)
