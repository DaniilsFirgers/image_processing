from PIL import Image


def sobel_operator(image):
    # Convert the image to grayscale using the Luma formula
    grayscale_image = image.convert("L")

    # Sobel operator kernels
    # Operator for hotizontal gradient to detect chnages in intensity from left to right
    # [0, 0, 0] represents the center pixel of interest, while the surrounding rows contribute
    # to detecting the change in intensity
    kernel_x = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
    # Operator for vertical gradient to detect changes in intensity from top to bottom
    # [0, 0, 0] represents the center pixel of interest, while the surrounding columns contribute
    # to detecting the change in intensity
    kernel_y = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]

    # Get image width and height
    width, height = grayscale_image.size

    # Create a new image to store the result
    result_image = Image.new("L", (width, height))

 # Apply the Laplacian filter to each pixel of of vertical and horizontal neighbors
    # -1 means that the pixel is on the edge of the image and has no neighbor, so it is ignored
    for y in range(1, height - 1):
        for x in range(1, width - 1):
            # Initialize variables thta will store the cumulative sum of
            # the pizel values weighted by the corresponding kernel values
            gx = gy = 0
            # Iterate over the 3x3 neighborhood
            for i in range(3):
                for j in range(3):
                    # Retrives the intensity value of the pixel at the given coordinates
                    # -1 is adjusted to account for the fact that the kernel is 3x3
                    pixel_value = grayscale_image.getpixel(
                        (x + i - 1, y + j - 1))
                    # Updates the cumulative sum of the weighted pixel values
                    gx += pixel_value * kernel_x[i][j]
                    gy += pixel_value * kernel_y[i][j]

            # Calculate the Euclidean distance between the horizontal and vertical gradients
            # This distance represents the intensity of the gradient at the pixel
            gradient = int((gx**2 + gy**2)**0.5)

            # Ensure the gradient is in the valid range [0, 255]
            gradient = max(0, min(255, gradient))

            # Set the pixel in the result image
            result_image.putpixel((x, y), gradient)

    return result_image
