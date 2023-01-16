# Write a program to apply various enhancements on images using image derivatives by implementing Gradient
# Gradient 

import numpy as np
from matplotlib import pyplot as plt 
import cv2

def Gradient():
    img = cv2.imread("lenna_original.jpg")
    gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
    kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])

    img_prewittx = cv2.filter2D(img,-1,kernelx)
    img_prewitty = cv2.filter2D(img,-1,kernely)

    prewitt = np.hypot(img_prewittx,img_prewitty)

    prewitt = prewitt[:,:,0]

    prewitt = prewitt.astype("int")
    plt.imshow(prewitt,cmap="gray")
    plt.show()

def main():
    Gradient()
    
if __name__ == "__main__":
    main()