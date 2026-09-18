# Project Statement

## Project Title

Single-Image Lane Detection System Using Computer Vision

## Problem Statement

Road lane markings provide important visual information for understanding road structure. Detecting lane markings manually from road images is time-consuming and difficult to scale.

This project develops a computer vision system that automatically identifies lane markings from a single road image. The system uses image preprocessing, edge detection, region-of-interest selection, and Hough Transform-based line detection.

## Scope

The project focuses on lane detection from static road images.

The system performs:

1. Image preprocessing
2. Grayscale conversion
3. Gaussian filtering
4. Canny edge detection
5. Region-of-interest extraction
6. Hough Transform-based line detection
7. Lane visualization

The project does not include real-time video processing, autonomous vehicle control, or hardware integration.

## Target Users

- Computer vision students
- Researchers learning image processing
- Students studying road-scene analysis
- Developers interested in basic driver-assistance concepts

## Major Functional Modules

### Module 1: Image Preprocessing

Converts the input image into grayscale and applies Gaussian filtering.

### Module 2: Edge and Region Detection

Uses Canny edge detection and a region-of-interest mask to identify relevant road boundaries.

### Module 3: Lane Detection and Visualization

Uses the Probabilistic Hough Transform to detect lane-related line segments and overlays the detected lanes on the original image.

## Input

A JPEG road image stored inside the input directory.

## Output

The system produces:

- Grayscale image
- Blurred image
- Canny edge image
- Region-of-interest image
- Lane-detected image
- Complete processing pipeline image