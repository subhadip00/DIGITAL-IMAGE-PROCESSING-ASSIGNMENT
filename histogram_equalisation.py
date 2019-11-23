import cv2
import numpy as np 
import matplotlib.pyplot as plt 

img1=cv2.imread('lena.tif',0)
cv2.imshow('Original Image',img1)
img2=cv2.equalizeHist(img1)
cv2.imshow('Histogram Equalized',img2)
cv2.waitKey(0)