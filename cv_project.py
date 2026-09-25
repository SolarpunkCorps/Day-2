# Shape detection and counting project.
# This script reads an image, detects contours, counts objects,
# draws bounding boxes, and identifies the shape of each object.

import cv2

# Step 1: Read the input image.
image = cv2.imread("shapes.jpeg")

# Step 2: Convert the image to grayscale.
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Step 3: Apply a simple binary threshold to separate object regions.
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Step 4: Find contours in the thresholded image.
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

output = image.copy()

# Step 5: Draw all detected contours on the output image.
cv2.drawContours(output, contours, -1, (0, 255, 0), 2)

# Step 6: Count the number of detected objects and display it.
cv2.putText(output, f"Objects: {len(contours)}", (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

# Step 7 & 8: Draw bounding boxes and estimate each shape.
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(output, (x, y), (x + w, y + h), (255, 0, 0), 2)

    approx = cv2.approxPolyDP(cnt, 0.02 * cv2.arcLength(cnt, True), True)
    corners = len(approx)

    if corners == 3:
        shape_name = "Triangle"
    elif corners == 4:
        shape_name = "Rectangle/Square"
    elif corners > 4:
        shape_name = "Circle"
    else:
        shape_name = "Unknown"

    cv2.putText(output, shape_name, (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

# Display the final annotated output.
cv2.imshow("Final Output", output)
cv2.waitKey(0)
cv2.destroyAllWindows()