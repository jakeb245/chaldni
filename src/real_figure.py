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


def get_angle(image):
    imgray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    imgray = np.float32(imgray)
    dst = cv.cornerHarris(imgray, 2, 3, 0.04)
    dst = cv.dilate(dst, None)
    ret, dst = cv.threshold(dst,0.01*dst.max(),255,0)
    dst = np.uint8(dst)
    # find centroids
    ret, labels, stats, centroids = cv.connectedComponentsWithStats(dst)
    # define the criteria to stop and refine the corners
    criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 100, 0.001)
    corners = cv.cornerSubPix(imgray, np.float32(centroids), (5, 5), (-1, -1), criteria)
    # Now draw them
    res = np.hstack((centroids, corners))
    res = np.int0(res)
    image[res[:, 1], res[:, 0]] = [0, 0, 255]
    image[res[:, 3], res[:, 2]] = [0, 255, 0]
    cv.imshow('blah',image)


if __name__ == '__main__':
    fname = "Slide1.png"
    im = cv.imread(fname)
    contours1 = get_contours(im)
    cent = find_center(im, contours1[1])
    get_angle(im)
    im_rot = rotate_image(im, cent, 69)
    contours2 = get_contours(im_rot)
    get_angle(im_rot)
    plt.imshow(im_rot, cmap='gray')
    plt.show()
