import numpy as np
from PIL import Image
from utils import image_to_array, get_intensity_frequency, get_cumulative_distribution, get_mapped_intensity_levels

unequalized_image = Image.open("/app/images/Unequalized_Hawkes_Bay_NZ.jpg")

unequalized_image_grayscale = unequalized_image.convert("L")

unequalized_image_array = image_to_array(unequalized_image_grayscale)

unequalized_image_frequency = get_intensity_frequency(unequalized_image_array)

cumulative_distribution = get_cumulative_distribution(
    unequalized_image_frequency)

mapped_intensity_levels = get_mapped_intensity_levels(cumulative_distribution)
equalized_image_array = [[mapped_intensity_levels[pixel]
                          for pixel in row] for row in unequalized_image_array]

equalized_image_array = np.array(equalized_image_array, dtype=np.uint8)
eq_img = Image.fromarray(equalized_image_array, mode='L')
eq_img.save("/app/images/Equalized_Hawkes_Bay_NZ.jpg")
