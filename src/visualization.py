import cv2
import matplotlib.pyplot as plt


def create_pipeline_figure(
    original,
    grayscale,
    edges,
    roi,
    hough_result,
    final_result,
    output_path
):
    fig, axes = plt.subplots(
        2,
        3,
        figsize=(15, 9)
    )

    axes[0, 0].imshow(
        cv2.cvtColor(original, cv2.COLOR_BGR2RGB)
    )
    axes[0, 0].set_title("Original Image")
    axes[0, 0].axis("off")

    axes[0, 1].imshow(
        grayscale,
        cmap="gray"
    )
    axes[0, 1].set_title("Grayscale")
    axes[0, 1].axis("off")

    axes[0, 2].imshow(
        edges,
        cmap="gray"
    )
    axes[0, 2].set_title("Canny Edge Detection")
    axes[0, 2].axis("off")

    axes[1, 0].imshow(
        roi,
        cmap="gray"
    )
    axes[1, 0].set_title("Region of Interest")
    axes[1, 0].axis("off")

    axes[1, 1].imshow(
        cv2.cvtColor(
            hough_result,
            cv2.COLOR_BGR2RGB
        )
    )
    axes[1, 1].set_title("Hough Transform")
    axes[1, 1].axis("off")

    axes[1, 2].imshow(
        cv2.cvtColor(
            final_result,
            cv2.COLOR_BGR2RGB
        )
    )
    axes[1, 2].set_title("Final Lane Detection")
    axes[1, 2].axis("off")

    plt.tight_layout()

    plt.savefig(
        output_path,
        dpi=200,
        bbox_inches="tight"
    )

    plt.close(fig)