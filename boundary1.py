import cv2 
import numpy as np 
import matplotlib.pyplot as plt

# Let's load a simple image with 3 black squares 
image = cv2.imread('boundary.jpg',1) 


kernel = np.ones((3,3), np.uint8) 
img_erosion = cv2.erode(image, kernel, iterations=1) 
img_dilation = cv2.dilate(image, kernel, iterations=1) 

contour=img_dilation-img_erosion

plt.subplot(121),plt.imshow(image)
plt.title("Image"),plt.xticks([]),plt.yticks([])

plt.subplot(122),plt.imshow(contour)
plt.title("Contour"),plt.xticks([]),plt.yticks([])

plt.show()

