# Write program to demonstrate the following aspects of signal processing on suitable data
# 1.Upsampling and downsampling on Image/speech signal
# 2.Fast Fourier Transform to compute DFT

import cv2
from matplotlib import pyplot as plt
import numpy as np
from sympy import fft

# downsampling
def Downsampling(img1,m,n,f):
    img2 = np.zeros((m//f ,n//f),dtype = np.int32)

    for i in range(0,m,f):
        for j in range(0,n,f):
            try:
                img2[i//f][j//f] = img1[i][j]
            except IndexError:
                pass

    plt.imshow(img2,cmap="gray")
    plt.show()

    Upsampling(img1,img2,m,n,f)

# Upsampling
def Upsampling(img1,img2,m,n,f):
    img3 = np.zeros((m, n), dtype = np.int32)

    for i in range(0,m-1,f):
        for j in range(0,n-1,f):
            img3[i][j] = img2[i//f][j//f]

    for i in range(1,m-(f-1),f):
        for j in range(0,n-(f-1)):
            img3[i:i+(f-1), j] = img3[i-1][j]

    for i in range(0,m-1):
        for j in range(1,n-1,f):
            img3[i, j:j+(f-1)] = img3[i][j-1]

    plt.imshow(img3,cmap="gray")
    plt.show()

# 2.Fast Fourier Transform to compute DFT
def FFT():
    seq = [15,21,13,44]

    tranform = fft(seq)
    print(tranform)

def main():
    img1 = cv2.imread('lenna.jpg',0)

    m,n = img1.shape
    print("Dimensions ",m,n)

    plt.imshow(img1,cmap="gray")
    plt.show()

    Downsampling(img1,m,n,4)
    FFT()

if __name__ == "__main__":
    main()