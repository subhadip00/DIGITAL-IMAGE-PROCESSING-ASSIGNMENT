import cv2 
import numpy as np 
import matplotlib.pyplot as plt
# Reading the input image 
inputimg = cv2.imread('dotted_img.jpeg', 0)
outputimg=cv2.medianBlur(inputimg,3)

cv2.imshow('Input',inputimg)
cv2.imshow('output',outputimg)
cv2.waitKey(0)
