# Day 2 — Make the Machine See

<div align="left">

[![Python](https://img.shields.io/badge/Python-3.13.0-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-5.0.0-5C3EE8?logo=opencv&logoColor=white)](https://opencv.org/)
[![NumPy](https://img.shields.io/badge/NumPy-2.1.3-013243?logo=numpy&logoColor=white)](https://numpy.org/)
[![Ultralytics](https://img.shields.io/badge/Ultralytics-8.4.162-00A4EF?logo=ultralytics&logoColor=white)](https://ultralytics.com/)
[![MediaPipe](https://img.shields.io/badge/MediaPipe-1.0.1-00BFA5?logo=google&logoColor=white)](https://mediapipe.dev/)
[![Platform](https://img.shields.io/badge/Platform-Windows_11-0078D6?logo=windows&logoColor=white)](https://www.microsoft.com/windows/)
[![IDE](https://img.shields.io/badge/IDE-VS_Code-007ACC?logo=visualstudiocode&logoColor=white)](https://code.visualstudio.com/)

</div>

This project is built and tested with Python 3.13.0 and the libraries used in this workshop: OpenCV 5.0.0, NumPy 2.1.3, Ultralytics 8.4.162, and MediaPipe 1.0.1. This README explains each Python file in the order it is used, including why the file exists, what its important components do, and what concept it teaches.

## 0. Setup — Before Running the Files

Open the Day 2 folder in VS Code and open **Terminal → New Terminal**.

Check Python:

```bash
python --version
```

Install the libraries for the OpenCV exercises:

```bash
pip install opencv-python numpy
```

Verify OpenCV:

```bash
python -c "import cv2; print(cv2.__version__)"
```

Before `10_yolo_object_detection.py`, install Ultralytics:

```bash
pip install ultralytics
```

Before `12_hand_tracking.py`, install MediaPipe:

```bash
pip install mediapipe
```

Useful commands:

```bash
python filename.py
```

```bash
python 01_test.py
python 08_webcam.py
python 09_webcam_red_detection.py
python 10_yolo_object_detection.py
```

Check NumPy:

```bash
python -c "import numpy; print(numpy.__version__)"
```

Check Ultralytics:

```bash
python -c "import ultralytics; print(ultralytics.__version__)"
```

---

# `01_test.py`

**Purpose:** Check that OpenCV is installed and working.

**Why:** Before working with images or cameras, verify that Python can import OpenCV successfully.

**What it does:**
- Imports OpenCV.
- Prints the installed OpenCV version.
- Confirms that OpenCV is working.

**Key components:**

`import cv2` — imports OpenCV.

`cv2.__version__` — returns the installed OpenCV version.

**Main concept:** Python → OpenCV → Working environment.

---

# `02_read_image.py`

**Purpose:** Read and display `pic1.jpg`.

**Why:** Before processing images, we need to know how to load and display them.

**What it does:**
- Reads `pic1.jpg`.
- Displays it.
- Waits for a key.
- Closes the window.

**Key components:**

`cv2.imread()` — reads an image from a file.

`cv2.imshow()` — displays the image.

`cv2.waitKey()` — keeps the window open while waiting for keyboard input.

`cv2.destroyAllWindows()` — closes OpenCV windows.

**Main concept:** Image file → OpenCV → Image.

---

# `03_image_processing.py`

**Purpose:** Introduce basic image processing.

**Why:** Images can be transformed into forms that are more useful for later analysis.

**What it does:**
- Reads the image.
- Resizes it.
- Displays the original and resized images.
- Converts the image from BGR to grayscale.

**Key components:**

`cv2.resize()` — changes image dimensions.

`cv2.cvtColor()` — converts between colour spaces.

`cv2.COLOR_BGR2GRAY` — converts BGR into grayscale.

**Why grayscale:** A colour image has Blue, Green and Red channels. Grayscale represents brightness using one channel, typically from 0 (black) to 255 (white). This simplifies many later operations.

**Main concept:** Original image → Processing → New representation.

---

# `04_thresholding.py`

**Purpose:** Convert a grayscale image into a binary image.

**Why:** Separating pixels into black and white regions can make objects or regions easier to analyse.

**What it does:**
- Reads the image.
- Converts it to grayscale.
- Applies a threshold.
- Displays the grayscale and binary images.

**Key components:**

`cv2.threshold()` — compares pixel intensity with a selected threshold.

`cv2.THRESH_BINARY` — creates a binary result.

Pixels on one side of the threshold become black and pixels on the other side become white.

**Why:** A simplified image can make the next step, contour detection, easier.

**Limitation:** Results depend on lighting, contrast and the chosen threshold.

**Main concept:** Grayscale → Threshold → Binary image.

---

# `05_contours.py`

**Purpose:** Find boundaries of regions in a thresholded image.

**Why:** Once an image contains separated regions, contours allow us to identify their boundaries and analyse their size.

**What it does:**
- Reads and converts the image to grayscale.
- Thresholds the image.
- Finds contours.
- Counts them.
- Calculates their areas.
- Draws them.

**Key components:**

`cv2.findContours()` — finds boundaries of connected regions.

`cv2.RETR_EXTERNAL` — retrieves outermost contours.

`cv2.CHAIN_APPROX_SIMPLE` — reduces unnecessary contour points.

`cv2.contourArea()` — calculates the area enclosed by a contour.

`cv2.drawContours()` — draws contours for visualisation.

**Main concept:** Binary image → Contours → Detected regions.

---

# `06_color_detection.py`

**Purpose:** Detect a selected colour using HSV.

**Why:** Instead of relying only on brightness, we can use colour information to locate a specific colour.

**What it does:**
- Reads the image.
- Converts BGR to HSV.
- Defines a lower and upper HSV range for red.
- Creates a mask.
- Displays the original image and mask.

**Key components:**

`cv2.cvtColor()` — converts BGR to HSV.

`cv2.COLOR_BGR2HSV` — specifies that conversion.

`np.array()` — stores numerical HSV limits.

`cv2.inRange()` — selects pixels inside the specified HSV range.

**HSV:**
- H = Hue
- S = Saturation
- V = Value

**Mask:** White pixels match the selected range; black pixels do not.

**Why HSV:** It separates colour information from brightness more conveniently for many colour-detection tasks.

**Limitation:** HSV values depend on lighting, shadows, camera settings and the exact object colour.

**Main concept:** Image → HSV → Colour range → Mask.

---

# `07_red_object_detection.py`

**Purpose:** Detect a red region and draw a bounding box around it.

**Why:** This combines colour detection and contours to create a simple classical computer-vision detector.

**What it does:**
- Converts the image to HSV.
- Creates a red mask.
- Finds contours.
- Measures contour areas.
- Ignores very small regions.
- Creates a bounding rectangle.
- Draws the rectangle and label.

**Key components:**

`cv2.inRange()` — creates the red mask.

`cv2.findContours()` — finds red regions.

`cv2.contourArea()` — measures each region.

`cv2.boundingRect()` — calculates x, y, width and height of the bounding box.

`cv2.rectangle()` — draws the box.

`cv2.putText()` — adds the label.

**Why the area filter:** Small unwanted regions or noise should not automatically be treated as objects.

**Main concept:** Colour detection + contours + bounding box = simple classical object detection.

The program does not understand that something is a “phone” or “person.” It is identifying a region because its pixels satisfy the selected colour rules.

---

# `08_webcam.py`

**Purpose:** Read and display a live webcam feed.

**Why:** A robot normally receives a continuous stream of camera frames rather than one static photograph.

**What it does:**
- Opens the default camera.
- Captures frames continuously.
- Checks whether capture succeeded.
- Displays each frame.
- Stops when `q` is pressed.
- Releases the camera.

**Key components:**

`cv2.VideoCapture(0)` — opens the default camera.

`camera.read()` — captures the next frame.

`while True` — continuously processes frames.

`cv2.imshow()` — displays the current frame.

`cv2.waitKey(1)` — allows the display to update and checks keyboard input.

`camera.release()` — releases the camera.

`cv2.destroyAllWindows()` — closes OpenCV windows.

**Main concept:** Camera → Frame → Display → Next frame → Repeat.

---

# `09_webcam_red_detection.py`

**Purpose:** Detect red objects from a live webcam.

**Why:** This combines the earlier colour-detection concepts with real-time camera input.

**What it does:**
- Opens the webcam.
- Captures frames.
- Horizontally flips the frame.
- Converts BGR to HSV.
- Creates two red masks.
- Combines them.
- Finds contours.
- Filters small regions.
- Draws bounding boxes.
- Adds the `RED` label.
- Displays the camera and mask.

**Key components:**

`cv2.flip(frame, 1)` — horizontally flips the frame, useful when the webcam appears mirrored.

Two red HSV ranges are used because red occurs at both ends of OpenCV's HSV hue scale.

`cv2.inRange()` — creates each mask.

`mask1 | mask2` — combines both red masks.

`cv2.findContours()` — finds connected red regions.

`cv2.contourArea()` — filters small regions.

`cv2.boundingRect()` — finds the bounding box.

`cv2.rectangle()` — draws it.

`cv2.putText()` — labels it.

`cv2.imshow()` — displays the camera and mask.

**Why display the mask:** It shows what the detector actually considers red. If a red shirt is not detected, the mask helps determine whether the HSV range needs adjustment.

**Main concept:**

**Camera → Frame → HSV → Red Mask → Contours → Bounding Box → Detection**

---

# `10_yolo_object_detection.py`

**Purpose:** Detect common objects such as people, phones, bottles, chairs, laptops, cars and other supported categories using a pretrained YOLO model.

**Why:** The previous detector identifies objects using manually selected colour rules. YOLO uses a pretrained neural network that has learned visual patterns associated with object categories.

**Required installation:**

```bash
pip install ultralytics
```

**What it does:**
- Loads a pretrained YOLO model.
- Opens the webcam.
- Captures frames.
- Flips the frame horizontally.
- Sends each frame to YOLO.
- Receives detections.
- Draws bounding boxes, class names and confidence values.
- Displays the annotated frame.
- Stops when `q` is pressed.

**Key components:**

`from ultralytics import YOLO` — imports the YOLO interface.

`YOLO(...)` — loads the pretrained model.

`cv2.VideoCapture(0)` — opens the webcam.

`camera.read()` — captures frames.

`cv2.flip(frame, 1)` — horizontally flips the frame.

`model(frame)` — sends the frame through the YOLO model.

`results[0].plot()` — creates an annotated image showing detections.

**What a YOLO detection provides:**

**Class** — what the model believes the object is.

**Bounding box** — where the object is located.

**Confidence** — numerical confidence associated with the detection.

**Why this is different from the red detector:**

Classical detector:

**Image → Colour rule → Mask → Contour → Bounding box**

YOLO:

**Image → Neural network → Object class + Confidence + Bounding box**

**Important limitation:** A pretrained model cannot automatically detect every object in existence. It can detect the categories included in the model's training data.

General object detection and dedicated face detection are also different tasks. Detecting a `person` does not automatically mean the program is performing face recognition.

**Main concept:**

**Camera → Frame → YOLO → Class + Confidence + Bounding Box**

---

# File Order

Run and understand the files in this order:

`01_test.py`

↓

`02_read_image.py`

↓

`03_image_processing.py`

↓

`04_thresholding.py`

↓

`05_contours.py`

↓

`06_color_detection.py`

↓

`07_red_object_detection.py`

↓

`08_webcam.py`

↓

`09_webcam_red_detection.py`

↓

`10_yolo_object_detection.py`

↓

`11_object_distance_estimation.py`

↓

`12_hand_tracking.py`

The progression is:

**OpenCV setup**

→ Read an image

→ Process an image

→ Grayscale

→ Thresholding

→ Contours

→ Colour detection

→ Red-object detection

→ Webcam

→ Real-time red detection

→ AI-based object detection

# Day 2 Overall Concept

The classical computer-vision part follows:

**Image / Camera → Pixels → Processing → Threshold / Colour Mask → Contours → Bounding Box → Object Location**

The AI-based part follows:

**Camera → Frame → YOLO Neural Network → Object Class + Confidence + Bounding Box**

The objective is to understand how these two approaches differ before moving toward more advanced robotics vision systems.

---

# `11_object_distance_estimation.py`

**Purpose:** Estimate the distance to a detected phone using YOLO and a simple camera-distance formula.

**Why:** Once an object is detected, we can also estimate how far away it is by comparing its pixel width with a known real-world width.

**What it does:**
- Loads YOLO.
- Opens the webcam.
- Detects objects.
- Keeps only `cell phone` detections.
- Measures the phone width in pixels.
- Uses a known phone width and focal length to estimate the distance.
- Draws a bounding box and displays the estimated distance on the frame.

**Key components:**

`YOLO(...)` — loads the pretrained detection model.

`box.xyxy[0].tolist()` — gets the bounding box coordinates.

`pixel_width = x2 - x1` — calculates the object width in pixels.

`KNOWN_WIDTH` — the real width of the object in centimetres.

`FOCAL_LENGTH` — a camera constant used for distance estimation.

`cv2.putText()` — displays the estimated distance on the image.

**Main concept:** Detected object → pixel size → camera geometry → estimated distance.

---

# `12_hand_tracking.py`

**Purpose:** Track hands in real time using MediaPipe.

**Why:** Hand tracking is used in gesture control, sign-language recognition, AR interaction, and touchless interfaces.

**What it does:**
- Opens the webcam.
- Creates a MediaPipe Hand Landmarker.
- Converts each frame to RGB.
- Detects hand landmarks.
- Draws green circles for each landmark.
- Connects joints with lines to form a hand skeleton.
- Displays the result until `q` is pressed.

**Key components:**

`mp.tasks.vision.HandLandmarker` — loads the hand detection model.

`mp.Image(...)` — converts the OpenCV frame into MediaPipe image data.

`landmarker.detect_for_video(...)` — detects hands in each frame.

`hand_landmarks` — stores the 21 key points of each detected hand.

`cv2.circle()` — draws each landmark.

`cv2.line()` — draws connections between the joints.

**Main concept:** Camera frame → hand landmarks → tracked joints → gesture and interaction data.

---

# File Order

Run and understand the files in this order:

`01_test.py`

↓

`02_read_image.py`

↓

`03_image_processing.py`

↓

`04_thresholding.py`

↓

`05_contours.py`

↓

`06_color_detection.py`

↓

`07_red_object_detection.py`

↓

`08_webcam.py`

↓

`09_webcam_red_detection.py`

↓

`10_yolo_object_detection.py`

↓

`11_object_distance_estimation.py`

↓

`12_hand_tracking.py`

The progression is:

**OpenCV setup**

→ Read an image

→ Process an image

→ Grayscale

→ Thresholding

→ Contours

→ Colour detection

→ Red-object detection

→ Webcam

→ Real-time red detection

→ AI-based object detection

→ Distance estimation

→ Hand tracking

# Day 2 Overall Concept

The classical computer-vision part follows:

**Image / Camera → Pixels → Processing → Threshold / Colour Mask → Contours → Bounding Box → Object Location**

The AI-based part follows:

**Camera → Frame → YOLO Neural Network → Object Class + Confidence + Bounding box**

The advanced part follows:

**Camera → Detection → Size / Geometry → Distance estimate**

**Camera → Hand landmarks → Joint tracking → Gesture interaction**

The objective is to understand how these approaches differ before moving toward more advanced robotics vision systems.
