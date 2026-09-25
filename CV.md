# Day 2 --- Make the Machine See

This folder introduces the basic computer-vision concepts used in Day 2
of the robotics foundation program.

The learning path is:

**Camera / Image → OpenCV → Image Processing → Thresholding → Contours →
Object Detection**

The purpose is not to start with advanced AI or YOLO. The goal is to
understand how a computer can work with pixels and use simple vision
techniques to locate an object.

------------------------------------------------------------------------

## 1. Software Setup

The examples are intended to be written and run in **VS Code**.

The main requirements are:

-   Python
-   OpenCV
-   NumPy

OpenCV provides the computer-vision functions. NumPy is used for
numerical arrays, including the HSV colour ranges used for colour
detection.

A GPU is not required for these exercises.

Check that Python is installed from the VS Code terminal, then install
OpenCV and NumPy.

To verify OpenCV, check its installed version from the terminal.

------------------------------------------------------------------------

## 2. Folder Structure

The Day 2 folder contains a sequence of small programs. Each file
introduces one concept and then builds toward real-time camera-based
detection.

The intended order is:

1.  `01_test.py`
2.  `02_read_image.py`
3.  `03_image_processing.py`
4.  `04_thresholding.py`
5.  `05_contours.py`
6.  `06_color_detection.py`
7.  `07_red_object_detection.py`
8.  `08_webcam.py`
9.  `09_webcam_red_detection.py`

An image such as `cone.jpg` can be kept in the same folder for the
image-based exercises.

------------------------------------------------------------------------

# 3. `01_test.py` --- Check OpenCV

This is the simplest program in the folder.

It imports OpenCV and prints the installed OpenCV version. It also
prints a message confirming that OpenCV can be imported successfully.

### Important lines

**Importing OpenCV**

`import cv2`

This makes the OpenCV library available to the Python program.

**Checking the version**

`cv2.__version__`

This returns the installed OpenCV version.

### Purpose

This file confirms that the Python environment and OpenCV installation
are working before moving to image processing.

------------------------------------------------------------------------

# 4. `02_read_image.py` --- Read and Display an Image

This program introduces the basic image workflow.

It loads an image from the same folder and displays it in an OpenCV
window.

### Important functions

**`cv2.imread()`**

Reads an image from a file and stores it as image data.

The filename must point to an existing image. For example, the image
file used in the exercise can be named `cone.jpg`.

**`cv2.imshow()`**

Creates a window and displays the image.

The first argument is the window name and the second argument is the
image to display.

**`cv2.waitKey(0)`**

Waits indefinitely for a keyboard input. This keeps the image window
open until a key is pressed.

**`cv2.destroyAllWindows()`**

Closes the OpenCV windows.

### Concept

The basic flow is:

**Image file → OpenCV reads image → OpenCV displays image**

------------------------------------------------------------------------

# 5. What OpenCV Sees

A digital image is fundamentally numerical data.

A colour image is made of pixels, and each pixel contains numerical
values representing its colour.

OpenCV normally represents colour images using **BGR** order rather than
RGB.

That means a colour pixel is represented conceptually as:

**Blue, Green, Red**

For example, a pixel with very high red and very low blue and green
represents red.

This becomes important when detecting colours.

------------------------------------------------------------------------

# 6. `03_image_processing.py` --- Basic Image Processing

This file introduces simple image transformations.

The first version demonstrates image resizing.

### `cv2.resize()`

Resizes an image to a specified width and height.

This is an example of image processing because the original image data
is transformed into a new representation.

The program displays both the original and resized images so the
difference can be observed.

------------------------------------------------------------------------

## Grayscale Conversion

The same file can also demonstrate conversion from colour to grayscale.

### `cv2.cvtColor()`

Converts an image from one colour representation to another.

### `cv2.COLOR_BGR2GRAY`

Tells OpenCV to convert the image from BGR colour into grayscale.

A colour image has three colour channels:

**Blue + Green + Red**

A grayscale image has one intensity channel representing brightness.

Typically:

**0 = black**

**255 = white**

Grayscale images are useful because many image-processing operations
become simpler when colour information is removed.

------------------------------------------------------------------------

# 7. `04_thresholding.py` --- Thresholding

