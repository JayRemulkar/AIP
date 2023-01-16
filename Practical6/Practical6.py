# Write a program to implement linear and nonlinear noise smoothing on suitable image or sound signal.
# linear and nonlinear noise smoothing

from PIL import Image, ImageFilter
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def main():
    img1 = Image.open("lenna_original.jpg")

    #GaussianBlur liner
    smooth = img1.filter(ImageFilter.GaussianBlur)
    plt.imshow(smooth)
    plt.show()

    img2 = Image.open("lenna_original.jpg")

    # Median Filter liner
    img2 = img2.filter(ImageFilter.MedianFilter(size=3))
    plt.imshow(img2)
    plt.show()

    # mode Filter non liner
    img2 = img1.filter(ImageFilter.ModeFilter(size=3))
    plt.imshow(img2)
    plt.show()

if __name__ =="__main__":
    main()