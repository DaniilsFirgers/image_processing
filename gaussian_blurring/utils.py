import math
from PIL import Image


def generate_gaussian_kernel(size: int, sigma: float) -> list[list[float]]:
    """
    Generates a Gaussian kernel of a given size and sigma
    """
    if not isinstance(size, int) or not isinstance(sigma, float):
        raise TypeError("Size must be an integer and sigma must be a float")

    kernel = [[0] * size for _ in range(size)]
    center = size // 2
    total = 0

    for i in range(size):
        for j in range(size):
            kernel[i][j] = (1/math.sqrt(2 * math.pi * sigma)) * \
                math.e ** (-((i - center) ** 2 + (j - center)
                           ** 2) / (2 * sigma ** 2))
            total += kernel[i][j]

    return [[element / total for element in row] for row in kernel]


def apply_gaussian_blur(image: Image, kernel: list[list[float]]) -> list[list[int]]:
    """
    Applies a Gaussian blur to an image
    """
    result = [[0 for _ in range(len(image[0]))] for _ in range(len(image))]
    k_size = len(kernel) // 2

    for i in range(k_size, len(image) - k_size):
        for j in range(k_size, len(image[0]) - k_size):
            pixel_sum = 0
            for x in range(len(kernel)):
                for y in range(len(kernel[0])):
                    pixel_sum += image[i + x - k_size][j +
                                                       y - k_size] * kernel[x][y]
            result[i][j] = int(pixel_sum)

    return result


def image_to_array(image):
    """
    Converts a PIL image to a 2D array
    """
    width, height = image.size
    pixel_values = []

    for y in range(height):
        row = []
        for x in range(width):
            pixel_value = image.getpixel((x, y))
            row.append(pixel_value)
        pixel_values.append(row)

    return pixel_values
