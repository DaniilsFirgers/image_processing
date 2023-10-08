from PIL import Image
import numpy as np


def image_to_array(file_path):
    image = Image.open(file_path).convert('L')  # Convert to grayscale
    return np.array(image)


def bilinear_scaling(image, new_height, new_width):
    height, width = image.shape
    x_ratio = new_width / width
    y_ratio = new_height / height

    new_image = np.zeros((new_height, new_width))

    for i in range(new_height):
        for j in range(new_width):
            x = int(j / x_ratio)
            y = int(i / y_ratio)

            x_diff = (j / x_ratio) - x
            y_diff = (i / y_ratio) - y

            A = image[y, x]
            B = image[y, x + 1] if x + 1 < width else 0
            C = image[y + 1, x] if y + 1 < height else 0
            D = image[y + 1, x + 1] if x + 1 < width and y + 1 < height else 0

            new_image[i, j] = A * (1 - x_diff) * (1 - y_diff) + B * x_diff * (
                1 - y_diff) + C * (1 - x_diff) * y_diff + D * x_diff * y_diff

    return new_image


def save_image(array, file_path):
    # Convert the NumPy array to an image
    image = Image.fromarray(array.astype('uint8'))

    # Save the image
    image.save(file_path)
