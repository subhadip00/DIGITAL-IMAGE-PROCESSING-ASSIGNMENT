import cv2
import numpy as np 
img=cv2.imread('lena.tif')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
sift=cv2.xfeatures2d.SIFT_create()
#sift=cv2.SIFT()
kp=sift.detect(gray,None)
img=cv2.drawKeypoints(gray,kp)
cv2.imshow("Sift",img)
cv2.waitKey(0)