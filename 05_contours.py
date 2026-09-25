import cv2

image = cv2.imread("pic1.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, threshold = cv2.threshold(
    gray,
    120,
    255,
    cv2.THRESH_BINARY
)

contours, hierarchy = cv2.findContours(
    threshold,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

print("Number of contours:", len(contours))

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

cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

cv2.imshow("Contours", image)

cv2.waitKey(0)
cv2.destroyAllWindows()