import cv2
import numpy as np


def canny_edge_detection(image, low_threshold=50, high_threshold=150):
    return cv2.Canny(image, low_threshold, high_threshold)


def create_region_of_interest(edges):
    height, width = edges.shape

    mask = np.zeros_like(edges)

    polygon = np.array([
        [
            (0, height),
            (width, height),
            (int(width * 0.60), int(height * 0.55)),
            (int(width * 0.40), int(height * 0.55))
        ]
    ], dtype=np.int32)

    cv2.fillPoly(mask, polygon, 255)

    roi = cv2.bitwise_and(edges, mask)

    return roi, mask