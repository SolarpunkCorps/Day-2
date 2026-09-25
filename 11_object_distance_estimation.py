# 11_object_distance_estimation.py

from ultralytics import YOLO
import cv2

# Load YOLO model
model = YOLO("yolo11n.pt")

# Open webcam
camera = cv2.VideoCapture(0)

# ------------------------------------------------
# MEASURE YOUR OBJECT
# ------------------------------------------------

# Measure the real width of the object in cm.
# Example: if your phone is 7.5 cm wide:
KNOWN_WIDTH = 7.5

# ------------------------------------------------
# CAMERA CALIBRATION
# ------------------------------------------------

# Put the object at a known distance from camera.
# Example:
# Object = 50 cm away
# Measure its pixel width on the screen.
#
# Focal length = Pixel Width × Known Distance / Real Width
#
# You need to determine this value for your camera.

FOCAL_LENGTH = 700


while True:

    ret, frame = camera.read()

    if not ret:
        print("Could not access camera")
        break

    # Mirror image
    frame = cv2.flip(frame, 1)

    # Run YOLO
    results = model(frame)

    # Draw detections
    annotated_frame = results[0].plot()

    boxes = results[0].boxes

    if boxes is not None:

        for box in boxes:

            # Get class
            class_id = int(box.cls[0])
            class_name = model.names[class_id]

            # Detect only cell phones
            if class_name != "cell phone":
                continue

            # Bounding box
            x1, y1, x2, y2 = box.xyxy[0].tolist()

            x1 = int(x1)
            y1 = int(y1)
            x2 = int(x2)
            y2 = int(y2)

            # Width of object in pixels
            pixel_width = x2 - x1

            if pixel_width <= 0:
                continue

            # Distance estimation
            distance = (
                KNOWN_WIDTH * FOCAL_LENGTH
            ) / pixel_width

            # Display distance
            cv2.putText(
                annotated_frame,
                f"Distance: {distance:.1f} cm",
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2
            )

    # Show result
    cv2.imshow(
        "Object Distance",
        annotated_frame
    )

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


camera.release()
cv2.destroyAllWindows()