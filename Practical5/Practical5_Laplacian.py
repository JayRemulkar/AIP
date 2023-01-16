# Write a program to apply various enhancements on images using image derivatives by implementing Laplacian operations.
# Laplacian operations.

import mahotas
import numpy as np
import cv2
from matplotlib import pyplot as plt

def LaplacianOperation():
    img = mahotas.imread("lenna_original.jpg")

    ddepth = cv2.CV_16S
    kernel_size = 3

    src = cv2.imread("lenna_original.jpg",1)
    
    src = cv2.GaussianBlur(src, (3,3), 0)

    src_gray = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)

    dst = cv2.Laplacian(src_gray, ddepth, ksize = kernel_size)

    abs_dst = cv2.convertScaleAbs(dst)

    print("original image")
    plt.imshow(img)
    plt.show()

    print("When apply laplacian operation")
    plt.imshow(abs_dst)
    plt.show()

def main():
    LaplacianOperation()

if __name__ == "__main__":
    main()