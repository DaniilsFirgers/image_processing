from PIL import Image
import numpy as np
import math


def dft2d(x):
    M, N = x.shape
    X = np.zeros((M, N), dtype=np.complex128)

    for u in range(M):
        print(u)
        for v in range(N):
            for m in range(M):
                for n in range(N):
                    X[u, v] += x[m, n] * (math.cos(2 * math.pi * (u * m / M + v * n / N))
                                          - 1j * math.sin(2 * math.pi * (u * m / M + v * n / N)))

    return X


def inverse_dft2d(X):
    M, N = X.shape
    x = np.zeros((M, N), dtype=np.float64)

    for m in range(M):
        for n in range(N):
            for u in range(M):
                for v in range(N):
                    x[m, n] += X[u, v] * (math.cos(2 * math.pi * (u * m / M + v * n / N))
                                          + 1j * math.sin(2 * math.pi * (u * m / M + v * n / N)))

    return np.abs(x) / (M * N)  # Convert back to real values and normalize


# Load a grayscale image
image = Image.open('/app/images/grayscale.jpg').convert('L')
image_array = np.array(image)

# Apply 2D Fourier Transform
X = dft2d(image_array)
print(X)

# Perform inverse transform
reconstructed_image_array = inverse_dft2d(X)

# Convert the result back to image format
reconstructed_image = Image.fromarray(
    reconstructed_image_array.astype('uint8'))

# Display or save the images
image.show()
reconstructed_image.show()
