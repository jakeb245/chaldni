"""
Reverse fit C constant
"""
import matplotlib.pyplot as plt
from src.compare import compare_images, add_figures
import os
import statistics
from skimage.restoration import denoise_tv_chambolle


def get_model(img_dir, freq_list):
    """
    Get list of image filenames from img_dir for specified frequency.
    filename structure: "Freq965_C0.244214.PNG"
    :param img_dir: path to directory of theoretical images
    :param freq: frequency
    :return:
    """
    images = {}
    for freq in freq_list:
        for ff in os.listdir(img_dir):
            f = ff[0:-4]  # Remove .png
            fs = f.split('_')
            if fs[0].endswith(str(freq)):
                c = fs[1][1:]
                images[os.path.join(img_dir, ff)] = [freq, float(c)]
    return images


def get_data(img_dir):
    images = {}
    freq_list = []
    for img_full in os.listdir(img_dir):
        if img_full.startswith('figure'):
            img = img_full[0:-4]  # Remove .png
            sp = img.split('_')
            freq = sp[1]
            images[img_full] = freq
            freq_list.append(freq)
    return images, freq_list


def fit(freq, images, exp_fname):
    lowest_error = 1.0
    lowest_c = None
    for img in images:
        img_denoised = denoise_tv_chambolle(img, weight=0.2, channel_axis=-1)
        if images[img][0] == freq:
            error = compare_images(exp_fname, img_denoised, denoise=False)
            c = images[img][1]
            if error < lowest_error:
                lowest_error = error
                best_img = img
                lowest_c = c
    lowest_c = lowest_c

    return lowest_c


if __name__ == '__main__':
    theo_dir = "/Users/jakebuchanan/code/chladni/ReverseFit/images"
    data_dir = "/Users/jakebuchanan/code/chladni/data"

    exp_images, freq_list = get_data(data_dir)
    img_list = get_model(theo_dir, freq_list)

    c = []
    for exp in exp_images:
        c.append(fit(exp_images[exp], img_list, os.path.join(data_dir, exp)))

    print(c)
