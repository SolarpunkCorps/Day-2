# Open and display a webcam feed.
# This script captures live video from the default camera and shows it in a window.

import cv2

# Open the default webcam.
camera = cv2.VideoCapture(0)

while True:

    # Read each frame from the webcam.
    ret, frame = camera.read()

    if not ret:
        print("Could not access camera")
        break

    # Flip the image horizontally for a mirror effect.
    frame = cv2.flip(frame, 1)

    # Display the video frame.
    cv2.imshow("Webcam", frame)

    # Press q to stop the video stream.
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()