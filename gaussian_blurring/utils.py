import math


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
