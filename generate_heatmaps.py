import os

from PIL import Image, ImageDraw

from ptable_trends import ptable_plotter

# row [87-118] are highjacked for custom values:
#   ph, alk, cond, hard, doc, chl-a, s04
# example usage:
#   ptable_plotter(filename="AOSTRA_KM9_median.csv", extended=False, cmap="inferno", data_override=True)


def draw_rectangle(input_path, output_path, x, y, width, height):
    image = Image.open(input_path)
    image = image.convert("RGBA")
    draw = ImageDraw.Draw(image)

    rectangle_color = (255, 255, 255, 255)
    draw.rectangle([x, y, x + width, y + height], fill=rectangle_color)

    image.save(output_path, "PNG")
    print("modified: " + output_path)


def generate_images(input_folder, override):
    # create images folder
    output_folder = input_folder + "images/"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    # enumerate csv files
    for filename in os.listdir(input_folder):
        if filename.endswith(".csv"):
            input_path = os.path.join(input_folder, filename)
            image_name = filename.split(".")[0] + ".png"
            output_path = os.path.join(output_folder, image_name)
            print("processing: " + input_path + " >>> " + image_name)

            # generate PNG from CSV file
            ptable_plotter(filename=input_path, extended=False, cmap="coolwarm", output_filename=output_path, data_override=override)

            # draw rectangle to blank out unused elements at end of highjacked row
            if override:
                draw_rectangle(output_path, output_path, 380, 500, 582, 100)


current_directory = os.getcwd()
# NOTE: we process tadpole data set before water data here because override will
# leave source element values overwritten for subsequent non override calls
# todo: fix so state isn't modified between calls to ptable_plotter() function
generate_images(current_directory + "/tadpole_data/", False)
generate_images(current_directory + "/water_data/", True)
# eg now calls with override=False will have previously injected values
# generate_images(current_directory + "/tadpole_data/", False) <-