"""
This code should take an image that contains a black square plate
on a white surface and isolate the plate. Then it should rotate the
image and scale it as necessary. Finally, it should convert the
image to binary format
"""

from skimage import io, feature, color
import matplotlib.pyplot as plt
import cv2 as cv


if __name__ == '__main__':
    fname = "real_test.jpeg"
    im = cv.imread(fname)
    imgray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
    ret, thresh = cv.threshold(imgray, 127, 255, 0)
    contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    cv.drawContours(im, contours, -1, (0, 255, 0), 3)
    plt.imshow(im, cmap='gray')
    plt.show()
