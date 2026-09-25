# 11_object_distance_estimation.py

from ultralytics import YOLO
import cv2

# Load YOLO model
model = YOLO("yolo11n.pt")

# Open webcam
camera = cv2.VideoCapture(0)

# Real width of your phone in cm
KNOWN_WIDTH = 7.5

# Camera focal length
# Calibrate this value for your camera
FOCAL_LENGTH = 700


while True:

    ret, frame = camera.read()

    if not ret:
        print("Could not access camera")
        break

    # Flip image horizontally
    frame = cv2.flip(frame, 1)

    # Run YOLO
    results = model(frame)

    # Original frame
    annotated_frame = frame.copy()

    boxes = results[0].boxes

    if boxes is not None:

        for box in boxes:

            # Get detected class
            class_id = int(box.cls[0])
            class_name = model.names[class_id]

            # Only detect cell phone
            if class_name != "cell phone":
                continue

            # Get bounding box coordinates
            x1, y1, x2, y2 = box.xyxy[0].tolist()

            x1 = int(x1)
            y1 = int(y1)
            x2 = int(x2)
            y2 = int(y2)

            # Calculate phone width in pixels
            pixel_width = x2 - x1

            if pixel_width <= 0:
                continue

            # Estimate distance
            distance = (
                KNOWN_WIDTH * FOCAL_LENGTH
            ) / pixel_width

            # Draw phone bounding box
            cv2.rectangle(
                annotated_frame,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                2
            )

            # Display phone label
            cv2.putText(
                annotated_frame,
                "Phone",
                (x1, y1 - 35),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2
            )

            # Display distance
            cv2.putText(
                annotated_frame,
                f"Distance: {distance:.1f} cm",
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2
            )

    # Show result
    cv2.imshow(
        "Phone Distance Estimation",
        annotated_frame
    )

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


camera.release()
cv2.destroyAllWindows()