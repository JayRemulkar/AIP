# Write the program to implement various morphological image processing techniques

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Erosion

img = cv2.imread("lenna_original.jpg",0)
kernel = np.ones((5,5),np.uint8)
#print(img)

# erode() is used to perform erosion on image
erosion = cv2.erode(img, kernel, iterations=1)
#print(erosion)

plt.imshow(erosion)
plt.show()

# Dilation

# dilate() is used to perform dilation on image
dilation = cv2.dilate(img, kernel, iterations=1)

plt.imshow(dilation)
plt.show()

# Opening  

opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

plt.imshow(opening)
plt.show()

# Closing

closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

plt.imshow(closing)
plt.show()