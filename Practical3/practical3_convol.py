#Write program to demonstrate the following aspects of signal on sound/image data
# 1 Convolution operation

import cv2
from matplotlib import pyplot as plt
import numpy as np

# Blurring using convolution operation Box Blurring
def main():
    img = cv2.imread("lenna.jpg")
    plt.imshow(img,cmap="gray")
    plt.show()

    box_blur_fil = np.array([[0.1111111, 0.1111111, 0.1111111],[0.1111111, 0.1111111, 0.1111111],[0.1111111, 0.1111111, 0.1111111]])

    box_blur = cv2.filter2D(src=img,ddepth=-1,kernel=box_blur_fil)
    plt.imshow(box_blur)
    plt.show()

if __name__ == "__main__":
    main()