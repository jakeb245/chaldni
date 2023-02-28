"""
Reverse fit C constant
"""
import matplotlib.pyplot as plt
from src.compare import compare_images, add_figures
import os
import statistics


def get_model(img_dir, exp_images):
    """
    Get list of image filenames from img_dir for specified frequency.
    filename structure: "Freq965_C0.244214.PNG"
    :param img_dir: path to directory of theoretical images
    :param freq: frequency
    :return:
    """
    freq_list = []
    for fp in exp_images:
        freq_list.append(exp_images[fp])

    images = {}
    for freq in freq_list:
        for ff in os.listdir(img_dir):
            f = ff[0:-4]  # Remove .png
            fs = f.split('_')
            print(fs)
            if fs[0].endswith(str(freq)):
                print(freq)
                c = fs[1][1:]
                images[os.path.join(img_dir, ff)] = [freq, float(c)]
    return images


def get_data(img_dir):
    images = {}
    for img_full in os.listdir(img_dir):
        if img_full.startswith('figure'):
            img = img_full[0:-4]  # Remove .png
            sp = img.split('_')
            freq = float(sp[1])
            images[img_full] = freq
    return images


def fit(freq_list, images, exp_fname):
    lowest_c = []
    for freq in freq_list:
        lowest_error = 1.0
        best_img = None
        for img in images:
            if images[img][0] == freq:
                error = compare_images(exp_fname, img)
                c = images[img][1]
                if error < lowest_error:
                    lowest_error = error
                    best_img = img
        lowest_c.append(images[best_img][1])

    print("Best fitting C values:", lowest_c)

    avg = statistics.mean(lowest_c)
    stdev = statistics.stdev(lowest_c, avg)

    print(f"Average C: {avg} +/- {stdev}")
    return avg, stdev


if __name__ == '__main__':
    theo_dir = "/Users/jakebuchanan/code/chladni/ReverseFit/images"
    data_dir = "/Users/jakebuchanan/code/chladni/data"

    exp_images = get_data(data_dir)
    img_list = get_model(theo_dir, exp_images)
