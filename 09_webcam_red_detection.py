# Detect red objects from a live webcam feed.
# The script converts each video frame to HSV, filters red tones,
# finds contours, and draws bounding boxes around detected red objects.

import cv2
import numpy as np

# Open the default webcam.
camera = cv2.VideoCapture(0)

while True:

    # Read the next frame from the camera.
    ret, frame = camera.read()

    if not ret:
        print("Could not access camera")
        break

    # Flip the image horizontally for a mirror effect.
    frame = cv2.flip(frame, 1)

    # Convert BGR frame to HSV for easier color thresholding.
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define two red ranges to cover the full red hue spectrum.
    lower_red1 = np.array([0, 80, 50])
    upper_red1 = np.array([10, 255, 255])

    lower_red2 = np.array([170, 80, 50])
    upper_red2 = np.array([179, 255, 255])

    # Create masks for both red ranges and combine them.
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = mask1 | mask2

    # Find contours in the red mask.
    contours, _ = cv2.findContours(
        mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    # Draw boxes and labels around visible red objects.
    for contour in contours:

        area = cv2.contourArea(contour)

        if area > 500:

            x, y, w, h = cv2.boundingRect(contour)

            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

            cv2.putText(
                frame,
                "RED",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2
            )

    # Display the processed camera feed and red mask.
    cv2.imshow("Camera", frame)
    cv2.imshow("Red Mask", mask)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()