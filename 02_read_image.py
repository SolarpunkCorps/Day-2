# Read and display an image with OpenCV.
# This script loads a local image file and shows it in a window.

import cv2

# Read the image from the working directory.
image = cv2.imread("pic1.jpg")

# Display the image and wait for the user to close it.
cv2.imshow("My Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()