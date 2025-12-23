# Real-Time Face Detection using MediaPipe and OpenCV

## Project Overview
This project implements **real-time face detection** using **MediaPipe Face Detection** integrated with **OpenCV** for webcam video capture and visualization. The system detects faces in a live video stream and overlays precise bounding boxes and key facial information in real time.

Compared to traditional Haar Cascade methods, MediaPipe provides a faster and more robust deep learning–based solution.

---

## Objectives
- Perform real-time face detection using a webcam
- Utilize MediaPipe’s lightweight face detection model
- Visualize detected faces with bounding boxes
- Integrate MediaPipe with OpenCV for live video processing
- Understand deep learning–based face detection pipelines

---

## Technologies Used
- Python 3
- OpenCV (cv2)
- MediaPipe

---

## System Configuration

### Face Detection Parameters
- **Minimum Detection Confidence:** 1.0
- **Model Selection:** 0  
  - Optimized for short-range face detection (within ~2 meters)

These settings prioritize detection accuracy in real-time scenarios.

---

## Methodology

### 1. Webcam Capture
- Live video stream captured using OpenCV
- Frames processed continuously until user termination

---

### 2. Frame Preprocessing
- Frames flipped horizontally for natural interaction
- Resized to 500 × 500 resolution
- Converted from BGR to RGB (required by MediaPipe models)

---

### 3. Face Detection
- MediaPipe Face Detection model processes each frame
- Detects faces and provides:
  - Bounding box coordinates
  - Detection confidence scores

---

### 4. Visualization
- MediaPipe drawing utilities used to render:
  - Bounding boxes
  - Key facial detection annotations

---

### 5. Real-Time Display
- Annotated video feed shown in a window
- Execution stops when the **'p'** key is pressed

---

## Key Concepts Demonstrated
- Deep learning–based face detection
- Real-time video processing
- MediaPipe Face Detection API
- RGB/BGR color space conversion
- OpenCV and MediaPipe integration

---

## Output
- Live webcam feed with detected faces
- High-confidence bounding boxes
- Smooth and responsive detection

---

## How to Run the Project

### Prerequisites
Install required libraries:
- opencv-python
- mediapipe

---

### Steps
1. Ensure a webcam is connected
2. Run the Python script
3. Face the camera
4. Observe:
   - Real-time face detection
   - Bounding box overlays
5. Press **'p'** to exit

---

## Learning Outcomes
- Understanding modern face detection systems
- Experience using MediaPipe deep learning models
- Ability to build real-time computer vision applications
- Comparison between classical and deep learning detectors

---

## Limitations
- Optimized for frontal faces
- Requires sufficient lighting
- Detection confidence set to maximum may miss subtle faces

---

## Future Improvements
- Adjust detection confidence dynamically
- Switch to long-range face detection model
- Integrate face landmarks or mesh detection
- Add face tracking across frames
- Use detected faces for recognition tasks

---

## Use Case
This project is suitable for:
- Computer vision and AI learning
- Face detection applications
- Human-computer interaction systems
- Real-time video analysis tools

---

## Author
Developed as an educational computer vision project demonstrating real-time face detection using MediaPipe and OpenCV.
