from utils import image_to_array, bilinear_scaling, save_image

# Bilinear scaling is a great choice when desired output
# dimension is no more than double or half its original size.
NEW_WIDTH = 800
NEW_HEIGHT = 900

image_array = image_to_array("/app/images/gray_scale_doggo.jpg")
scaled_image = bilinear_scaling(image_array, NEW_WIDTH, NEW_HEIGHT)
image_name = f"scaled_doggo_{NEW_WIDTH}x{NEW_HEIGHT}.jpg"
save_image(scaled_image, f"/app/images/{image_name}")
