#Contrast adjustments

from PIL import Image,ImageEnhance
import matplotlib.pyplot as plt

#read the image
# Image.open(f,mode) it is same like fileio
img = Image.open("lenna_original.jpg")

#image brightness enhancer
enhancer = ImageEnhance.Contrast(img)

# set factors for contrast adjustment
factors = [0.5,1.0,1.5,2.0]

# show different contrast settings of lenna original photo
for i in factors:
    # enhance() this method returns enhanced image
    img_output = enhancer.enhance(i)
    imgplot = plt.imshow(img_output)
    plt.show()
