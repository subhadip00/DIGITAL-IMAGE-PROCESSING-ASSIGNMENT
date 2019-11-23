
import cv2 
import numpy as np 
import matplotlib.pyplot as plt
# Reading the input image 
img_temp = cv2.imread('fingerprint.png', 0) 
(thresh, img) = cv2.threshold(img_temp, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
cv2.imwrite('fingerprint_binary.png',img)



# Taking a matrix of size 5 as the kernel 
kernel = np.ones((3,3), np.uint8) 

# The first parameter is the original image, 
# kernel is the matrix with which image is 
# convolved and third parameter is the number 
# of iterations, which will determine how much 
# you want to erode/dilate a given image. 
img_erosion = cv2.erode(img, kernel, iterations=1) 
opening = cv2.morphologyEx(img_erosion, cv2.MORPH_OPEN, kernel)

img_dilation = cv2.dilate(opening, kernel, iterations=1) 

closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)


plt.subplot(151), plt.imshow(img,cmap='gray')
plt.title('Input'),plt.xticks([]),plt.yticks([])

plt.subplot(152), plt.imshow(img_erosion,cmap='gray')
plt.title('Erosion'),plt.xticks([]),plt.yticks([])

plt.subplot(153), plt.imshow(img_dilation,cmap='gray')
plt.title('Dilation'),plt.xticks([]),plt.yticks([])

plt.subplot(154), plt.imshow(opening,cmap='gray')
plt.title('Opening'),plt.xticks([]),plt.yticks([])

plt.subplot(155), plt.imshow(closing,cmap='gray')
plt.title('Closing'),plt.xticks([]),plt.yticks([])

plt.show()
