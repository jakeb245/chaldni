"""Compare two images in binary format using mean-squared-error"""

import numpy as np
from skimage import io, color
from skimage.filters import threshold_mean
from sklearn.metrics import mean_squared_error
from skimage.restoration import denoise_tv_chambolle


def read_image(filename, denoise=False):
    raw = io.imread(filename)
    if denoise:
        raw = denoise_tv_chambolle(raw, weight=0.2, channel_axis=-1)
    try:
        rgb = color.rgba2rgb(raw)
    except:
        rgb = raw
    finally:
        gray = color.rgb2gray(rgb)
    thresh = threshold_mean(gray)
    bool_array = gray > thresh
    return bool_array * 1


def compare_images(exp_filename, theo_filename, denoise=True):
    exp = read_image(exp_filename, denoise=denoise)
    theo = read_image(theo_filename)

    error = mean_squared_error(exp, theo)

    return error


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


def add_figures(exp_filename, theo_filename):
    exp = read_image(exp_filename, denoise=True)
    theo = read_image(theo_filename)

    added = binary_to_transparent(exp) + binary_to_transparent(theo, color='yellow')

    return added