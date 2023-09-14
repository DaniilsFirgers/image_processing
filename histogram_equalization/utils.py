def image_to_array(image):
    width, height = image.size
    pixel_values = []

    for y in range(height):
        row = []
        for x in range(width):
            pixel_value = image.getpixel((x, y))
            row.append(pixel_value)
        pixel_values.append(row)

    return pixel_values


def get_intensity_frequency(image_array):
    frequency_counts = [0] * 256
    for row in image_array:
        for intensity in row:
            frequency_counts[intensity] += 1
    return frequency_counts


def get_cumulative_distribution(frequency_counts: list[int]):
    cdf = [0] * 256
    for i in range(256):
        if i == 0:
            cdf[i] = frequency_counts[i]
        else:
            cdf[i] = cdf[i - 1] + frequency_counts[i]

    total_pixels = sum(frequency_counts)
    normalized_cdf = [cdf[i] / total_pixels for i in range(256)]
    return normalized_cdf


def get_mapped_intensity_levels(normalized_cdf: list[float]):
    mapped_intesity_levels = [round(cdf_value * 255)
                              for cdf_value in normalized_cdf]
    return mapped_intesity_levels