Thresholding separates pixels according to their intensity.

A simple binary threshold can be understood as:

**Pixel below the chosen threshold → black**

**Pixel at or above the threshold → white**

### `cv2.threshold()`

Performs thresholding on an image.

The grayscale image is used as the input because the threshold is based
on pixel intensity.

The important parameters represent:

-   The input grayscale image
-   The threshold value
-   The maximum value assigned to pixels that pass the threshold
-   The thresholding method

### `cv2.THRESH_BINARY`

Creates a binary image consisting of black and white regions.

### Why thresholding is useful

Suppose an object is visually different from its background.
Thresholding can sometimes produce an image where:

**Object → white**

**Background → black**

This makes the object easier to locate with later operations such as
contour detection.

Thresholding is highly dependent on lighting and the chosen threshold
value, so it does not work equally well in every environment.

------------------------------------------------------------------------

# 8. `05_contours.py` --- Finding Boundaries

A contour represents the boundary of a connected region in an image.

The program first creates a thresholded image and then searches for
contours in it.

### `cv2.findContours()`

Searches an image for contours.

The thresholded image is supplied as the input.

### `cv2.RETR_EXTERNAL`

Tells OpenCV to retrieve only the outermost contours.

This is useful when the goal is to find the external boundary of objects
rather than every possible nested boundary.

### `cv2.CHAIN_APPROX_SIMPLE`

Compresses contour information by removing unnecessary points while
preserving the overall contour shape.

### `len(contours)`

Returns the number of contours that were found.

### `cv2.contourArea()`

Calculates the area enclosed by a contour.

The area is useful for filtering out very small regions that may be
caused by noise.

### `cv2.drawContours()`

Draws the detected contours on the image so they can be visualized.

------------------------------------------------------------------------

# 9. Bounding Boxes

After detecting a contour, a rectangle can be drawn around it.

### `cv2.boundingRect()`

Calculates a rectangular boundary around a contour.

It provides four values:

-   **x** --- horizontal position of the left edge
-   **y** --- vertical position of the top edge
-   **w** --- width of the rectangle
-   **h** --- height of the rectangle

### `cv2.rectangle()`

Draws the rectangle on the image.

A common workflow is:

**Contour → Bounding rectangle → Visual location of object**

### Area filtering

The contour area can be checked before drawing a bounding box.

For example, requiring an area greater than a chosen value prevents very
small contours from being treated as objects.

This is a simple form of noise filtering.

------------------------------------------------------------------------

# 10. `06_color_detection.py` --- Detecting a Colour

This file introduces colour-based computer vision.

Instead of converting the image to grayscale, the image is converted to
the **HSV colour space**.

## HSV

HSV represents colour using:

-   **H --- Hue**
-   **S --- Saturation**
-   **V --- Value**

Hue represents the basic colour.

Saturation represents how strong or pure the colour is.

Value represents brightness.

HSV is often convenient for colour detection because colour information
is separated from brightness more clearly than in BGR.

### `cv2.COLOR_BGR2HSV`

Converts an OpenCV BGR image into HSV.

### `np.array()`

Creates numerical arrays containing the lower and upper limits of the
desired HSV range.

### `cv2.inRange()`

Checks every pixel against the selected HSV range.

Pixels inside the selected range become white in the mask.

Pixels outside the range become black.

The result is called a **mask**.

Conceptually:

**Matching colour → white**

**Other colours → black**

------------------------------------------------------------------------

# 11. Why Red Requires Two HSV Ranges

Red is located at both ends of OpenCV's HSV hue scale.

Therefore, detecting red can require two hue ranges:

**Lower red range → near hue 0**

**Upper red range → near hue 179**

The two masks can then be combined.

This is important because using only the lower red range may miss some
red pixels.

The exact HSV limits are not universal. Camera characteristics,
lighting, shadows, white balance, fabric, and the particular shade of
red can change the values produced by the camera.

For that reason, a colour detector may need its HSV limits adjusted for
the environment.

------------------------------------------------------------------------

# 12. `07_red_object_detection.py` --- Red Object + Contours

This program combines the previous concepts.

The processing pipeline is:

**Image → BGR to HSV → Red mask → Contours → Area filtering → Bounding
box → Label**

