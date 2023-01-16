# non linear noise smoothning

from PIL import Image, ImageFilter
import matplotlib.pyplot as plt

img = Image.open("lenna_original.jpg")

img2 = img.filter(ImageFilter.ModeFilter(size=3))
plt.imshow(img2)
plt.show()