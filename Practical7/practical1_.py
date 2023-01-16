# Write a program to Apply edge detection techniques such as Sobel and Canny to extract meaningful information from the given image samples

import cv2
import matplotlib.pyplot as plt

# Canny edge detection

img = cv2.imread("lenna_original.jpg")      # read image
# Setting parameter values
t_lower = 50    # lower threshold
t_upper = 150   # upper threshold

# Applying the Canny Edge filter
edge = cv2.Canny(img,t_lower,t_upper)

plt.imshow(edge)
plt.show()