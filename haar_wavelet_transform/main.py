from PIL import Image
import numpy as np


def haar_wavelet_transform(matrix):
    # Get the number of rows and columns
    rows, cols = matrix.shape
    # Initialize the transformed matrix
    transformed_matrix = matrix.copy()

    # Iterate over the half of the rows
    for i in range(rows // 2):
        # Iterate over the half of the columns
        for j in range(cols // 2):
            # average of the four positions
            # averasge represents the low frequency or approximation coefficients
            avg = (matrix[2*i, 2*j] + matrix[2*i, 2*j+1] +
                   matrix[2*i+1, 2*j] + matrix[2*i+1, 2*j+1]) / 4.0
            # difference between the four positions
            # This represents the high frequency or detail coefficients
            diff = (matrix[2*i, 2*j] - matrix[2*i, 2*j+1] -
                    matrix[2*i+1, 2*j] + matrix[2*i+1, 2*j+1]) / 4.0

            # top left quadrant of the transformed matrix contains the average values
            # approximation coefficients
            transformed_matrix[i, j] = avg

            # top right quadrant of the transformed matrix contains the difference values
            # The detail coefficients correspond to changes in the columns
            transformed_matrix[i, j + cols // 2] = diff

            # bottom left quadrant of the transformed matrix contains the difference values
            # The detail coefficients correspond to changes in the rows
            transformed_matrix[i + rows // 2, j] = (
                matrix[2*i, 2*j] - matrix[2*i, 2*j+1] + matrix[2*i+1, 2*j] - matrix[2*i+1, 2*j+1]) / 4.0

            # bottom right quadrant of the transformed matrix contains the difference values
            # The detail coefficients correspond to changes in the rows and columns
            transformed_matrix[i + rows // 2, j + cols // 2] = (
                matrix[2*i, 2*j] + matrix[2*i, 2*j+1] - matrix[2*i+1, 2*j] - matrix[2*i+1, 2*j+1]) / 4.0

    return transformed_matrix


def apply_haar_wavelet(image_path, output_path):
    # Read the image using PIL
    original_image = Image.open(image_path).convert(
        'L')  # Convert to grayscale
    original_matrix = np.array(original_image, dtype=float)

    # Apply Haar wavelet transform
    transformed_matrix = haar_wavelet_transform(original_matrix)

    # Normalize values to the range [0, 255] for visualization purposes
    transformed_matrix = np.clip(transformed_matrix, 0, 255)
    transformed_matrix -= np.min(transformed_matrix)
    transformed_matrix /= np.max(transformed_matrix) / 255.0

    # Save the transformed image
    transformed_image = Image.fromarray(transformed_matrix.astype(np.uint8))
    transformed_image.save(output_path)


if __name__ == "__main__":
    input_image_path = "/app/images/grayscale.jpg"
    output_image_path = "/app/images/output.jpg"

    apply_haar_wavelet(input_image_path, output_image_path)
