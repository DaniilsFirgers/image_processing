from laplacian import laplacian_filter
from sobel import sobel_operator
from PIL import Image


def main():
    input_image_path = "/app/images/original_image.png"
    sobel_output_image_path = "/app/images/sobel.png"
    laplacian_output_image_path = "/app/images/laplacian.png"
    original_image = Image.open(input_image_path)

    sobel_image = sobel_operator(original_image)

    sobel_image.save(sobel_output_image_path)
    print(
        f"Sobel operator applied. Result saved at: {sobel_output_image_path}")

    laplacian_image = laplacian_filter(original_image)

    laplacian_image.save(laplacian_output_image_path)
    print(
        f"Laplacian filter applied. Result saved at: {laplacian_output_image_path}")


if __name__ == "__main__":
    main()
