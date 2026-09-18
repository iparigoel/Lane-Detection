import cv2
import numpy as np


def detect_lines(roi):
    return cv2.HoughLinesP(
        roi,
        rho=1,
        theta=np.pi / 180,
        threshold=30,
        minLineLength=30,
        maxLineGap=60
    )


def classify_lines(lines, image_shape):
    if lines is None:
        return [], []

    height, width = image_shape[:2]

    left_lines = []
    right_lines = []

    for line in lines:
        x1, y1, x2, y2 = line[0]

        if x2 == x1:
            continue

        slope = (y2 - y1) / (x2 - x1)

        if abs(slope) < 0.4 or abs(slope) > 4:
            continue

        length = np.sqrt(
            (x2 - x1) ** 2 +
            (y2 - y1) ** 2
        )

        intercept = y1 - slope * x1

        if slope < 0:
            left_lines.append((slope, intercept, length))
        else:
            right_lines.append((slope, intercept, length))

    left_lines.sort(key=lambda x: x[2], reverse=True)
    right_lines.sort(key=lambda x: x[2], reverse=True)

    return left_lines[:5], right_lines[:5]


def average_line(lines, image_shape):
    if not lines:
        return None

    height, width = image_shape[:2]

    total_length = sum(line[2] for line in lines)

    slope = sum(
        line[0] * line[2] for line in lines
    ) / total_length

    intercept = sum(
        line[1] * line[2] for line in lines
    ) / total_length

    y1 = height
    y2 = int(height * 0.55)

    x1 = int((y1 - intercept) / slope)
    x2 = int((y2 - intercept) / slope)

    x1 = max(0, min(width - 1, x1))
    x2 = max(0, min(width - 1, x2))

    return x1, y1, x2, y2


def draw_lane_lines(image, lines):
    result = image.copy()

    left_lines, right_lines = classify_lines(
        lines,
        image.shape
    )

    left = average_line(
        left_lines,
        image.shape
    )

    right = average_line(
        right_lines,
        image.shape
    )

    if left is not None:
        x1, y1, x2, y2 = left

        cv2.line(
            result,
            (x1, y1),
            (x2, y2),
            (0, 255, 0),
            6
        )

    if right is not None:
        x1, y1, x2, y2 = right

        cv2.line(
            result,
            (x1, y1),
            (x2, y2),
            (0, 255, 0),
            6
        )

    return result


def create_lane_overlay(image, lane_image):
    return cv2.addWeighted(
        image,
        0.8,
        lane_image,
        1.0,
        0
    )