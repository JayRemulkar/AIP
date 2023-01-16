"""Write program to implement point/pixel intensity transformations such as
Log and Power-law transformations
Contrast adjustments
Histogram equalization
Thresholding, and halftoning operations"""

import cv2
from matplotlib import pyplot as plt
from matplotlib import image as mpimg
import numpy as np
import warnings

warnings.filterwarnings("ignore")

# Log transformations
def LogTransform(img):
    
    c = 255/(np.log(1 + np.max(img)))
    log_transformed = c * np.log(1 + img)

    log_transformed = np.array(log_transformed,dtype = np.uint8)

    cv2.imwrite("log_transformed.jpg",log_transformed)

    img = mpimg.imread("log_transformed.jpg")
    plt.imshow(img)
    plt.show()

# Power-law transformations
def PowerLawTranf(img):

    Arr = []

    for gamma in [0.1,0.5,1.2,2.2]:
        
        gamma_corrected = np.array(255*(img / 255) ** gamma, dtype = "uint8")
        cv2.imwrite("gamma_transformed"+str(gamma)+".jpg",gamma_corrected)
        Arr.append("gamma_transformed"+str(gamma)+".jpg")

    for Timg in Arr:
        temp = mpimg.imread(Timg)
        plt.imshow(temp)
        plt.show()

def main():
    img1 = cv2.imread("lenna.jpg")
    img2 = cv2.imread("lenna_original.jpg")
    
    LogTransform(img1)
    PowerLawTranf(img2)

if __name__ == "__main__":
    main()