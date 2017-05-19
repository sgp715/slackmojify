import unittest
from math import floor
import os
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


class Tests(unittest.TestCase):

    def test_determine_dimensions(self):

        actual = determine_dimensions((64, 64), (64, 64))
        expected = (64, 64)
        self.assertEqual(actual, expected)

        actual = determine_dimensions((64, 64), (128, 128))
        expected = (64, 64)
        self.assertEqual(actual, expected)

        actual = determine_dimensions((64, 64), (128, 64))
        expected = (64, 32)
        self.assertEqual(actual, expected)

        actual = determine_dimensions((64, 32), (128, 64))
        expected = (64, 32)
        self.assertEqual(actual, expected)


if __name__ == "__main__":

    unittest.main()
