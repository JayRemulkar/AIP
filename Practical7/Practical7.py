# Write a program to Apply edge detection techniques such as Sobel and Canny to extract meaningful information from the given image samples

import cv2
import matplotlib.pyplot as plt

#Canny
def main():
    img = cv2.imread("lenna_original.jpg")

    t_lower = 50
    t_upper = 150

    edge = cv2.Canny(img, t_lower, t_upper)

    plt.imshow(edge)
    plt.show()

if __name__ == "__main__":
    main()