# Write program to demonstrate the following aspects of signal processing on suitable data
# 1.Upsampling and downsampling on Image/speech signal
# 2.Fast Fourier Transform to compute DFT

import cv2
from matplotlib import pyplot as plt
import numpy as np

# imread(path,flag) used to load a image
# 1 for color  0 for gray   -1 for unchanged
# it return an array which contains a matrix of pixels
img1 = cv2.imread('lenna.jpg', 0)

# shape() retruns dimension of array
[m, n] = img1.shape
print('Image Shape:', m, n)

# imshow(data,cmap) it shows an image of data
# accpets data or shaps
print('Original Image:')
plt.imshow(img1, cmap="gray")
plt.show()

# Down sampling
# Assign a down sampling rate
# Here we are down sampling the
# image by 4
f = 4
# Create a matrix of all zeros for
# downsampled values

# zeros((m,n),dtype) it gives a array which contains matrix of zeros
img2 = np.zeros((m // f, n // f), dtype=np.int32)

# Assign the down sampled values from the original
# image according to the down sampling frequency.
# For example, if the down sampling rate f=2, take
# pixel values from alternate rows and columns
# and assign them in the matrix created above
for i in range(0, m, f):
    for j in range(0, n, f):
        try:
            img2[i // f][j // f] = img1[i][j]
        except IndexError:
            pass

print('Down Sampled Image:')
plt.imshow(img2, cmap="gray")
plt.show()

# Up sampling
# Create matrix of zeros to store the upsampled image
img3 = np.zeros((m, n), dtype=np.int32)

# new size
for i in range(0, m-1, f):
	for j in range(0, n-1, f):
		img3[i, j] = img2[i//f][j//f]

# Nearest neighbour interpolation-Replication
# Replicating rows
for i in range(1, m-(f-1), f):
	for j in range(0, n-(f-1)):
		img3[i:i+(f-1), j] = img3[i-1, j]

# Replicating columns
for i in range(0, m-1):
	for j in range(1, n-1, f):
		img3[i, j:j+(f-1)] = img3[i, j-1]

print('Up Sampled Image:')
plt.imshow(img3, cmap="gray")
plt.show()