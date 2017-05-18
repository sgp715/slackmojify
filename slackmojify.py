#!/usr/bin/python3

import argparse
import imghdr
from PIL import Image
from shrink import mini


def slackmojify(image_path, save_path="new_image"):
    """
    image_path: the path to the image that we want to compress
    this function takes the image and compresses it to a size that
    that is small enough to be uploaded as a custom emoji to Slack
    """
    img_type = imghdr.what(image_path)
    valid_types = ["jpeg", "png"] #, "gif"]
    if img_type in valid_types:
        image = Image.open(image_path)
        resized_image = mini(image)
        resized_image.save(save_path + '.' + img_type)
    else:
        print("Not a valid filetype.")

    # print("File already satisfies slackmoji requirements.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Make a file uploadable as a slackmoji.")
    parser.add_argument("image", metavar='I', type=str, nargs=1, help="path to the file to minimize")
    parser.add_argument("-s", "--save", type=str, nargs=1, help="specify the file to save the new image to")
    args = parser.parse_args()
    if args.save:
        slackmojify(args.image[0], args.save[0])
    else:
        slackmojify(args.image[0])
