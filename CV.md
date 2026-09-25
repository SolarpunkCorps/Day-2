# Day 2 — Make the Machine See

A concise, detailed quick-reference for the Day 2 OpenCV files.

Learning path:

**Image / Camera → OpenCV → Processing → Threshold / Mask → Contours → Bounding Box → Detection → Position**

---

## 0. Setup

### Software

- **VS Code** — write and run the Python files.
- **Python** — programming language.
- **OpenCV** — image/video processing and computer vision.
- **NumPy** — numerical arrays and HSV colour ranges.
- **Ultralytics** — required later if using YOLO object detection.

### Install

```bash
pip install opencv-python numpy
```

For YOLO:

```bash
pip install ultralytics
```

### Verify

```bash
python --version
```

```bash
python -c "import cv2; print(cv2.__version__)"
```

```bash
python -c "import numpy; print(numpy.__version__)"
```

```bash
python -c "import ultralytics; print(ultralytics.__version__)"
```

### Run a file

```bash
python filename.py
```

Example:

```bash
python 01_test.py
```

---

# `01_test.py` — Test OpenCV

### Why?

- Confirms that OpenCV is installed.
- Confirms Python can import OpenCV.
- Prevents setup problems from appearing later.

### Key lines

- **`import cv2`**
  - Loads OpenCV.
  - `cv2` is the Python name used for OpenCV.

- **`cv2.__version__`**
  - Returns the installed OpenCV version.

### Expected result

- OpenCV version is printed.
- A confirmation message appears.

### Learn

**Python → OpenCV is working.**

---

# `02_read_image.py` — Read an Image

### Why?

- Before processing images, first learn how to load one.
- This is the basic OpenCV image workflow.

### Input

- `pic1.jpg`
- Keep the image in the same folder as the Python file.

### Key functions

- **`cv2.imread()`**
  - Reads an image from a file.
  - Returns image data that OpenCV can process.

- **`cv2.imshow()`**
  - Opens a window.
  - Displays the image.

- **`cv2.waitKey(0)`**
  - Waits until a key is pressed.
  - `0` means wait indefinitely.

- **`cv2.destroyAllWindows()`**
  - Closes OpenCV windows.

### Flow

**Image file → `imread()` → `imshow()` → keyboard input → close**

### Learn

An image is data that OpenCV can read, modify and display.

---

# `03_image_processing.py` — Basic Processing

### Why?

- Raw images are not always the easiest form to analyse.
- We can transform an image before detecting anything.

### Part 1 — Resize

- **`cv2.resize()`**
  - Changes image width and height.
  - Useful for making images smaller/faster to process or fitting a required size.

### Part 2 — Grayscale

- **`cv2.cvtColor()`**
  - Converts an image between colour spaces.

- **`cv2.COLOR_BGR2GRAY`**
  - Converts OpenCV's BGR image to grayscale.

### BGR

OpenCV normally stores colour as:

**B → Blue**

**G → Green**

**R → Red**

Not RGB.

### Grayscale

- Colour image → 3 colour channels.
- Grayscale → 1 brightness/intensity channel.
- `0` → black.
- `255` → white.

### Why grayscale?

- Removes colour information.
- Simplifies many later operations.
- Useful for intensity-based processing.

### Flow

**BGR image → resize / grayscale → processed image**

### Learn

Different image representations are useful for different vision tasks.

---

# `04_thresholding.py` — Thresholding

### Why?

- We want to separate pixels into useful regions.
- A binary image is easier to analyse than a full grayscale image for some tasks.

### Key function

- **`cv2.threshold()`**
  - Compares each pixel with a threshold value.
  - Produces a new thresholded image.

### `cv2.THRESH_BINARY`

Creates two basic regions:

- One side of threshold → black.
- Other side → white.

Conceptually:

**Pixel < threshold → black**

**Pixel ≥ threshold → white**

### Parameters

The threshold operation uses:

- Input grayscale image.
- Threshold value.
- Maximum output value.
- Thresholding method.

### Why?

A useful result can look like:

**Object → white**

**Background → black**

This makes later contour detection easier.

### Limitation

Thresholding is affected by:

- Lighting.
- Shadows.
- Contrast.
- Selected threshold value.

### Flow

**Grayscale → threshold → binary image**

### Learn

