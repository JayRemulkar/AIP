"""Write program to implement point/pixel intensity transformations such as
Log and Power-law transformations
Contrast adjustments
Histogram equalization
Thresholding, and halftoning operations"""

import cv2
from matplotlib import pyplot as plt
import numpy as np

# thresholding
def Thresholding():
    img = cv2.imread("lenna_original.jpg",0)

    ret, thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

    plt.imshow(thresh1,"gray",vmin=0,vmax=255)
    plt.show()

def main():
    Thresholding()

if __name__ == "__main__":
    main()