import cv2 
import numpy as np 
import matplotlib.pyplot as plt
# Reading the input image 
inputimg = cv2.imread('building.jpeg', 0)
kernelx=np.array([[-1,2,-1],[-1,2,-1],[-1,2,-1]],dtype='int32')
kernely=np.array([[-1,-1,-1],[2,2,2],[-1,-1,-1]],dtype='int32')

sobelx=cv2.filter2D(inputimg,-1,kernelx)
sobely=cv2.filter2D(inputimg,-1,kernely)
cv2.imshow('Horizontal Edges',sobely)
cv2.imshow('Vertical Edges',sobelx)
cv2.waitKey(0)

'''plt.subplot(131),plt.imshow(inputimg,cmap='gray')
plt.title('input iamge'),plt.xticks([]),plt.yticks([])

plt.subplot(132),plt.imshow(sobelx,cmap='gray')
plt.title('input iamge'),plt.xticks([]),plt.yticks([])

plt.subplot(133),plt.imshow(sobely,cmap='gray')
plt.title('input iamge'),plt.xticks([]),plt.yticks([])

plt.show()
'''
