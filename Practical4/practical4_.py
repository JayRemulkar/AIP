# Thresholding, and halftoning operations

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
from PIL import Image

# Image thresholding on lenna
img = cv.imread("lenna_original.jpg",0)
# threshold() 1st parameter is img.
# 2nd is the threshold value for every pixel,
# if the pixel value is less than threshhold value the pixel value gets changed to 0
# 3rd parameter is the value which gets changed with pixels which exceds the threshold value
# 4th is thresholding types
ret,thresh1 = cv.threshold(img,127,255,cv.THRESH_BINARY)

plt.imshow(thresh1,"gray",vmin=0,vmax=255)
plt.show()

# image halftoneing

img = Image.open("lenna_original.jpg")        # open RGB image
# convert(color_mode) Returns a converted copy of this image.
cmyk = img.convert("CMYK").split()             # RGB contone RGB to CMYK contone
print(cmyk)
c = cmyk[0].convert("1").convert("L")         # and then halftone ('1') each plane
m = cmyk[1].convert("1").convert("L")         # ...and back to ('L') mode
y = cmyk[2].convert("1").convert("L")
k = cmyk[3].convert("1").convert("L")

new_cmyk = Image.merge("CMYK",[c,m,y,k])        # put together all 4 planes
res = new_cmyk.save("half_toneing.jpg")

img = mpimg.imread("half_toneing.jpg")
plt.imshow(img)
plt.show()