import cv2
import numpy as np

image = cv2.imread("pic1.jpg")

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_red = np.array([0, 120, 70])
upper_red = np.array([10, 255, 255])

mask = cv2.inRange(
    hsv,
    lower_red,
    upper_red
)

cv2.imshow("Original", image)
cv2.imshow("Red Mask", mask)

cv2.waitKey(0)
cv2.destroyAllWindows()