The image is first converted to HSV.

A red colour range is selected.

A mask is generated.

Contours are detected from the mask.

Small contours can be ignored using an area threshold.

A bounding rectangle is then created around the remaining contour.

### `cv2.putText()`

Places text on an image.

It can be used to label the detected region as a red object.

### Important idea

This is **classical computer vision**.

It is not machine learning, deep learning, or YOLO.

The program is not understanding the object semantically. It is finding
image regions whose pixels match the selected colour criteria.

------------------------------------------------------------------------

# 13. `08_webcam.py` --- Read a Live Camera

This file changes the input from a saved image to a live camera.

### `cv2.VideoCapture(0)`

Opens the default camera.

The number `0` normally refers to the first available camera. Other
camera devices may have different indexes.

### `camera.read()`

Reads the next frame from the camera.

It provides:

-   A success value
-   The captured frame

The success value is checked before processing the frame.

### `while True`

Creates a continuous loop so that frames can be captured repeatedly.

A camera produces a sequence of frames rather than a single image.

### `cv2.imshow()`

Displays the current frame.

### `cv2.waitKey(1)`

Waits briefly for keyboard input while allowing the next frame to be
processed.

Checking for the `q` key allows the user to exit the loop.

### `camera.release()`

Releases the camera after the loop ends.

### `cv2.destroyAllWindows()`

Closes the OpenCV windows.

------------------------------------------------------------------------

# 14. Camera Mirroring

The camera feed may appear mirrored.

This is common with front-facing webcams and does not mean the camera
hardware is malfunctioning.

If an unmirrored view is required, the frame can be horizontally flipped
before displaying or processing it.

### `cv2.flip(frame, 1)`

The second argument specifies a horizontal flip.

The important distinction is:

**Displaying a mirrored image is a visual transformation.**

It does not mean that OpenCV has changed the actual object or understood
the scene incorrectly.

For robotics applications, left/right orientation should be handled
deliberately because it can affect decisions such as turning left or
right.

------------------------------------------------------------------------

# 15. `09_webcam_red_detection.py` --- Real-Time Red Object Detection

This is the main exercise that combines the concepts from the previous
files.

The processing pipeline is:

**Camera → Frame → HSV → Red Mask → Contours → Area Filter → Bounding
Box → Label**

The camera continuously supplies frames.

Each frame is converted from BGR to HSV.

The selected red ranges are used to create a mask.

Contours are detected from the mask.

Small contours are ignored.

A bounding box is drawn around detected red regions.

The original camera frame and the mask can both be displayed.

### Two useful windows

**Camera**

Shows the original camera image with the detection box and label.

**Mask**

Shows what the colour detector is actually selecting.

The mask is particularly useful for debugging.

If the red shirt is not being detected, the mask helps determine whether
the problem is the colour range, lighting, or another part of the
processing pipeline.

------------------------------------------------------------------------

# 16. Why a Red Shirt May Not Be Detected

A program cannot simply understand that a shirt is "red."

It checks numerical pixel values.

The actual HSV values produced by a camera can change because of:

-   Lighting
-   Shadows
-   Camera exposure
-   White balance
-   The exact shade of red
-   Reflections
-   Background colours

Therefore, the selected HSV range may need adjustment.

A good way to understand this is to watch the mask.

If the shirt remains black in the mask, its pixels are outside the
selected HSV range.

If the shirt becomes white but other objects also become white, the
range may be too broad.

This demonstrates an important principle of computer vision:

**Detection quality depends on the representation and criteria used to
separate an object from its surroundings.**

------------------------------------------------------------------------

# 17. Finding the Object's Centre

Once a bounding rectangle provides:

**x, y, w, h**

the centre of the detected region can be calculated.

The horizontal centre is:

**x + width / 2**

The vertical centre is:

**y + height / 2**

In the Python implementation, integer division can be used so that the
resulting pixel coordinates are integers.

The centre gives the object's approximate position within the camera
frame.

This is the beginning of connecting computer vision to robot control.

------------------------------------------------------------------------

# 18. From Vision to Robot Movement

Suppose the camera image is divided into three horizontal regions:

**LEFT \| CENTER \| RIGHT**

