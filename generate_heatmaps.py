import os

from PIL import Image, ImageDraw

from ptable_trends import ptable_plotter

# row [87-118] are highjacked for custom values (so4, ph, conductivity, etc)
# ptable_plotter(filename="AOSTRA_KM9_median.csv", extended=False, cmap="inferno")


def draw_rectangle(input_path, output_path, x, y, width, height):
    image = Image.open(input_path)
    image = image.convert("RGBA")
    draw = ImageDraw.Draw(image)

    rectangle_color = (255, 255, 255, 255)
    draw.rectangle([x, y, x + width, y + height], fill=rectangle_color)

    image.save(output_path, "PNG")
    print("modified: " + output_path)


current_directory = os.getcwd()
input_folder = current_directory + "/data/"

# create images folder
output_folder = input_folder + "images/"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    if filename.endswith(".csv"):
        input_path = os.path.join(input_folder, filename)
        image_name = filename.split(".")[0] + ".png"
        output_path = os.path.join(output_folder, image_name)
        print("processing: " + input_path + " >>> " + image_name)
        
        # generate PNG from CSV file
        ptable_plotter(filename=input_path, extended=False, cmap="inferno", output_filename=output_path)

        # draw rectangle to blank out unused elements at end of highjacked row
        draw_rectangle(output_path, output_path, 380, 500, 582, 100)
