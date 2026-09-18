import os
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

from src.lane_detection import (
    detect_lines,
    draw_lane_lines,
    create_lane_overlay
)

from src.visualization import (
    create_pipeline_figure
)


INPUT_PATH = "input/road.jpeg"
OUTPUT_DIR = "output"


def save_image(path, image):
    cv2.imwrite(path, image)


def main():

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print("=" * 50)
    print("SINGLE IMAGE LANE DETECTION SYSTEM")
    print("=" * 50)

    image = load_image(INPUT_PATH)

    print("[1/6] Image loaded")

    grayscale = convert_to_grayscale(image)

    save_image(
        os.path.join(
            OUTPUT_DIR,
            "01_grayscale.jpg"
        ),
        grayscale
    )

    print("[2/6] Grayscale conversion completed")

    blurred = apply_gaussian_blur(grayscale)

    save_image(
        os.path.join(
            OUTPUT_DIR,
            "02_blurred.jpg"
        ),
        blurred
    )

    print("[3/6] Gaussian filtering completed")

    edges = canny_edge_detection(blurred)

    save_image(
        os.path.join(
            OUTPUT_DIR,
            "03_canny_edges.jpg"
        ),
        edges
    )

    print("[4/6] Canny edge detection completed")

    roi, mask = create_region_of_interest(edges)

    save_image(
        os.path.join(
            OUTPUT_DIR,
            "04_region_of_interest.jpg"
        ),
        roi
    )

    print("[5/6] Region of interest created")

    lines = detect_lines(roi)

    hough_result = draw_lane_lines(
        image,
        lines
    )

    final_result = create_lane_overlay(
        image,
        hough_result
    )

    save_image(
        os.path.join(
            OUTPUT_DIR,
            "05_lane_detected.jpg"
        ),
        final_result
    )

    print("[6/6] Lane detection completed")

    create_pipeline_figure(
        image,
        grayscale,
        edges,
        roi,
        hough_result,
        final_result,
        os.path.join(
            OUTPUT_DIR,
            "06_complete_pipeline.jpg"
        )
    )

    print()
    print("PROJECT COMPLETED SUCCESSFULLY")
    print()
    print("Generated files:")

    for filename in sorted(os.listdir(OUTPUT_DIR)):
        print(f"  - {filename}")

    print()
    print("Main result:")
    print("  output/05_lane_detected.jpg")

    print()
    print("Complete pipeline:")
    print("  output/06_complete_pipeline.jpg")

    print("=" * 50)


if __name__ == "__main__":
    main()