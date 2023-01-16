"""Write program to implement point/pixel intensity transformations such as
Log and Power-law transformations
Contrast adjustments
Histogram equalization
Thresholding, and halftoning operations"""

import cv2
import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import warnings

img = cv2.imread("lenna.jpg")

warnings.filterwarnings("ignore")
# Apply log transform.
c = 255/(np.log(1 + np.max(img)))
log_transformed = c * np.log(1 + img)
#print(log_transformed)

# Specify the data type.
log_transformed = np.array(log_transformed,dtype=np.uint8)
#print(log_transformed)
# Save the output.
# cv2.imwrite(filename, image) used to store image on device returns true on success
cv2.imwrite("log_transformed.jpg",log_transformed)

img = mpimg.imread("log_transformed.jpg")
imgplot = plt.imshow(img)
#print(img)
plt.show()

img = cv2.imread("lenna_original.jpg")

# Trying 4 gamma values.
for gamma in [0.1,0.5,1.2,2.2]:
    
    # Apply gamma correction.
    gamma_corrected = np.array(255*(img / 255) ** gamma, dtype="uint8")

    # Save edited images.
    cv2.imwrite("gamma_transformed"+str(gamma)+".jpg",gamma_corrected) 

#code to show different gamma levels in power law transform
for i in [0.1,0.5,1.2,2.2]:
    img = mpimg.imread(f"gamma_transformed"+str(i)+".jpg")
    imgplot = plt.imshow(img)
    plt.show()

