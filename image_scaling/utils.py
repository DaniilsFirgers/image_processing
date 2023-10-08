from PIL import Image
import numpy as np


def image_to_array(file_path):
    image = Image.open(file_path).convert('L')  # Convert to grayscale
    return np.array(image)
