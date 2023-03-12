import cv2
import os

# set path to input and output directories
input_dir = "/Users/abasaltbahrami/Downloads/reserach/"
output_dir = "/Users/abasaltbahrami/Downloads/reserach/edited/"

# list of allowed file extensions
allowed_extensions = ['.jpg', '.png', '.HEC', '.jpeg', '.webp']

# get list of file names in input directory
file_names = os.listdir(input_dir)

# loop over all files in input directory
for file_name in file_names:
    # check if the file has an allowed extension
    if any(file_name.endswith(ext) for ext in allowed_extensions):
        # read image from input directory
        input_path = os.path.join(input_dir, file_name)
        img = cv2.imread(input_path)

        # resize image to size 600x300
        resized_img = cv2.resize(img, (600, 300))

        # add name of the image to the top left corner in white color
        name = os.path.splitext(file_name)[0].upper()  # convert to uppercase
        cv2.putText(resized_img, name, (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        # write resized image to output directory with png format
        output_path = os.path.join(
            output_dir, os.path.splitext(file_name)[0] + '.png')
        cv2.imwrite(output_path, resized_img)
