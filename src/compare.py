"""Compare two images in binary format using mean-squared-error"""

from skimage import io, color
from skimage.filters import threshold_mean
from sklearn.metrics import mean_squared_error


def read_image(filename):
    raw = io.imread(filename)
    try:
        rgb = color.rgba2rgb(raw)
    except:
        rgb = raw
    finally:
        gray = color.rgb2gray(rgb)
    thresh = threshold_mean(gray)
    bool_array = gray > thresh
    return bool_array * 1


def compare_images(exp_filename, theo_filename):
    exp = read_image(exp_filename)
    theo = read_image(theo_filename)

    error = mean_squared_error(exp, theo)

    return error
