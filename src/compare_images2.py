from src.compare import compare_images, add_figures
import matplotlib.pyplot as plt


if __name__ == '__main__':
    theo = "/Users/jakebuchanan/code/chladni/ReverseFit/images/Freq965C212926.PNG"
    real = "figure_965.png"

    print(compare_images(real, theo))

    combine = add_figures(real, theo)
    plt.imshow(combine)
    plt.show()
