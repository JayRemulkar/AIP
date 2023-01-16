# Write a program to apply various enhancements on images using image derivatives by implementing
# Gradient and 
# Laplacian operations.

import numpy as np
from pylab import imshow, show
import matplotlib.pyplot as plt
import cv2

# gradient operator on lenna original colour image
img = cv2.imread("lenna_original.jpg",1)

# Converting image to grayscale
# cvtColor() is used to convert image from one color space to other.
# return an image with the given color space.
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Creating Prewitt filter
kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])

# Applying filter to the image in both x and y direction
# filter2D() using this filter we can convolve our image with kernel.
img_prewittx = cv2.filter2D(img,-1,kernelx)
img_prewitty = cv2.filter2D(img,-1,kernely)
#print(img_prewittx,img_prewitty)

# Taking root of squared sum(np.hypot) from both the direction and displaying
# hypot() return hypotenuse.
prewitt = np.hypot(img_prewittx,img_prewitty)
#print(prewitt)
prewitt = prewitt[:,:,0]
# astype() make copy of array to specific type
prewitt = prewitt.astype("int")
plt.imshow(prewitt,cmap="gray")
plt.show()