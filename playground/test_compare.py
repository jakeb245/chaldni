"""
Test comparing images
"""

import numpy as np
import matplotlib.pyplot as plt
from skimage import io, color
from skimage.filters import threshold_mean
from sklearn.metrics import mean_squared_error
from skimage.transform import rescale


def rgba_to_binary(image):
    rgb = color.rgba2rgb(image)
    gray = color.rgb2gray(rgb)
    thresh = threshold_mean(gray)
    return gray > thresh


def rgb_to_binary(image):
    gray = color.rgb2gray(image)
    thresh = threshold_mean(gray)
    return gray > thresh


def really_long_array(array):
    long = []
    for x in range(len(array)):
        long.append(array[x])
    return np.array(long)


def binary_to_transparent(image):
    new_image = []
    for x in range(len(image)):
        new_x = []
        for y in range(len(image[x])):
            if image[x][y]: # True is black
                new_y = [255, 255, 255, 0.5]
            else:
                new_y = [0,0,0,0.5]
            new_x.append(np.array(new_y))
        new_image.append(np.array(new_x))
    return np.array(new_image)


if __name__ == '__main__':
    exp = rgba_to_binary(io.imread('MoreCleanedExp.png'))*1
    theo = rgb_to_binary(io.imread('LineContour.png'))*1

    exp_array = really_long_array(exp)
    theo_array = really_long_array(theo)

    print(mean_squared_error(exp, theo))
    print(mean_squared_error(theo_array, exp_array))

    exp_test = binary_to_transparent(exp)
    theo_test = binary_to_transparent(theo)

    fig = plt.figure()
    plt.rcParams['figure.facecolor'] = 'black'
    plt.imshow(exp_test + theo_test)
    plt.savefig('AddedFigures.png')
