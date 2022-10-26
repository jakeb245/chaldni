"""
Get figure from image???
"""

from skimage import io
from skimage import feature
from skimage import color
from skimage import measure
from skimage.restoration import denoise_tv_chambolle, estimate_sigma
import matplotlib.pyplot as plt


def figure_from_image(image_file):
    pass


if __name__ == '__main__':
    in_filename = 'Subject.png'

    raw_image = io.imread(in_filename)
    rgb_image = color.rgba2rgb(raw_image)
    gray_image = color.rgb2gray(rgb_image)

    canny_test = feature.canny(gray_image, sigma=3)

    sig_est = estimate_sigma(canny_test)
    print(sig_est)

    denoise1 = denoise_tv_chambolle(canny_test, weight=0.1)
    fig = plt.figure()
    plt.imshow(denoise1, cmap="gray")
    plt.show()
