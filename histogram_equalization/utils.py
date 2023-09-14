def image_to_array(image):
    width, height = image.size
    pixel_values = []

    for y in range(height):
        for x in range(width):
            pixel_value = image.getpixel((x, y))
            pixel_values.append(pixel_value)

    return pixel_values
