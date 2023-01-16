#Write program to demonstrate the following aspects of signal on sound/image data
# 1 Convolution operation
# 2 Template Matching

# Blurring using convolution operation Box Blurring

import cv2
import numpy as np 
from matplotlib import pyplot as plt 

img = cv2.imread("lenna.jpg")
plt.imshow(img)
plt.show()

# Kernel for box blur filter
# It is a unity matrix which is divided by 9
# array(data) creates an array and returns it
box_blur_ker = np.array([[0.1111111, 0.1111111, 0.1111111],[0.1111111, 0.1111111, 0.1111111],[0.1111111, 0.1111111, 0.1111111]])
print(box_blur_ker)

# Applying Box Blur effect
# Using the cv2.filter2D() function
# src is the source of image(here, img)
# ddepth is destination depth. -1 will mean output image will have same depth as input image
# kernel is used for specifying the kernel operation (here, box_blur_ker)
box_blur = cv2.filter2D(img,ddepth=-1,kernel = box_blur_ker)

plt.imshow(box_blur)
plt.show()