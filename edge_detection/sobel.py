from PIL import Image, ImageFilter


def sobel_operator(image):
    # Convert the image to grayscale
    grayscale_image = image.convert("L")

    # Sobel operator kernels
    kernel_x = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
    kernel_y = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]

    # Get image size
    width, height = grayscale_image.size

    # Create a new image to store the result
    result_image = Image.new("L", (width, height))

    for y in range(1, height - 1):
        for x in range(1, width - 1):
            # Calculate the gradients
            gx = gy = 0
            for i in range(3):
                for j in range(3):
                    pixel_value = grayscale_image.getpixel(
                        (x + i - 1, y + j - 1))
                    gx += pixel_value * kernel_x[i][j]
                    gy += pixel_value * kernel_y[i][j]

            # Calculate the magnitude of the gradient
            gradient = int((gx**2 + gy**2)**0.5)

            # Ensure the gradient is in the valid range [0, 255]
            gradient = max(0, min(255, gradient))

            # Set the pixel in the result image
            result_image.putpixel((x, y), gradient)

    return result_image


def main():
    # Open the image using PIL
    input_image_path = "images/original_image.png"
    output_image_path = "images/sobel.png"

    original_image = Image.open(input_image_path)

    # Apply the Sobel operator
    sobel_image = sobel_operator(original_image)

    # Save the result
    sobel_image.save(output_image_path)
    print(f"Sobel operator applied. Result saved at: {output_image_path}")


if __name__ == "__main__":
    main()
