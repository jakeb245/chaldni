"""
Get figure from image???
"""

from skimage import io
from skimage import color
from skimage.restoration import denoise_tv_chambolle, estimate_sigma
import matplotlib.pyplot as plt


def figure_from_image(image_filename):
    raw_image = io.imread(image_filename)

    if raw_image.shape[0] == 4:
        rgb_image = color.rgba2rgb(raw_image)
        gray_image = color.rgb2gray(rgb_image)
    elif raw_image.shape[0] == 3:
        rgb_image = raw_image
        gray_image = color.rgb2gray(rgb_image)
        # TODO: invert colors on theoretical figure
    else:
        gray_image = raw_image

    sig_est = estimate_sigma(gray_image)
    print(f'Estimated sigma of {image_filename} = {sig_est}')

    denoise = denoise_tv_chambolle(gray_image, weight=0.2)
    sig_est_denoise = estimate_sigma(denoise)
    print(f'Estimated sigma after denoise = {sig_est_denoise}')

    return denoise


def scale_image(image1, image2):
    pass


def compare_images(image1, image2):
    pass


if __name__ == '__main__':
    exp_filename = 'Subject.png'
    th_filename = 'LineCountour.png'

    exp = figure_from_image(exp_filename)
    theo = figure_from_image(th_filename)

    fig = plt.figure(0)
    plt.imshow(exp)

    fig = plt.figure(1)
    plt.imshow(theo)

    plt.show()
