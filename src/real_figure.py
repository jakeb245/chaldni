"""
This code should take an image that contains a black square plate
on a white surface and isolate the plate. Then it should rotate the
image and scale it as necessary. Finally, it should convert the
image to binary format
"""

from skimage import io
import matplotlib.pyplot as plt


def isolate_plate(image):
    pass


if __name__ == '__main__':
    fname = "real_test.jpeg"
    raw_image = io.imread(fname)
