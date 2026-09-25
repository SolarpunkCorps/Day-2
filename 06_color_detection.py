# Detect a red object using a color mask.
# This script converts the image to HSV and filters only the red pixels.

import cv2
import numpy as np

# Load the image to process.
image = cv2.imread("pic1.jpg")

# Convert from BGR color space to HSV, which is easier for color filtering.
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define the lower and upper bounds for red in HSV.
lower_red = np.array([0, 120, 70])
upper_red = np.array([10, 255, 255])

# Create a mask that contains only pixels within the red range.
mask = cv2.inRange(
    hsv,
    lower_red,
    upper_red
)

# Display the original image and the red mask.
cv2.imshow("Original", image)
cv2.imshow("Red Mask", mask)

cv2.waitKey(0)
cv2.destroyAllWindows()