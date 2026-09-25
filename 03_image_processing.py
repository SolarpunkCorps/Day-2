# Convert an image to grayscale.
# This script loads an image, converts it from BGR to grayscale,
# and displays both versions side by side in separate windows.

import cv2

# Load the image.
image = cv2.imread("pic1.jpg")

# Convert the color image to grayscale for simpler processing.
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Show the original and processed versions.
cv2.imshow("Original", image)
cv2.imshow("Grayscale", gray)

cv2.waitKey(0)
cv2.destroyAllWindows()