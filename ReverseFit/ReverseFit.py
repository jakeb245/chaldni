"""
Reverse fit C constant
"""

import matplotlib.pyplot as plt
from src.compare import compare_images, read_image
import os
import statistics
import numpy as np
import csv


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
    exp_img = read_image(exp_fname, denoise=True)
    for img in images:
        if images[img][0] == freq:
            error = compare_images(exp_fname, img, exp_img, denoise=False)
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
    outfile = "/Users/jakebuchanan/code/chladni/ReverseFit/output.csv"

    exp_images, freq_list = get_data(data_dir)
    img_list = get_model(theo_dir, freq_list)

    with open(outfile, 'w') as file:
        writer = csv.writer(file)
        header = ['Frequency', 'C']
        writer.writerow(header)

        c_each = []
        for exp in exp_images:
            exp_name = exp.split('_')
            freq = exp_name[1][0:-4]
            c = fit(exp_images[exp], img_list, os.path.join(data_dir, exp))
            c_each.append(c)
            print(f"For image {exp}: c = {c}")
            writer.writerow([freq, c])

        mean = statistics.mean(c_each)
        dev = statistics.stdev(c_each)

        writer.writerow(['Mean', 'Dev'])
        writer.writerow([mean, dev])

    freq_list = [float(s) for s in freq_list]
    xrange = (min(freq_list), max(freq_list))
    xline = np.linspace(xrange[0],xrange[1],1000)
    fig = plt.figure()
    plt.plot(freq_list, c_each, '.')
    plt.plot(xline, np.zeros(len(xline)) + mean, color='blue')
    plt.plot(xline, np.zeros(len(xline)) + mean + dev, color='blue', linestyle='dotted')
    plt.plot(xline, np.zeros(len(xline)) + mean - dev, color='blue', linestyle='dotted')
    plt.title('C constant vs. Frequency')
    plt.ylabel('C constant')
    plt.xlabel('Frequency')
    plt.savefig('/Users/jakebuchanan/code/chladni/ReverseFit/output.png', dpi=300)
