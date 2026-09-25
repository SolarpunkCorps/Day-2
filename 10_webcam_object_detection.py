from ultralytics import YOLO
import cv2

# Load a pretrained YOLO model
model = YOLO("yolo11n.pt")

# Open webcam
camera = cv2.VideoCapture(0)

while True:

    ret, frame = camera.read()

    if not ret:
        print("Could not access camera")
        break

    # Flip the image horizontally
    frame = cv2.flip(frame, 1)

    # Run object detection
    results = model(frame)

    # Draw detected objects on the frame
    annotated_frame = results[0].plot()

    # Show result
    cv2.imshow("Object Detection", annotated_frame)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()