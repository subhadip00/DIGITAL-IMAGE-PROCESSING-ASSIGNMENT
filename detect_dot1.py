import cv2 
import numpy as np 
import matplotlib.pyplot as plt
# Reading the input image 
inputimg = cv2.imread('dotted_img.jpeg', 0)

laplacian=np.array([[0,0,0],[1,-8,1],[0,0,0]],np.int32)

outputimg=cv2.filter2D(inputimg,-1,laplacian)
cv2.imshow('Input',inputimg)
cv2.imshow('Output',outputimg)
cv2.waitKey(0)