from PIL import Image
import numpy as np


def image_to_array(file_path: str):
    """Converts a PIL image to a 2D array"""
    image = Image.open(file_path).convert('L')  # Convert to grayscale
    return np.array(image)


def bilinear_scaling(image, new_height: int, new_width: int):
    """Scales an image using bilinear interpolation"""
    height, width = image.shape
    # Calculate the ratio between the new and old image width and height
    x_ratio = new_width / width
    y_ratio = new_height / height

    # Create an empty array for the scaled image
    scaled_image = np.zeros((new_height, new_width))

    # Iterate over the new image pixels
    for i in range(new_height):
        for j in range(new_width):
            # width
            w = int(j / x_ratio)
            # height
            h = int(i / y_ratio)
            # difference between the new and old pixel coordinates
            w_diff = (j / x_ratio) - w
            h_diff = (i / y_ratio) - h

            A = image[h, w]
            # checks if pixel to the right exists
            B = image[h, w + 1] if w + 1 < width else 0
            # checks if pixel below exists
            C = image[h + 1, w] if h + 1 < height else 0
            # checks if pixel to the right and below exists
            D = image[h + 1, w + 1] if w + 1 < width and h + 1 < height else 0

            # linear interpolation equation Y = A(1-w)(1-h) + B(w)(1-h) + C(h)(1-w) + Dwh
            scaled_image[i, j] = A * (1 - w_diff) * (1 - h_diff) + B * w_diff * (
                1 - h_diff) + C * (1 - w_diff) * h_diff + D * w_diff * h_diff

    return scaled_image


def save_image(array, file_path):
    # Convert the NumPy array to an image
    image = Image.fromarray(array.astype('uint8'))

    # Save the image to disk
    image.save(file_path)
