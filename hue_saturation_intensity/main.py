import math
from PIL import Image

HUE_VALUES = {
    "red": 0,
    "yellow": 60,
    "green": 120,
    "blue": 240,
}

INPUT_IMAGE_PATH = "images/cat.jpg"


class CustomHueImage:
    # initailize the class and set the image width and height
    def __init__(self, image):
        self.image = image
        self.width, self.height = image.size

    # get image pixels
    def get_pixel(self, x, y):
        return self.image.getpixel((x, y))

    # set image pixels
    def set_pixel(self, x, y, value):
        self.image.putpixel((x, y), value)

    # save the image with the given filename
    def save(self, filename):
        self.image.save(filename)


def rgb_to_hsi(rgb):
    # unpack the tuple
    r, g, b = rgb
    # scale the values to the range [0, 1]
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    # calculate the intensity by averaging the values
    intensity = (r + g + b) / 3.0

    # if red, green, and blue are all 0, then the image is a shade of gray
    # and the hue and saturation are both 0
    if r == g == b:
        hue = 0.0
        saturation = 0.0
    else:
        # component of the hue formula
        num = 0.5 * ((r - g) + (r - b))
        # denominator of the hue formula
        den = ((r - g) ** 2 + (r - b) * (g - b)) ** 0.5
        # clamp the value to the range [-1, 1] to avoid domain errors
        theta = min(max(num / den, -1.0), 1.0)
        hue = math.acos(theta)

        # calculate the hue in radians
        # if blue is the largest component, then the angle is between red and green
        if b > g:
            hue = 2.0 * math.pi - hue

        # calculate the saturation using the formula for saturation
        saturation = 1.0 - 3.0 * min(r, g, b) / (r + g + b)

    return hue, saturation, intensity


def hsi_to_rgb(hsi):
    # unpack the tuple to get the hue, saturation, and intensity
    hue, saturation, intensity = hsi

    # if saturation is 0, then the image is a shade of gray
    # and the hue doesn't matter
    if saturation == 0.0:
        r = g = b = intensity
    else:
        # h prime is the hue in degrees in range 0 to 6
        h_prime = hue * 6.0 / (2.0 * math.pi)
        # intensity is between 0 and 1, so c is between 0 and 1
        c = (1.0 - abs(2.0 * intensity - 1.0)) * saturation
        # intermediate value x for the formula
        x = c * (1.0 - abs(h_prime % 2.0 - 1.0))

        # depending on which range h prime is in, the RGB values are calculated differently
        if 0.0 <= h_prime < 1.0:
            r, g, b = c, x, 0.0
        elif 1.0 <= h_prime < 2.0:
            r, g, b = x, c, 0.0
        elif 2.0 <= h_prime < 3.0:
            r, g, b = 0.0, c, x
        elif 3.0 <= h_prime < 4.0:
            r, g, b = 0.0, x, c
        elif 4.0 <= h_prime < 5.0:
            r, g, b = x, 0.0, c
        else:
            r, g, b = c, 0.0, x

        # m is calculated using the formula for intensity and then added to each component
        m = intensity - 0.5 * c
        r, g, b = r + m, g + m, b + m

    # scale the values to the range [0, 255] and convert to integers
    r, g, b = int(r * 255), int(g * 255), int(b * 255)
    return r, g, b


def change_hue(image, delta_hue):
    """ Iterates over every pixel in the image and changes the hue by the given amount"""
    # iterate over height
    for y in range(image.height):
        # iterate over width
        for x in range(image.width):
            # Get the pixel value
            pixel = image.get_pixel(x, y)
            # Convert to HSI
            hue, saturation, intensity = rgb_to_hsi(pixel)

            # Change the hue by the given angle
            hue += delta_hue
            # Normalize the hue component to the range [0, 2pi]
            hue = hue % (2 * math.pi)

            # Convert back to RGB
            modified_pixel = hsi_to_rgb((hue, saturation, intensity))

            # Set the modified pixel
            image.set_pixel(x, y, modified_pixel)


for hue_name, hue_value in HUE_VALUES.items():
    image = Image.open(INPUT_IMAGE_PATH)
    custom_image = CustomHueImage(image)
    hue_value = math.radians(hue_value)
    change_hue(custom_image, hue_value)

    custom_image.save(f"images/cat_{hue_name}.jpg")
    print(f"Saved cat image for {hue_name}")
