# gridslice
# command-line tool for slicing your images
# Copyright (C) 2018 jack01

import argparse, sys, os
from PIL import Image

pil_read_write_types = ('.png', '.tiff', '.tif', '.jpg', '.jpeg', '.gif', '.bmp', '.ico', '.webp')

def main():
    parser = argparse.ArgumentParser(description='Command line tool for slicing an image on a grid.',)
    parser.add_argument('input_image_path', help = 'Path to the input image file')
    parser.add_argument('start_x', type = int, help = 'Start x')
    parser.add_argument('start_y', type = int, help = 'Start y')
    parser.add_argument('width', type = int, help = 'Slice width')
    parser.add_argument('height', type = int, help = 'Slice height')
    parser.add_argument('slices_x', type = int, help = 'Number of x slices')
    parser.add_argument('slices_y', type = int, help = 'Number of y slices')

    args = parser.parse_args()

    if args.input_image_path.lower().endswith(pil_read_write_types) == False:
        print('error: the specified output image file is not in a supported format')
        sys.exit(1)

    try:
        image = Image.open(args.input_image_path)
    except:
        print('error: there was an error opening the image file')
        sys.exit(1)

    count = 0
    extension = os.path.splitext(args.input_image_path)[1]

    for y in range(args.start_y, args.start_y + args.height * (args.slices_y), args.height):
        for x in range(args.start_x, args.start_x + args.width * (args.slices_x), args.width):
            slice = image.crop((x, y, x + args.width, y + args.height))
            filename = os.path.splitext(args.input_image_path)[0] + " slice " + str(count)

            existing_count = 0
            while os.path.isfile(filename + extension):
                filename += "-" + str(existing_count)
                existing_count += 1

            try:
                slice.save(filename + extension, quality=100)
            except:
                print('error: there was an error saving the image file ' + filename + extension)
                sys.exit(1)

            count += 1
