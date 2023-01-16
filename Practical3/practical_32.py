# Write program to demonstrate the following aspects of signal on sound/image data.
# 2.Template matching

import cv2
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import image as mpimg

img_rgb = cv2.imread("messi.png")

# cvtColor(src,code) is used to change colorspace of an image 
# return an image with changed color
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

plt.imshow(img_gray)
plt.show()

template = cv2.imread("template.jpg",0)

plt.imshow(template)
plt.show()

# Store width and height of template in w and h
w, h = template.shape[::-1]
#print(w,h)

# matchTemplate(target_image,template,method) it is used to find ssecific pattern in image 
# returns a matrix with a matching value from target_image.
result = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)

print(result)
#plt.imshow(result)
#plt.show()

# Specify a threshold
# Store the coordinates of matched area in a numpy array
threshold = 0.8

# where(condition(array),[x,y]) return array of values depends on condition
# if true yeild x else yeilds y 
loc = np.where(result >= threshold)
print(loc)

# Draw a rectangle around the matched region.
# rectangle(src,stat_point,end_point,color,thickness)
# returns an image with with rectangle
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb,pt,(pt[0] + w, pt[1] + h), (0,0,255), 2)

# Show the final image with the matched area.
# it is used to save image in device 
# imwrite(filename,image_to_store) return true if succes
cv2.imwrite("res.png",img_rgb)

#show template matched in original image in red box

# pyplot.imread() is internally calls image.imread()
img = mpimg.imread("res.png")
plt.imshow(img)
plt.show()
