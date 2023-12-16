from PIL import Image


def laplacian_filter(image):
    # Convert the image to grayscale
    grayscale_image = image.convert("L")

    # Laplacian filter kernel
    kernel = [[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]

    # Get image size
    width, height = grayscale_image.size

    # Create a new image to store the result
    result_image = Image.new("L", (width, height))

    for y in range(1, height - 1):
        for x in range(1, width - 1):
            # Calculate the Laplacian filter value
            laplacian_value = sum(grayscale_image.getpixel(
                (x + i - 1, y + j - 1)) * kernel[i][j] for i in range(3) for j in range(3))

            # Ensure the value is in the valid range [0, 255]
            laplacian_value = max(0, min(255, laplacian_value))

            # Set the pixel in the result image
            result_image.putpixel((x, y), laplacian_value)

    return result_image


def main():
    # Open the image using PIL
    input_image_path = "images/original_image.png"
    output_image_path = "images/laplacian.png"

    original_image = Image.open(input_image_path)

    # Apply the Laplacian filter
    laplacian_image = laplacian_filter(original_image)

    # Save the result
    laplacian_image.save(output_image_path)
    print(f"Laplacian filter applied. Result saved at: {output_image_path}")


if __name__ == "__main__":
    main()
