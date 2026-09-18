import cv2


def load_image(path):
    image = cv2.imread(path)

    if image is None:
        raise FileNotFoundError(f"Image not found: {path}")

    return image


def convert_to_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def apply_gaussian_blur(image, kernel_size=(5, 5)):
    return cv2.GaussianBlur(image, kernel_size, 0)