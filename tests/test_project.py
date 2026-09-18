import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import cv2

from src.preprocessing import (
    load_image,
    convert_to_grayscale,
    apply_gaussian_blur
)

from src.edge_detection import (
    canny_edge_detection,
    create_region_of_interest
)

from src.lane_detection import detect_lines


IMAGE_PATH = "input/road.jpeg"


def test_image_exists():
    assert os.path.exists(IMAGE_PATH)


def test_image_loading():
    image = load_image(IMAGE_PATH)

    assert image is not None
    assert len(image.shape) == 3


def test_grayscale_conversion():
    image = load_image(IMAGE_PATH)
    gray = convert_to_grayscale(image)

    assert len(gray.shape) == 2


def test_blur():
    image = load_image(IMAGE_PATH)
    gray = convert_to_grayscale(image)
    blur = apply_gaussian_blur(gray)

    assert blur.shape == gray.shape


def test_canny():
    image = load_image(IMAGE_PATH)
    gray = convert_to_grayscale(image)
    blur = apply_gaussian_blur(gray)
    edges = canny_edge_detection(blur)

    assert edges.shape == gray.shape


def test_roi():
    image = load_image(IMAGE_PATH)
    gray = convert_to_grayscale(image)
    blur = apply_gaussian_blur(gray)
    edges = canny_edge_detection(blur)

    roi, mask = create_region_of_interest(edges)

    assert roi.shape == edges.shape
    assert mask.shape == edges.shape


def test_hough_detection():
    image = load_image(IMAGE_PATH)
    gray = convert_to_grayscale(image)
    blur = apply_gaussian_blur(gray)
    edges = canny_edge_detection(blur)
    roi, mask = create_region_of_interest(edges)

    lines = detect_lines(roi)

    assert lines is None or len(lines) > 0