# Image thresholding example.
# This script converts the image to grayscale and then applies a binary threshold.
# Thresholding helps separate objects from the background in image processing.

import cv2

# Read and prepare the image.
image = cv2.imread("pic1.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply a binary threshold: pixels above 120 become white, others become black.
_, threshold = cv2.threshold(
    gray,
    120,
    255,
    cv2.THRESH_BINARY
)

# Display the grayscale and thresholded images.
cv2.imshow("Grayscale", gray)
cv2.imshow("Threshold", threshold)

cv2.waitKey(0)
cv2.destroyAllWindows()