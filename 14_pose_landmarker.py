# 14_pose_landmarker.py

import cv2
import mediapipe as mp
import os


# ============================================================
# MediaPipe Tasks
# ============================================================

BaseOptions = mp.tasks.BaseOptions
PoseLandmarker = mp.tasks.vision.PoseLandmarker
PoseLandmarkerOptions = mp.tasks.vision.PoseLandmarkerOptions
RunningMode = mp.tasks.vision.RunningMode


# ============================================================
# Find model relative to THIS Python file
# ============================================================

model_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "models",
    "pose_landmarker.task"
)

print("Model path:", model_path)

if not os.path.exists(model_path):
    print("ERROR: pose_landmarker.task not found!")
    print("Expected location:")
    print(model_path)
    exit()

print("Model found!")


# ============================================================
# Create Pose Landmarker
# ============================================================

options = PoseLandmarkerOptions(
    base_options=BaseOptions(
        model_asset_path=model_path
    ),
    running_mode=RunningMode.VIDEO,
    num_poses=1,
    min_pose_detection_confidence=0.5,
    min_pose_presence_confidence=0.5,
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
# Pose connections
# ============================================================

connections = [
    # Face
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 7),
    (0, 4),
    (4, 5),
    (5, 6),
    (6, 8),

    # Torso
    (11, 12),
    (11, 23),
    (12, 24),
    (23, 24),

    # Left arm
    (11, 13),
    (13, 15),
    (15, 17),
    (15, 19),
    (15, 21),

    # Right arm
    (12, 14),
    (14, 16),
    (16, 18),
    (16, 20),
    (16, 22),

    # Left leg
    (23, 25),
    (25, 27),
    (27, 29),
    (27, 31),

    # Right leg
    (24, 26),
    (26, 28),
    (28, 30),
    (28, 32)
]


# ============================================================
# Create Pose Landmarker
# ============================================================

with PoseLandmarker.create_from_options(options) as landmarker:

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
        # Detect pose
        # ----------------------------------------------------

        results = landmarker.detect_for_video(
            mp_image,
            frame_timestamp
        )


        # ====================================================
        # Draw pose
        # ====================================================

        if results.pose_landmarks:

            for pose_landmarks in results.pose_landmarks:

                # ------------------------------------------------
                # Draw landmarks
                # ------------------------------------------------

                for landmark in pose_landmarks:

                    x = int(
                        landmark.x * frame.shape[1]
                    )

                    y = int(
                        landmark.y * frame.shape[0]
                    )

                    # Only draw landmarks inside frame
                    if (
                        0 <= x < frame.shape[1]
                        and 0 <= y < frame.shape[0]
                    ):

                        cv2.circle(
                            frame,
                            (x, y),
                            5,
                            (0, 255, 0),
                            -1
                        )


                # ------------------------------------------------
                # Draw connections
                # ------------------------------------------------

                for start, end in connections:

                    x1 = int(
                        pose_landmarks[start].x
                        * frame.shape[1]
                    )

                    y1 = int(
                        pose_landmarks[start].y
                        * frame.shape[0]
                    )

                    x2 = int(
                        pose_landmarks[end].x
                        * frame.shape[1]
                    )

                    y2 = int(
                        pose_landmarks[end].y
                        * frame.shape[0]
                    )

                    cv2.line(
                        frame,
                        (x1, y1),
                        (x2, y2),
                        (0, 255, 0),
                        2
                    )


        # ====================================================
        # Show result
        # ====================================================

        cv2.imshow(
            "MediaPipe Pose Landmarker",
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