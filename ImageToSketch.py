import cv2


def convert_to_sketch(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Invert the grayscale image
    inverted_image = cv2.bitwise_not(gray_image)

    # Apply Gaussian blur to the inverted image
    blurred_image = cv2.GaussianBlur(inverted_image, (21, 21), 0)

    # Blend the grayscale image with the blurred image using the "color dodge" blending mode
    sketch_image = cv2.divide(gray_image, blurred_image, scale=256.0)

    # Display the original image and the sketch image
    cv2.imshow("Original Image", image)
    cv2.imshow("Sketch Image", sketch_image)

    # Wait for a key press and then close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Path to the image you want to convert to a sketch
image_path = "/Users/abasaltbahrami/Downloads/QuBiT/QuBiT.jpg"

# Call the function to convert the image to a sketch
convert_to_sketch(image_path)