Thresholding turns continuous intensity information into simpler regions.

---

# `05_contours.py` — Find Boundaries

### Why?

- After thresholding, we have regions.
- We need to identify the boundaries of those regions.

### Key function

- **`cv2.findContours()`**
  - Searches for boundaries of connected regions.

### Important options

- **`cv2.RETR_EXTERNAL`**
  - Retrieves outermost contours.
  - Useful when internal/nested contours are not needed.

- **`cv2.CHAIN_APPROX_SIMPLE`**
  - Removes unnecessary contour points.
  - Keeps the basic contour shape.

### Count contours

- **`len(contours)`**
  - Tells how many contours were found.

### Measure contours

- **`cv2.contourArea()`**
  - Calculates the area inside a contour.
  - Useful for deciding whether a region is large enough to matter.

### Display contours

- **`cv2.drawContours()`**
  - Draws the detected boundaries on the image.

### Flow

**Binary image → contours → boundaries**

### Learn

A contour describes the boundary of a connected image region.

---

# Bounding Boxes — Locate a Region

This concept is used with contour detection.

### `cv2.boundingRect(contour)`

Returns:

- **`x`** → left position.
- **`y`** → top position.
- **`w`** → width.
- **`h`** → height.

### `cv2.rectangle()`

- Draws the rectangle.
- Useful for showing where the detected region is.

### Area filtering

Example concept:

**If area > selected value → keep region**

**Otherwise → ignore it**

### Why?

- Removes tiny regions.
- Reduces noise.
- Prevents every tiny contour from being treated as an object.

### Flow

**Contour → area check → bounding rectangle → visual object location**

---

# `06_color_detection.py` — Detect a Colour

### Why?

- Grayscale uses brightness.
- Sometimes we specifically need colour information.
- HSV is convenient for colour-based detection.

### HSV

**H — Hue**
- Basic colour.

**S — Saturation**
- Colour strength/purity.

**V — Value**
- Brightness.

### Key conversion

- **`cv2.cvtColor()`**
  - Converts the image.

- **`cv2.COLOR_BGR2HSV`**
  - BGR → HSV.

### Define a colour range

- **`np.array()`**
  - Stores numerical lower/upper limits.

Conceptually:

**Lower HSV limit → allowed range → Upper HSV limit**

### Create mask

- **`cv2.inRange()`**
  - Checks every pixel.
  - Inside range → white.
  - Outside range → black.

### Mask

A mask is an image showing where the selected condition is true.

**White = selected**

**Black = not selected**

### Why?

Now the computer has a simple map of where the selected colour appears.

### Flow

**BGR → HSV → colour range → mask**

---

# Why Red Uses Two Ranges

Red is special in OpenCV's HSV hue scale.

Red occurs near both ends:

- **Near hue 0**
- **Near hue 179**

Therefore, red detection can use:

**Range 1 → low hue red**

**Range 2 → high hue red**

Then the two masks are combined.

### Why?

Using only one red range can miss some red pixels.

### Important

HSV values are not universal.

They change with:

- Lighting.
- Shadows.
- Camera exposure.
- White balance.
- Exact shade of red.
- Reflections.
- Background.

So HSV ranges may need calibration.

---

# `07_red_object_detection.py` — Red Object

### Why?

This combines several previous concepts into one detector.

### Pipeline

**Image → HSV → red mask → contours → area filter → bounding box → label**

### Key components

- **`cv2.inRange()`**
  - Creates the red mask.

- **`cv2.findContours()`**
  - Finds connected red regions.

- **`cv2.contourArea()`**
  - Measures each region.

- **`cv2.boundingRect()`**
  - Gets object position and size.

- **`cv2.rectangle()`**
  - Draws the detection box.

- **`cv2.putText()`**
  - Adds the `Red Object` label.

### Why area filtering?

- Removes tiny noise.
- Keeps larger candidate regions.

### Important

This is **classical computer vision**.

It is not:

- Machine learning.
- Deep learning.
- YOLO.

The program does not know that something is a shirt, phone or person.

It knows only:

**"These pixels match my red criteria."**

### Learn

**Colour + contour + bounding box = simple object detector**

---

# `08_webcam.py` — Live Camera

### Why?

A robot usually receives a continuous camera stream, not one saved image.

### Key function

