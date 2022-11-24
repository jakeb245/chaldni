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
        for y in array[x]:
            long.append(y)
    return np.array(long)


def binary_to_transparent(image,color):
    new_image = []
    for x in range(len(image)):
        new_x = []
        for y in range(len(image[x])):
            if image[x][y]: # True is black
                if color == 'red':
                    new_y = [255, 0, 0, 0.5]
                elif color == 'blue':
                    new_y = [0, 0, 255, 0.5]
                else:
                    new_y = [255, 255, 255, 0.5]
            else:
                new_y = [0,0,0,0.5]
            new_x.append(np.array(new_y))
        new_image.append(np.array(new_x))
    return np.array(new_image)


if __name__ == '__main__':
    exp = rgba_to_binary(io.imread('MoreCleanedExp.png'))*1
    theo = rgb_to_binary(io.imread('Maybe.png'))*1

    exp_array = really_long_array(exp)
    theo_array = really_long_array(theo)
    exp_array = np.logical_not(theo_array).astype(int)
    print(exp_array)
    print(theo_array)

    print(mean_squared_error(exp, theo))
    print(mean_squared_error(exp_array, theo_array))
    print(mean_squared_error(theo_array, theo_array))

    exp_test = binary_to_transparent(exp,'red')
    theo_test = binary_to_transparent(theo,'blue')

    fig = plt.figure(dpi=200)
    plt.rcParams['figure.facecolor'] = 'black'
    plt.imshow(exp_test + theo_test)
    plt.axis('off')
    plt.savefig('AddedFigures.png',bbox_inches='tight', pad_inches=0)
