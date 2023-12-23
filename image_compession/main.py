from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def dpcm_encode(image, compression_strength):
    # Get the height and width of the image
    height, width = image.shape
    # Initialize the encoded values list
    encoded = []

    # Initialize the predictor with the first pixel value
    # used to estimate tthe current sample based on the previous one
    predictor = image[0, 0]

    # Iterate over the image's rows and columns
    for row in range(height):
        for col in range(width):
            # Calculate the prediction error by subtracting the predictor from the actual pixel value
            # Represents how much the current prediction differs from the actual pixel value
            prediction_error = image[row, col] - predictor

            # Quantize the prediction error based on compression_strength
            # Reduces the precision of the prediction error
            # The quanitization aims to reduce the number of bits required to store the error
            quantized_error = int(
                round(np.clip(prediction_error / compression_strength, -255, 255)))

            # Update the predictor for the next sample in the sample
            predictor += quantized_error

            # Store the quantized error
            encoded.append(quantized_error)

    return encoded


def save_as_compressed_image(encoded_values, image_shape, compression_strength):
    encoded_array = np.array(encoded_values).reshape(image_shape)

    compressed_image = Image.fromarray(encoded_array.astype(np.uint8))

    compressed_image.save(f'images/compressed-{compression_strength}-cat.jpg')


image_path = 'images/cat.jpg'
# open image as grayscale
original_image = Image.open(image_path).convert('L')
original_array = np.array(original_image)

# define the compression strengths
compression_strengths = [1, 2, 4, 8, 16]
for comperssion in compression_strengths:
    encoded_values = dpcm_encode(original_array, comperssion)

    save_as_compressed_image(encoded_values, original_array.shape, comperssion)
