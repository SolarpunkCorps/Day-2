# Real-time object detection using YOLO.
# This script loads a pretrained YOLO model and processes frames from the webcam.

from ultralytics import YOLO
import cv2

# Load a pretrained YOLO model from the local weights file.
model = YOLO("yolo11n.pt")

# Open the default webcam.
camera = cv2.VideoCapture(0)

while True:

    # Capture the next frame.
    ret, frame = camera.read()

    if not ret:
        print("Could not access camera")
        break

    # Flip the image horizontally for a mirror view.
    frame = cv2.flip(frame, 1)

    # Run object detection on the current frame.
    results = model(frame)

    # Draw bounding boxes and labels on the frame.
    annotated_frame = results[0].plot()

    # Show the annotated result.
    cv2.imshow("Object Detection", annotated_frame)

    # Press Q to exit the webcam loop.
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()