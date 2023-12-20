from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def dpcm_encode(image):
    height, width = image.shape
    encoded = []

    # Initialize the predictor with the first pixel value
    predictor = image[0, 0]

    for row in range(height):
        for col in range(width):
            # Calculate the prediction error
            prediction_error = image[row, col] - predictor

            # Quantize the prediction error (in this case, using a simple threshold)
            quantized_error = 1 if prediction_error >= 0 else -1

            # Update the predictor for the next pixel
            predictor += quantized_error

            # Store the quantized error
            encoded.append(quantized_error)

    return encoded


def dpcm_decode(encoded, original_shape):
    height, width = original_shape
    decoded = np.zeros((height, width), dtype=np.uint8)

    # Initialize the predictor with the first pixel value
    predictor = 0

    for row in range(height):
        for col in range(width):
            # Retrieve the quantized error
            quantized_error = encoded[row * width + col]

            # Update the predictor for the next pixel
            predictor += quantized_error

            # Reconstruct the pixel value and clip it to the valid range [0, 255]
            decoded[row, col] = np.clip(predictor, 0, 255)

    return decoded


image_path = 'images/cat.jpg'
original_image = Image.open(image_path).convert('L')  # Convert to grayscale
original_array = np.array(original_image)

# Encode the image using DPCM
encoded_values = dpcm_encode(original_array)

# Decode the encoded values
decoded_image_array = dpcm_decode(encoded_values, original_array.shape)

# Convert NumPy arrays to PIL Images
original_pil_image = Image.fromarray(original_array)
decoded_pil_image = Image.fromarray(decoded_image_array)

decoded_pil_image.save('images/decoded_image.jpg')
