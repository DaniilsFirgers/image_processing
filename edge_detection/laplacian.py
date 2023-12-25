from PIL import Image


def laplacian_filter(image):
    # Convert the image to grayscale using the Luma formula
    grayscale_image = image.convert("L")

    # Laplacian 3x3 filter kernel which is applied to every pixel of the image
    # The center pixel has the value 8, the surrounding pixels have the value -1, which are weights
    # 8 emphasizes high frequency changes in intensity, -1 emphasizes rapid changes in intensity
    kernel = [[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]

    # Get image width and height
    width, height = grayscale_image.size

    # Create a new image of the same width and height to store the converted image
    result_image = Image.new("L", (width, height))

    # Apply the Laplacian filter to each pixel of of vertical and horizontal neighbors
    # -1 means that the pixel is on the edge of the image and has no neighbor, so it is ignored
    for y in range(1, height - 1):
        for x in range(1, width - 1):
            # For each pixel thhe value is calculated by summing the product of the pixel values
            # and corresponding kernel values within the 3x3 neighborhood
            # grayscale_image.getpixel((x + i - 1, y + j - 1)) retreives the pixel intensity value at a coordinate
            # kernel[i][j] retreives the corresponding kernel value
            # for i in range(3) for j in range(3) - this is a nested loop that iterates over the 3x3 Laplacian kernel
            # overall it computes the sum of the weighted pixel values, representing the convolution operation
            laplacian_value = sum(grayscale_image.getpixel(
                (x + i - 1, y + j - 1)) * kernel[i][j] for i in range(3) for j in range(3))

            # Then value is scaled to the range [0, 255]
            laplacian_value = max(0, min(255, laplacian_value))

            # Then we set the pixel in the result image
            result_image.putpixel((x, y), laplacian_value)

    return result_image
