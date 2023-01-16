# Write a program to implement
# linear and 
# nonlinear noise smoothing 
# on suitable image or sound signal.

from PIL import Image, ImageFilter
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Opening the image
# (R prefixed to string in order to deal with '\' in paths)
image = Image.open("lenna_original.jpg")

# Blurring image by sending the ImageFilter.
# GaussianBlur predefined kernel argument
# ImageFilter module contains methods wich can be used with Image.filter method.
smooth = image.filter(ImageFilter.GaussianBlur)
# Displaying the image
plt.imshow(smooth)
plt.show()

# Median filter

img = Image.open("lenna_original.jpg")

# applying the median filte
img2 = img.filter(ImageFilter.MedianFilter(size=3))

plt.imshow(img2)
plt.show()
