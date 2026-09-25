# 12_hand_tracking.py

import cv2
import mediapipe as mp

# MediaPipe Tasks
BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
RunningMode = mp.tasks.vision.RunningMode


# Create Hand Landmarker
options = HandLandmarkerOptions(
    base_options=BaseOptions(
        model_asset_path="models/hand_landmarker.task"
    ),
    running_mode=RunningMode.VIDEO,
    num_hands=2,
    min_hand_detection_confidence=0.5,
    min_hand_presence_confidence=0.5,
    min_tracking_confidence=0.5
)


# Open webcam
camera = cv2.VideoCapture(0)


# Create Hand Landmarker
with HandLandmarker.create_from_options(options) as landmarker:

    frame_timestamp = 0

    while True:

        # Read webcam frame
        ret, frame = camera.read()

        if not ret:
            print("Could not access camera")
            break

        # Flip image horizontally
        frame = cv2.flip(frame, 1)

        # Convert BGR → RGB
        rgb_frame = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )

        # Convert to MediaPipe Image
        mp_image = mp.Image(
            image_format=mp.ImageFormat.SRGB,
            data=rgb_frame
        )

        # Increase timestamp
        frame_timestamp += 1

        # Detect hands
        results = landmarker.detect_for_video(
            mp_image,
            frame_timestamp
        )


        # Draw detected hands
        if results.hand_landmarks:

            for hand_landmarks in results.hand_landmarks:

                # Draw 21 landmarks
                for landmark in hand_landmarks:

                    x = int(
                        landmark.x * frame.shape[1]
                    )

                    y = int(
                        landmark.y * frame.shape[0]
                    )

                    cv2.circle(
                        frame,
                        (x, y),
                        5,
                        (0, 255, 0),
                        -1
                    )


                # Hand connections
                connections = [
                    (0, 1),
                    (1, 2),
                    (2, 3),
                    (3, 4),

                    (0, 5),
                    (5, 6),
                    (6, 7),
                    (7, 8),

                    (5, 9),
                    (9, 10),
                    (10, 11),
                    (11, 12),

                    (9, 13),
                    (13, 14),
                    (14, 15),
                    (15, 16),

                    (13, 17),
                    (17, 18),
                    (18, 19),
                    (19, 20),

                    (0, 17)
                ]


                # Draw connections
                for start, end in connections:

                    x1 = int(
                        hand_landmarks[start].x
                        * frame.shape[1]
                    )

                    y1 = int(
                        hand_landmarks[start].y
                        * frame.shape[0]
                    )

                    x2 = int(
                        hand_landmarks[end].x
                        * frame.shape[1]
                    )

                    y2 = int(
                        hand_landmarks[end].y
                        * frame.shape[0]
                    )

                    cv2.line(
                        frame,
                        (x1, y1),
                        (x2, y2),
                        (0, 255, 0),
                        2
                    )


        # Show result
        cv2.imshow(
            "MediaPipe Hand Tracking",
            frame
        )


        # Press Q to quit
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break


# Release resources
camera.release()
cv2.destroyAllWindows()