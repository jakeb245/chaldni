import src.compare as comp
import matplotlib.pyplot as plt


exp = '/Users/jakebuchanan/code/chladni/data/figure_965.png'
theo = '/Users/jakebuchanan/code/chladni/ReverseFit/images/Freq965_C0.202133.PNG'

print(comp.compare_images(exp, theo))

add = comp.add_figures(exp, theo)
plt.imshow(add)
plt.show()
