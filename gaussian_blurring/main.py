from utils import generate_gaussian_kernel, image_to_array, apply_gaussian_blur
from PIL import Image

KERNEL_SIZE = 3
SIGMA = 0.6


unbluured_image = Image.open("/app/images/cat.jpg")

converted_unblurred_image = unbluured_image.convert("L")

unblurred_image_array = image_to_array(converted_unblurred_image)

kernel = generate_gaussian_kernel(KERNEL_SIZE, SIGMA)

blurred_image_array = apply_gaussian_blur(unblurred_image_array, kernel)
print(blurred_image_array)
