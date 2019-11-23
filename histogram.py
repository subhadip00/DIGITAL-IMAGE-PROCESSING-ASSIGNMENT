import cv2
import sys
import numpy as np
import matplotlib.pyplot as plt
img1=cv2.imread('lena.tif',0)
img2=img1 & 15
img3=img1-img2
img4=cv2.equalizeHist(img3)
fig=plt.figure()
'''
ax1=fig.add_subplot(4,1,1)
ax1.imshow(img1,cmap='gray')
ax2=fig.add_subplot(4,1,2)
ax2.imshow(img2,cmap='gray')
ax3=fig.add_subplot(4,1,3)
ax3.imshow(img3,cmap='gray')
ax4=fig.add_subplot(4,1,4)
ax4.imshow(img4,cmap='gray')
'''
plt.show()