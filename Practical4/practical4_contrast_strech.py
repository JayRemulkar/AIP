"""Write program to implement point/pixel intensity transformations such as
Log and Power-law transformations
Contrast adjustments
Histogram equalization
Thresholding, and halftoning operations"""

from PIL import Image,ImageEnhance
from matplotlib import pyplot as plt

# Contrast adjustments
def main():
    img = Image.open("lenna_original.jpg")

    obj = ImageEnhance.Contrast(img)

    for i in [0.5,1.0,1.5,2.0]:
        output = obj.enhance(i)
        plt.imshow(output)
        plt.show()

if __name__ == "__main__":
    main()