# Single-Image Lane Detection System

A Computer Vision project that detects road lane markings from a single image using image preprocessing, Canny edge detection, Region of Interest masking, and Hough Line Transform.

## Project Overview

The system takes a road image as input and processes it through multiple Computer Vision stages.

The complete pipeline is:

Input Image
↓
Grayscale Conversion
↓
Gaussian Filtering
↓
Canny Edge Detection
↓
Region of Interest
↓
Hough Line Transform
↓
Lane Detection
↓
Visualization

## Features

- Single-image lane detection
- Grayscale conversion
- Gaussian noise reduction
- Canny edge detection
- Region-of-interest extraction
- Hough line detection
- Lane line visualization
- Intermediate result generation
- Complete pipeline visualization
- Automated validation tests

## Technologies

- Python
- OpenCV
- NumPy
- Matplotlib
- PyTest

## Requirements

Python 3.9 or higher is recommended.

## Project Structure

Lane-Detection/

├── input/
│   └── road.jpeg
│
├── output/
│
├── src/
│   ├── __init__.py
│   ├── preprocessing.py
│   ├── edge_detection.py
│   ├── lane_detection.py
│   └── visualization.py
│
├── tests/
│   └── test_project.py
│
├── main.py
├── requirements.txt
├── README.md
└── statement.md

## Installation

Open a terminal in the project root directory.

Create a virtual environment:

python -m venv venv

Activate the virtual environment on Windows:

venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

## Input Image

Place the input road image at:

input/road.jpeg

The project expects the exact filename:

road.jpeg

## Running the Project

Run:

python main.py

The program processes the image and saves all generated results inside:

output/

## Output Files

The program generates:

01_grayscale.jpg
02_blurred.jpg
03_canny_edges.jpg
04_region_of_interest.jpg
05_lane_detected.jpg
06_complete_pipeline.jpg

The main final result is:

output/05_lane_detected.jpg

The complete visual pipeline is:

output/06_complete_pipeline.jpg

## Testing

Run the automated tests using:

pytest

The tests validate:

- Input image availability
- Image loading
- Grayscale conversion
- Gaussian filtering
- Canny edge detection
- Region-of-interest processing
- Hough line detection

## Computer Vision Techniques

### Grayscale Conversion

Converts the input RGB/BGR image into a single-channel grayscale representation.

### Gaussian Filtering

Reduces image noise before edge detection.

### Canny Edge Detection

Identifies strong edges in the processed road image.

### Region of Interest

Restricts processing to the region containing the road.

### Hough Transform

Detects straight line segments from the edge image.

## Limitations

- The system is designed for static images.
- Performance depends on image quality and lighting.
- Strongly curved lane markings may not be represented perfectly by straight lines.
- The method is sensitive to road markings and environmental conditions.

## Future Enhancements

- Real-time video lane detection
- Lane curvature estimation
- Lane departure warning
- Deep-learning-based lane segmentation
- Weather and nighttime robustness
- Real-time camera integration

## Academic Relevance

The project applies fundamental Computer Vision concepts including image preprocessing, filtering, edge detection, region selection, line detection, and visualization.