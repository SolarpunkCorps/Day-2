# Detect and label a red object in an image.
# This script finds red regions, draws a bounding box around each large one,
# and adds a label to the image.

import cv2
import numpy as np

# Read the image.
image = cv2.imread("pic1.jpg")

# Convert the image to HSV for color-based filtering.
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define the red detection range.
lower_red = np.array([0, 120, 70])
upper_red = np.array([10, 255, 255])

# Create a mask for the red area.
mask = cv2.inRange(
    hsv,
    lower_red,
    upper_red
)

# Find contours of the detected red regions.
contours, _ = cv2.findContours(
    mask,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

# Draw a rectangle around each contour that is large enough to be relevant.
for contour in contours:

    area = cv2.contourArea(contour)

    if area > 500:

        x, y, w, h = cv2.boundingRect(contour)

        cv2.rectangle(
            image,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

        cv2.putText(
            image,
            "Red Object",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

# Show the final labeled image.
cv2.imshow("Object Detection", image)

cv2.waitKey(0)
cv2.destroyAllWindows()