"""
This code should take an image that contains a black square plate
on a white surface and isolate the plate. Then it should rotate the
image and scale it as necessary. Finally, it should convert the
image to binary format
"""
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv


def get_contours(image):
    imgray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, thresh = cv.threshold(imgray, 127, 255, 0)
    contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    return contours

def rotate_image(image, point, angle):
  rot_mat = cv.getRotationMatrix2D(point, angle, 1.0)
  result = cv.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv.INTER_LINEAR)
  return result


def find_center(image, c):
    M = cv.moments(c)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    return (cX, cY)


def get_angle(image, c):
    M = cv.moments(c)
    angle = (M["m10"] - M["m00"]) / (M["m01"] - M["m00"])
    print(angle)



if __name__ == '__main__':
    fname = "Slide1.png"
    im = cv.imread(fname)
    contours1 = get_contours(im)
    cent = find_center(im, contours1[1])
    get_angle(im, contours1[1])
    im_rot = rotate_image(im, cent, 69)
    contours2 = get_contours(im_rot)
    get_angle(im_rot, contours2[1])
    plt.imshow(im_rot, cmap='gray')
    plt.show()
