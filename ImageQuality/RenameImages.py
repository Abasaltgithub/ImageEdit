import os


def rename_photos(folder_path, new_name="A7R5_20x_0.30"):
    try:
        # Get a list of all files in the folder
        file_list = os.listdir(folder_path)

        # Keep track of the count for numbering the images
        count = 1

        # Process each file in the list
        for file_name in file_list:
            # Check if the file has the ".bmp" extension
            if file_name.lower().endswith(".bmp"):
                # Get the current file's full path
                old_path = os.path.join(folder_path, file_name)

                # Create the new file name with the specified format and number
                new_file_name = f"{new_name}_{count:03d}.bmp"

                # Get the new file's full path
                new_path = os.path.join(folder_path, new_file_name)

                # Rename the file
                os.rename(old_path, new_path)

                print(f"Renamed '{file_name}' to '{new_file_name}'")

                # Increment the count for the next image
                count += 1
    except Exception as e:
        print(f"Error renaming files: {e}")


if __name__ == "__main__":
    folder_path = "/Users/abasaltbahrami/My Drive/Microscope_InCor/A7R5_20x_0.30"

    # Call the function to rename BMP images in the folder
    rename_photos(folder_path)
