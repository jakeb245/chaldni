"""
Test comparing images
"""

import numpy as np
import matplotlib.pyplot as plt
from skimage import io, color
from skimage.filters import threshold_mean
from skimage.restoration import denoise_tv_chambolle
from sklearn.metrics import mean_squared_error


def rgba_to_binary(image):
    # rgb = color.rgba2rgb(image)
    gray = color.rgb2gray(image)
    thresh = threshold_mean(gray)
    return gray > thresh


def rgb_to_binary(image):
    gray = color.rgb2gray(image)
    thresh = threshold_mean(gray)
    return gray > thresh


def binary_to_transparent(image, color=None):
    new_image = []
    for x in range(len(image)):
        new_x = []
        for y in range(len(image[x])):
            if image[x][y]:  # True is black
                if color == 'red':
                    new_y = [255, 0, 0, 0.5]
                elif color == 'blue':
                    new_y = [0, 0, 255, 0.5]
                elif color == 'yellow':
                    new_y = [255, 255, 0, 0.5]
                else:
                    new_y = [255, 255, 255, 0.5]
            else:
                new_y = [0,0,0,0.5]
            new_x.append(np.array(new_y))
        new_image.append(np.array(new_x))
    return np.array(new_image)


if __name__ == '__main__':
    exp_raw = io.imread('../data/figure_965..png')
    exp = rgba_to_binary(denoise_tv_chambolle(exp_raw, weight=0.2, channel_axis=-1))*1
    theo = rgb_to_binary(io.imread('TheoProto.png'))*1

    print(mean_squared_error(exp, theo))

    exp_test = binary_to_transparent(exp)
    theo_test = binary_to_transparent(theo, 'yellow')

    fig = plt.figure(dpi=200)
    plt.rcParams['figure.facecolor'] = 'black'
    plt.imshow(exp_test + theo_test)
    plt.axis('off')
    plt.savefig('AddedFigures.png', bbox_inches='tight', pad_inches=0)
