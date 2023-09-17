from utils import generate_gaussian_kernel

KERNEL_SIZE = 3
SIGMA = 0.6

kernel = generate_gaussian_kernel(KERNEL_SIZE, SIGMA)
print(kernel)
