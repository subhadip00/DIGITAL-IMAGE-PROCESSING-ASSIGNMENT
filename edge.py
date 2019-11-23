import cv2 
import numpy as np 
import matplotlib.pyplot as plt
# Reading the input image 
inputimg = cv2.imread('baby.jpeg', 0)

laplacian=np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]],np.int32)

outputimg=cv2.filter2D(inputimg,-1,laplacian)
cv2.imshow('Input',inputimg)
cv2.imshow('Output',outputimg)
cv2.waitKey(0)