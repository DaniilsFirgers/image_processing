from utils import generate_gaussian_kernel, image_to_array, apply_gaussian_blur
from PIL import Image
import numpy as np

KERNEL_SIZE = 7  # higher kernel size means more blur
SIGMA = 11.0  # higher sigma means more blur

COMBINATIONS = [
    {'kernel_size': 3, 'sigma': 1.0},
    {'kernel_size': 5, 'sigma': 3.0},
    {'kernel_size': 7, 'sigma': 5.0},
    {'kernel_size': 9, 'sigma': 7.0},
]

UNBLURRED_IMAGE = Image.open("/app/images/cat.jpg")


for combination in COMBINATIONS:
    try:
        converted_unblurred_image = UNBLURRED_IMAGE.convert("L")

        unblurred_image_array = image_to_array(converted_unblurred_image)

        kernel = generate_gaussian_kernel(
            combination['kernel_size'], combination['sigma'])

        blurred_image_array = apply_gaussian_blur(
            unblurred_image_array, kernel)

        blurred_image_array = np.array(blurred_image_array, dtype=np.uint8)

        eq_img = Image.fromarray(blurred_image_array, mode='L')
        file_path = f"/app/images/blurred-cat-kernel-{combination['kernel_size']}-sigma-{combination['sigma']}.jpg"
        eq_img.save(file_path)
        print(f"Saved image to {file_path}")
    except Exception as e:
        print("Ooops", e)
