import numpy as np
from PIL import Image
from utils import image_to_array

unequalized_image = Image.open("/app/images/Unequalized_Hawkes_Bay_NZ.jpg")

unequalized_image_grayscale = unequalized_image.convert("L")

unequalized_image_array = image_to_array(unequalized_image_grayscale)

print(unequalized_image_array)

print("Hello world!")
