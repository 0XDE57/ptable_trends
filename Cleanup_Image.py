import os

from PIL import Image, ImageDraw


def draw_transparent_rectangle(input_path, output_path, x, y, width, height):
    image = Image.open(input_path)
    image = image.convert("RGBA")

    draw = ImageDraw.Draw(image)

    # Create a transparent rectangle
    rectangle_color = (0, 0, 0, 0)
    draw.rectangle([x, y, x + width, y + height], fill=rectangle_color)

    image.save(output_path, "PNG")
    print("save as: " + output_path)


input_folder = "/home/<user>/Desktop/heatmaps/"
output_folder = "/home/<user>/Desktop/heatmaps2/"
x = 380  # X coordinate of the top-left corner of the rectangle
y = 380  # Y coordinate of the top-left corner of the rectangle
width = 582  # Width of the rectangle
height = 100  # Height of the rectangle

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Iterate over PNG files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".png"):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)
        # print(input_path + " -> " + output_path)
        draw_transparent_rectangle(input_path, output_path, x, y, width, height)
