# Histogram equalization

import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = cv2.imread("lenna.jpg",0)

# creating a Histograms Equalization
# of a image using cv2.equalizeHist()
equ = cv2.equalizeHist(img)

# original image and histogram equalised imagae side by side comparison
# hstack() two bind things side by side
res = np.hstack((img,equ))
plt.imshow(res)
plt.show()