- **`cv2.VideoCapture(0)`**
  - Opens the default camera.
  - `0` usually means the first camera.

### Read frame

- **`camera.read()`**
  - Captures the next frame.
  - Returns:
    - Success/failure status.
    - Frame image.

### Check success

- If the frame was not captured:
  - Print an error.
  - Stop the loop.

### Continuous processing

- **`while True`**
  - Repeats frame capture.
  - Each loop processes one frame.

### Display

- **`cv2.imshow()`**
  - Shows the current frame.

### Keyboard

- **`cv2.waitKey(1)`**
  - Waits briefly.
  - Allows the window to update.
  - Checks for key input.

- **`ord("q")`**
  - Converts `q` into a value that can be compared with the keyboard result.

### Cleanup

- **`camera.release()`**
  - Gives the camera back to the system.

- **`cv2.destroyAllWindows()`**
  - Closes OpenCV windows.

### Flow

**Camera → frame → display → next frame → repeat**

---

# Camera Mirroring

The webcam may appear mirrored.

### Why?

Front-facing cameras are commonly displayed like a mirror.

### Fix

- **`cv2.flip(frame, 1)`**
  - Flips the frame horizontally.

### Important

Mirroring is only a visual transformation.

It does not mean OpenCV is detecting the wrong object.

For robotics, left/right orientation matters because it can affect movement decisions.

---

# `09_webcam_red_detection.py` — Real-Time Red Detection

### Why?

This combines:

- Webcam input.
- HSV conversion.
- Red detection.
- Masking.
- Contours.
- Area filtering.
- Bounding boxes.

### Pipeline

**Camera → Frame → HSV → Red Mask → Contours → Area Filter → Bounding Box → Label**

### Step 1 — Camera

- Open webcam.
- Read each frame.

### Step 2 — Mirror correction

- Horizontally flip the frame if desired.

### Step 3 — HSV

- Convert BGR → HSV.

### Step 4 — Red ranges

- Define low-hue red range.
- Define high-hue red range.

### Step 5 — Masks

- Create `mask1`.
- Create `mask2`.

### Step 6 — Combine

- Combine both masks.
- Result contains both red ranges.

### Step 7 — Contours

- Find connected regions in the mask.

### Step 8 — Area filter

- Ignore small regions.
- Keep larger candidate regions.

### Step 9 — Bounding box

- Find `x, y, w, h`.
- Draw rectangle.

### Step 10 — Label

- Add `RED` using `cv2.putText()`.

### Two windows

**Camera**
- Original camera view.
- Detection box.
- Label.

**Red Mask**
- White = detected red.
- Black = not detected.

### Why the mask is important

Use it for debugging.

If your red shirt is not detected:

**Shirt black in mask**
→ HSV range may not match.

**Shirt white + many unrelated areas white**
→ HSV range may be too broad.

### Learn

**Camera → vision processing → detected region**

---

# Why a Red Shirt May Not Be Detected

The program does not understand the word "red."

It compares pixel numbers.

Camera values change because of:

- Lighting.
- Shadows.
- Exposure.
- White balance.
- Fabric colour.
- Reflections.
- Background.

### Therefore

HSV thresholds often need adjustment.

### Key idea

**Computer vision detection depends on how the image is represented and what numerical criteria are selected.**

---

# Finding the Object Centre

Once we have:

**`x, y, w, h`**

we can estimate the centre.

### Horizontal centre

**`x + w / 2`**

### Vertical centre

**`y + h / 2`**

In Python, integer division can be used when integer pixel coordinates are required.

### Why?

The centre tells us where the detected object is inside the camera frame.

That information can later control a robot.

---

# From Vision to Robot Movement

Divide the camera view into:

**LEFT | CENTER | RIGHT**

Then compare the object's centre with these regions.

Example control logic:

**Object left → turn left**

**Object centre → move forward**

**Object right → turn right**

### Full robotics idea

**Camera → OpenCV → Find object → Centre → Position → Motor command**

This is the bridge between computer vision and robot control.

---

# `10_yolo_object_detection.py` — AI Object Detection

It introduces the next level after colour-based detection.

### Why?

The red detector asks:

**"Where are pixels that look red?"**

YOLO asks:

**"Which learned object category is present, where is it, and how confident is the model?"**

### Install

```bash
pip install ultralytics
```

### Key components

