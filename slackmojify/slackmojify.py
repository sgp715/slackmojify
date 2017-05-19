#!/usr/bin/python3

import argparse
from shrink import mini, mini_gif
import os
import imageio
from images2gif import images2gif


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


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Make a file uploadable as a slackmoji.")
    parser.add_argument("image", metavar='I', type=str, nargs=1, help="path to the file to minimize")
    parser.add_argument("-s", "--save", type=str, nargs=1, help="specify the file to save the new image to")
    args = parser.parse_args()
    if args.save:
        slackmojify(args.image[0], args.save[0])
    else:
        slackmojify(args.image[0])
