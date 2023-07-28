import cv2

# Load the image
img = cv2.imread(
    '/Users/abasaltbahrami/Library/CloudStorage/Dropbox/Screenshots/signature.png')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply a threshold to the image to remove noise
_, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

# Apply a median filter to the image to smooth out any rough edges
median = cv2.medianBlur(thresh, 1)

# Apply erosion and dilation to further remove noise and smooth out the signature
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1))
erode = cv2.erode(median, kernel, iterations=1)
dilate = cv2.dilate(erode, kernel, iterations=1)

# Save the processed image
cv2.imwrite(
    '/Users/abasaltbahrami/Downloads/processed_signature.jpg', dilate)
