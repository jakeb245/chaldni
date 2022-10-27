"""
Get figure from image???
"""

from skimage import io
from skimage import color
from skimage import util
from skimage.restoration import denoise_tv_chambolle, estimate_sigma
from skimage.filters import threshold_mean
from skimage.transform import rotate
import numpy as np
import matplotlib.pyplot as plt


def figure_from_image(image_filename):
    raw_image = io.imread(image_filename)
    rgb_image = color.rgba2rgb(raw_image)
    gray_image = color.rgb2gray(rgb_image)
    sig_est = estimate_sigma(gray_image)
    print(f'Estimated sigma of {image_filename} = {sig_est}')
    #denoise = denoise_tv_chambolle(gray_image, weight=0.2)
    #sig_est_denoise = estimate_sigma(denoise)
    #print(f'Estimated sigma after denoise = {sig_est_denoise}')
    #thresh = threshold_mean(denoise)
    thres = threshold_mean(gray_image)
    #binary= denoise > thresh
    binary = gray_image > thres
    return binary


def slope(x1, x2, y1, y2):
    return (y2 - y1) / (x2 - x1)


def get_angle(image):
    # Get 1st corner (i.e. find first True)
    x_line = []
    y_line = []
    x_len = len(image)
    y_len = len(image[0])
    for x in range(x_len):
        for y in range(y_len):
            if not image[x,y]:
                print(f"First point at (x,y) = {x},{y}")
                x_line.append(x)
                y_line.append(y)
                break

    dx = x_line[int(2*x_len/3)] - x_line[int(x_len/3)]
    dy = y_line[int(2*y_len/3)] - y_line[int(y_len/3)]
    return np.degrees(np.arctan(dy/dx))


def scale_image(image1, image2):
    pass


def compare_images(image1, image2):
    pass


if __name__ == '__main__':
    exp_filename = 'Subject.png'
    th_filename = 'LineContour.png'

    exp = figure_from_image(exp_filename)
    angle = get_angle(exp)
    print(angle)
    exp2 = rotate(exp, -angle)

    # theo = figure_from_image(th_filename)

    fig = plt.figure(figsize=[7.2,7.2],dpi=200,frameon=False)
    plt.imshow(exp2, cmap=plt.cm.gray)
    plt.axis('off')
    plt.savefig('CleanedExp.png',pad_inches=0, bbox_inches='tight')
