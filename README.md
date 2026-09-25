# Day 2 — Make the Machine See

This README explains each Python file in the order it is used.

---

## `01_test.py`

Purpose: Check that OpenCV is installed and working.

What it does:
- Imports OpenCV using `cv2`.
- Prints the installed OpenCV version.
- Prints a message confirming that OpenCV is working.

Main OpenCV concept:
- Importing and verifying the OpenCV library.

---

## `02_read_image.py`

Purpose: Read an image from a file and display it.

What it does:
- Imports OpenCV.
- Loads `cone.jpg` using OpenCV.
- Displays the image in an OpenCV window.
- Waits for a keyboard input.
- Closes the OpenCV window.

Important functions:
- `cv2.imread()` — reads an image from a file.
- `cv2.imshow()` — displays an image.
- `cv2.waitKey()` — waits for keyboard input.
- `cv2.destroyAllWindows()` — closes OpenCV windows.

---

## `03_image_processing.py`

Purpose: Perform basic image processing.

What it does:
- Reads the input image.
- Creates a resized version of the image.
- Displays the original and resized images.
- Also introduces conversion from BGR to grayscale.

Important functions:
- `cv2.resize()` — changes the image dimensions.
- `cv2.cvtColor()` — converts an image from one colour space to another.
- `cv2.COLOR_BGR2GRAY` — converts a BGR image to grayscale.

Main concept:
- An image can be transformed before further analysis.

---

## `04_thresholding.py`

Purpose: Convert a grayscale image into a binary image using a threshold.

What it does:
- Reads the image.
- Converts it to grayscale.
- Applies a threshold.
- Displays the grayscale image and the thresholded image.

Important function:
- `cv2.threshold()` — separates pixels according to their intensity.

With binary thresholding:
- Pixels on one side of the threshold become black.
- Pixels on the other side become white.

Main concept:
- Thresholding can separate regions of an image so that they are easier to analyze.

---

## `05_contours.py`

Purpose: Find boundaries of regions in a thresholded image.

What it does:
- Reads the image.
- Converts it to grayscale.
- Thresholds the image.
- Finds contours.
- Counts the detected contours.
- Calculates the area of each contour.
- Draws the contours on the original image.

Important functions:
- `cv2.findContours()` — finds contours in an image.
- `cv2.contourArea()` — calculates the area of a contour.
- `cv2.drawContours()` — draws detected contours.

Main concept:
- A contour represents the boundary of a connected region.

---

## `06_color_detection.py`

Purpose: Detect a selected colour using HSV.

What it does:
- Reads the image.
- Converts the image from BGR to HSV.
- Defines a lower and upper HSV range for red.
- Creates a mask containing pixels within that range.
- Displays the original image and the red mask.

Important functions:
- `cv2.cvtColor()` — converts BGR to HSV.
- `cv2.inRange()` — selects pixels within a specified range.
- `np.array()` — stores the numerical HSV limits.

Main concept:
- White pixels in the mask match the selected colour range.
- Black pixels do not match the selected range.

---

## `07_red_object_detection.py`

Purpose: Detect a red region and draw a bounding box around it.

What it does:
- Reads the image.
- Converts it to HSV.
- Creates a red-colour mask.
- Finds contours in the mask.
- Calculates contour areas.
- Ignores contours below the selected area.
- Finds a bounding rectangle around the remaining contour.
- Draws the rectangle.
- Adds a `Red Object` label.

Important functions:
- `cv2.inRange()` — creates the red mask.
- `cv2.findContours()` — finds red regions.
- `cv2.contourArea()` — checks the size of each region.
- `cv2.boundingRect()` — finds the rectangular boundary.
- `cv2.rectangle()` — draws the bounding box.
- `cv2.putText()` — writes the label.

Main concept:
- Colour detection + contours + bounding box creates a simple classical object-detection system.

---

## `08_webcam.py`

Purpose: Read and display a live webcam feed.

What it does:
- Opens the default camera.
- Continuously captures frames.
- Checks whether each frame was successfully captured.
- Displays each frame.
- Stops when `q` is pressed.
- Releases the camera.
- Closes the OpenCV windows.

Important functions:
- `cv2.VideoCapture(0)` — opens the default camera.
- `camera.read()` — captures the next frame.
- `cv2.imshow()` — displays the current frame.
- `cv2.waitKey()` — checks for keyboard input.
- `camera.release()` — releases the camera.
- `cv2.destroyAllWindows()` — closes the windows.

Main concept:
- A webcam provides a continuous sequence of images called frames.

---

## `09_webcam_red_detection.py`

Purpose: Detect red objects from a live webcam feed.

What it does:
- Opens the webcam.
- Captures frames continuously.
- Converts each frame from BGR to HSV.
- Creates a red-colour mask.
- Finds contours in the mask.
- Filters small contours by area.
- Creates bounding boxes around detected red regions.
- Labels detected regions as `RED OBJECT`.
- Displays both the camera feed and the mask.
- Stops when `q` is pressed.
- Releases the camera.

Important functions:
- `cv2.VideoCapture()` — opens the camera.
- `camera.read()` — captures each frame.
- `cv2.cvtColor()` — converts each frame to HSV.
- `cv2.inRange()` — creates the red mask.
- `cv2.findContours()` — finds red regions.
- `cv2.contourArea()` — filters small regions.
- `cv2.boundingRect()` — calculates the bounding box.
- `cv2.rectangle()` — draws the box.
- `cv2.putText()` — adds the label.
- `cv2.imshow()` — displays the results.

Main concept:

**Camera → Frame → HSV → Red Mask → Contours → Bounding Box → Detection**

---

## File Order

Run and understand the files in this order:

`01_test.py`

→ `02_read_image.py`

→ `03_image_processing.py`

→ `04_thresholding.py`

→ `05_contours.py`

→ `06_color_detection.py`

→ `07_red_object_detection.py`

→ `08_webcam.py`

→ `09_webcam_red_detection.py`

The files progressively combine the same basic OpenCV operations until the final file performs real-time red-object detection from the webcam.