The detected object's centre can then be compared with these regions.

A simple future control concept could be:

**Object on left → turn left**

**Object in centre → move forward**

**Object on right → turn right**

The complete conceptual pipeline becomes:

**Camera → OpenCV → Find object → Calculate centre → Determine position
→ Motor command**

This is the bridge between computer vision and robotics.

The Day 2 exercises stop before actual motor control. The objective here
is to understand the vision side first.

------------------------------------------------------------------------

# 19. Important OpenCV Functions Used

### `cv2.imread()`

Reads an image from a file.

### `cv2.imshow()`

Displays an image or video frame.

### `cv2.waitKey()`

Waits for keyboard input and allows OpenCV windows to update.

### `cv2.destroyAllWindows()`

Closes OpenCV windows.

### `cv2.resize()`

Changes image dimensions.

### `cv2.cvtColor()`

Converts an image between colour representations.

### `cv2.threshold()`

Creates a thresholded image based on pixel intensity.

### `cv2.findContours()`

Finds boundaries of connected regions.

### `cv2.contourArea()`

Calculates the area of a contour.

### `cv2.boundingRect()`

Calculates a rectangular boundary around a contour.

### `cv2.rectangle()`

Draws a rectangle.

### `cv2.drawContours()`

Draws contours.

### `cv2.putText()`

Writes text on an image.

### `cv2.VideoCapture()`

Opens a camera or video source.

### `camera.read()`

Captures a frame from the camera.

### `camera.release()`

Releases the camera.

### `cv2.flip()`

Flips an image, such as horizontally for correcting a mirrored camera
view.

### `cv2.inRange()`

Creates a mask by selecting pixels inside a specified numerical range.

------------------------------------------------------------------------

# 20. The Complete Day 2 Pipeline

The concepts introduced in this folder can be summarized as:

**Image / Camera**

↓

**OpenCV reads the image**

↓

**Image Processing**

↓

**Grayscale or HSV conversion**

↓

**Thresholding or Colour Mask**

↓

**Contours**

↓

**Object Location**

↓

**Bounding Box**

↓

**Object Centre**

↓

**Possible Robot Decision**

The two broad approaches introduced here are:

### Classical Computer Vision

**Image → Threshold / Colour Mask → Contour → Object**

This is what the Day 2 exercises primarily use.

### AI-Based Computer Vision

**Image → Neural Network / YOLO → Object + Class + Confidence**

AI-based detection is a later topic. Understanding the classical
pipeline first makes it easier to understand what an object detector is
actually doing at a higher level.

------------------------------------------------------------------------

# 21. Recommended Practice Order

Work through the files in this order:

**01_test.py**

Verify that OpenCV works.

↓

**02_read_image.py**

Learn how OpenCV reads and displays an image.

↓

**03_image_processing.py**

Learn resizing and grayscale conversion.

↓

**04_thresholding.py**

Learn how pixels can be separated using intensity.

↓

**05_contours.py**

Learn how boundaries can be extracted from a binary image.

↓

**06_color_detection.py**

Learn HSV and colour masks.

↓

**07_red_object_detection.py**

Combine colour detection with contours and bounding boxes.

↓

**08_webcam.py**

Learn how to process a live camera stream.

↓

**09_webcam_red_detection.py**

Combine the complete pipeline in real time.

------------------------------------------------------------------------

# 22. What You Should Know After Day 2

You do not need to memorize every OpenCV function.

You should be able to explain:

-   What OpenCV is.
-   How an image is represented as numerical pixel data.
-   Why OpenCV commonly uses BGR.
-   What grayscale means.
-   What thresholding does.
-   What a binary image is.
-   What a contour represents.
-   What a bounding box represents.
-   Why contour area can be used to filter noise.
-   What HSV represents.
-   Why HSV is useful for colour detection.
-   What a mask is.
-   Why red can require two HSV ranges.
-   How OpenCV reads frames from a webcam.
-   Why a webcam image may appear mirrored.
-   How a detected object's centre can be calculated.
-   How object position can eventually be converted into a robot
    movement decision.

The main goal is to understand the pipeline rather than memorize syntax.

**Camera / Image → Pixels → Processing → Detection → Position → Decision**