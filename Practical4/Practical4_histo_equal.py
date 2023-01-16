"""Write program to implement point/pixel intensity transformations such as
Log and Power-law transformations
Contrast adjustments
Histogram equalization
Thresholding, and halftoning operations"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

# Histogram equalization
def main():
    img = cv2.imread("lenna.jpg",0)

    Eqimg = cv2.equalizeHist(img)

    plt.imshow(np.hstack((img,Eqimg)))
    plt.show()

if __name__ == "__main__":
    main()