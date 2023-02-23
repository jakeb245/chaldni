"""
Reverse fit C constant
"""
import matplotlib.pyplot as plt

from src.compare import compare_images, add_figures
import os


def get_model(img_dir, freq):
    """
    Get list of image filenames from img_dir for specified frequency.
    filename structure: "Freq965_C0.244214.PNG"
    :param img_dir: path to directory of theoretical images
    :param freq: frequency
    :return:
    """
    images = {}
    for ff in os.listdir(img_dir):
        f = ff[0:-4]  # Remove .png
        fs = f.split('_')
        if fs[0].endswith(str(freq)):
            c = fs[1][1:]
            images[os.path.join(img_dir,ff)] = [freq, float(c)]
    return images


def fit(freq_list, images, exp_fname):
    for img in images:
        print(compare_images(exp_fname, img), images[img][1])
        add = add_figures(exp_fname, img)
        plt.imshow(add)
        plt.axis('off')
        plt.savefig("/Users/jakebuchanan/code/chladni/ReverseFit/img" + str(images[img][1]) + '.png',
                    bbox_inches='tight', pad_inches=0)


if __name__ == '__main__':
    freq_list = [965]
    real_fname = "/Users/jakebuchanan/code/chladni/src/RealProto.png"
    dir = "/Users/jakebuchanan/code/chladni/ReverseFit/images"
    for freq in freq_list:
        img_list = get_model(dir, freq)
        fit(freq, img_list, real_fname)
