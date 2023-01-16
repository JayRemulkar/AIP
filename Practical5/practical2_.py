# Write a program to apply various enhancements on images using image derivatives by implementing
# Laplacian operations.

import mahotas
import numpy as np
from pylab import gray, imshow, show
import matplotlib.pyplot as plt
import cv2

# accepts image as input returns an array like object which represents the image. 
img = mahotas.imread("lenna_original.jpg")
#print(img)

# filtering image
img = img[:,:]       # done because of mahotas lib
print(img)

#laplacian operator

# [variables]
# Declare the variables we are going to use
ddepth = cv2.CV_16S
kernel_size = 3

src = cv2.imread("lenna_original.jpg",1)

# Remove noise by blurring with a Gaussian filter 
src = cv2.GaussianBlur(src, (3, 3), 0)
#print(src)

# Convert the image to grayscale
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

# Apply Laplace function
dst = cv2.Laplacian(src_gray, ddepth, ksize=kernel_size)
#print(dst)

# converts back to 8-bit
abs_dst = cv2.convertScaleAbs(dst)

print(" Original Image")

# showing image
imshow(img)
show()

print("When apply laplacian operation")
plt.imshow(abs_dst)
show()