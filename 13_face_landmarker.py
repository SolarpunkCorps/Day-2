# 13_face_landmarker.py

import cv2
import mediapipe as mp
import os


# ============================================================
# MediaPipe Tasks
# ============================================================

BaseOptions = mp.tasks.BaseOptions
FaceLandmarker = mp.tasks.vision.FaceLandmarker
FaceLandmarkerOptions = mp.tasks.vision.FaceLandmarkerOptions
RunningMode = mp.tasks.vision.RunningMode


# ============================================================
# Find model relative to THIS Python file
# ============================================================

model_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "models",
    "face_landmarker.task"
)

print("Model path:", model_path)

if not os.path.exists(model_path):
    print("ERROR: face_landmarker.task not found!")
    print("Expected location:")
    print(model_path)
    exit()

print("Model found!")


# ============================================================
# Create Face Landmarker
# ============================================================

options = FaceLandmarkerOptions(
    base_options=BaseOptions(
        model_asset_path=model_path
    ),
    running_mode=RunningMode.VIDEO,
    num_faces=1,
    min_face_detection_confidence=0.5,
    min_face_presence_confidence=0.5,
    min_tracking_confidence=0.5
)


# ============================================================
# Open webcam
# ============================================================

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Could not access camera")
    exit()


# ============================================================
# Create Face Landmarker
# ============================================================

with FaceLandmarker.create_from_options(options) as landmarker:

    frame_timestamp = 0

    while True:

        # ----------------------------------------------------
        # Read webcam frame
        # ----------------------------------------------------

        ret, frame = camera.read()

        if not ret:
            print("Could not read camera frame")
            break


        # ----------------------------------------------------
        # Flip image horizontally
        # ----------------------------------------------------

        frame = cv2.flip(frame, 1)


        # ----------------------------------------------------
        # Convert BGR → RGB
        # ----------------------------------------------------

        rgb_frame = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )


        # ----------------------------------------------------
        # Convert to MediaPipe Image
        # ----------------------------------------------------

        mp_image = mp.Image(
            image_format=mp.ImageFormat.SRGB,
            data=rgb_frame
        )


        # ----------------------------------------------------
        # Increase timestamp
        # ----------------------------------------------------

        frame_timestamp += 1


        # ----------------------------------------------------
        # Detect face
        # ----------------------------------------------------

        results = landmarker.detect_for_video(
            mp_image,
            frame_timestamp
        )


        # ====================================================
        # Draw face landmarks
        # ====================================================

        if results.face_landmarks:

            for face_landmarks in results.face_landmarks:

                for landmark in face_landmarks:

                    x = int(
                        landmark.x * frame.shape[1]
                    )

                    y = int(
                        landmark.y * frame.shape[0]
                    )

                    cv2.circle(
                        frame,
                        (x, y),
                        1,
                        (0, 255, 0),
                        -1
                    )


        # ====================================================
        # Show result
        # ====================================================

        cv2.imshow(
            "MediaPipe Face Landmarker",
            frame
        )


        # ----------------------------------------------------
        # Press Q to quit
        # ----------------------------------------------------

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break


# ============================================================
# Release resources
# ============================================================

camera.release()
cv2.destroyAllWindows()