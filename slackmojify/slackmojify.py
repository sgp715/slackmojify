import os
import argparse
import imageio
import slackmojify.images2gif
from math import floor
import imghdr
from PIL import Image, ImageSequence


MAX_DIMENSION = 128


def _determine_dimensions(ideal_dimensions, current_dimensions):
    """
    ideal_dimensions: dimensions we want an image to fit into (width, height)
    current_dimensions: the dimensions the image currently has (width, height)
    returns the dimensions the image should be resized to
    """

    current_width = current_dimensions[0]
    current_height = current_dimensions[1]

    ideal_width = ideal_dimensions[0]
    ideal_height = ideal_dimensions[1]

    width_diff = current_width - ideal_width
    height_diff = current_height - ideal_height

    if (width_diff <= 0) and (height_diff <= 0):
        return current_dimensions

    if width_diff > height_diff:
        return ideal_width, int((ideal_width / current_width) * current_height)
    else:
        return int((ideal_height / current_height) * current_width), ideal_height

def mini(image_path):
    """
    https://www.youtube.com/watch?v=--hsVknT1c0
    image: A pillow image object
    returns an image that is shrunk to fit within slacks constraints
    """
    img_type = imghdr.what(image_path)
    valid_types = ["jpeg", "png"]
    if img_type in valid_types:
        image = Image.open(image_path)
        new_dims = _determine_dimensions((MAX_DIMENSION, MAX_DIMENSION), image.size)
        return image.resize((new_dims))
    return None

def reduce_quality(image):
    pass

def mini_gif(directory):
    """
    directory: contains the images to include in gif
    compresses images in folder so they can be made into a gif
    """
    images = []
    subs = list(os.walk(directory))[0][2]
    check = False
    for image_path in subs:
        if check == False:
            check = True
            compressed_image = mini(os.path.join(directory, image_path))
        else:
            new_image = mini(os.path.join(directory, image_path))
            if new_image.size != compressed_image.size:
                return None
            compressed_image = new_image
        images.append(compressed_image)
    return images


def slackmojify(image_path, save_path="new_image"):
    """
    image_path: the path to the image that we want to compress
    this function takes the image and compresses it to a size that
    that is small enough to be uploaded as a custom emoji to Slack
    """
    if os.path.isfile(image_path):
        compressed = mini(image_path)
        compressed.save(save_path + os.path.splitext(image_path)[1])
    elif os.path.isdir(image_path):
        # assume it is a directory and we want to make a gif
        compressed = mini_gif(image_path)
        images2gif.writeGif(save_path + ".gif", compressed)
    else:
        print("Could not create compressed image.")
        raise

def main():
    parser = argparse.ArgumentParser(description="Make a file uploadable as a slackmoji.")
    parser.add_argument("image", metavar='I', type=str, nargs=1, help="path to the file to minimize")
    parser.add_argument("-s", "--save", type=str, nargs=1, help="specify the file to save the new image to")
    args = parser.parse_args()
    if args.save:
        slackmojify(args.image[0], args.save[0])
    else:
        slackmojify(args.image[0])

if __name__ == "__main__":
    main()