- **`from ultralytics import YOLO`**
  - Imports the YOLO interface.

- **`YOLO(...)`**
  - Loads a pretrained model.

- **`model(frame)`**
  - Sends the camera frame through the neural network.

- **`results[0].plot()`**
  - Creates an annotated frame.

### Detection information

A YOLO detection can provide:

**Class**
- Example: person, bottle, phone, chair.

**Bounding box**
- Object location and size.

**Confidence**
- Numerical confidence associated with the detection.

### Classical vs AI

**Classical**

Image → Colour / Threshold → Mask → Contour → Box

**YOLO**

Image → Neural network → Class + Confidence + Box

### Important limitation

YOLO does not automatically detect every possible object.

It can detect the categories included in its training data.

Also:

**Person detection ≠ dedicated face detection ≠ face recognition**

These are different computer-vision tasks.

---

# Important Functions — Quick Reference

| Function | What it does | Why it matters |
|---|---|---|
| `cv2.imread()` | Reads image | Gets image into Python |
| `cv2.imshow()` | Displays image | Visualise result |
| `cv2.waitKey()` | Reads keyboard input | Controls windows/exit |
| `cv2.destroyAllWindows()` | Closes windows | Cleanup |
| `cv2.resize()` | Resizes image | Changes image dimensions |
| `cv2.cvtColor()` | Changes colour space | BGR → Gray/HSV |
| `cv2.threshold()` | Thresholds pixels | Creates binary regions |
| `cv2.findContours()` | Finds boundaries | Locates regions |
| `cv2.contourArea()` | Finds contour area | Filters regions |
| `cv2.boundingRect()` | Finds rectangle | Locates object |
| `cv2.rectangle()` | Draws rectangle | Visualises detection |
| `cv2.drawContours()` | Draws contours | Visualises boundaries |
| `cv2.putText()` | Writes text | Adds labels |
| `cv2.inRange()` | Creates mask | Selects pixel range |
| `cv2.VideoCapture()` | Opens camera | Gets live input |
| `camera.read()` | Gets next frame | Processes video |
| `camera.release()` | Releases camera | Cleanup |
| `cv2.flip()` | Flips image | Corrects mirror view |

---

# Complete Day 2 Pipeline

### Classical computer vision

**Image / Camera**

↓

**OpenCV reads frame**

↓

**BGR**

↓

**Grayscale or HSV**

↓

**Threshold or colour mask**

↓

**Contours**

↓

**Area filtering**

↓

**Bounding box**

↓

**Object centre**

↓

**Possible robot decision**

### AI-based vision

**Camera**

↓

**Frame**

↓

**YOLO**

↓

**Object class**

+

**Confidence**

+

**Bounding box**

---

# Practice Order

1. **`01_test.py`**
   - Verify OpenCV.

2. **`02_read_image.py`**
   - Read and display an image.

3. **`03_image_processing.py`**
   - Resize and convert to grayscale.

4. **`04_thresholding.py`**
   - Create a binary image.

5. **`05_contours.py`**
   - Find region boundaries.

6. **`06_color_detection.py`**
   - Create an HSV colour mask.

7. **`07_red_object_detection.py`**
   - Detect a red region.

8. **`08_webcam.py`**
   - Read live camera frames.

9. **`09_webcam_red_detection.py`**
   - Detect red in real time.

10. **`10_yolo_object_detection.py`**
   - Detect learned object categories using AI.

---

# Day 2 — What You Should Understand

- **OpenCV** — library for image/video processing.
- **Pixel** — numerical representation of image information.
- **BGR** — OpenCV's common colour representation.
- **Grayscale** — brightness-only image.
- **Threshold** — separates pixels using intensity.
- **Binary image** — simplified black/white image.
- **Contour** — boundary of a connected region.
- **Area** — size of a contour.
- **Bounding box** — rectangle around a detected region.
- **HSV** — colour representation useful for colour detection.
- **Mask** — black/white selection of pixels.
- **Webcam frame** — one image from a live camera stream.
- **YOLO** — pretrained neural-network object detector.
- **Confidence** — model's numerical confidence for a detection.

### Final mental model

**Camera / Image**

→ **Pixels**

→ **Processing**

→ **Detection**

→ **Position**

→ **Decision**

That is the foundation for connecting computer vision to robotics.