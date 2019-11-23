import cv2 
import numpy as np 

# Let's load a simple image with 3 black squares 
image = cv2.imread('boundary.jpg',0) 

edged = cv2.Canny(image, 30, 200) 



contours, hierarchy = cv2.findContours(edged, 
	cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 

cv2.imshow('Canny Edges After Contouring', edged) 
'''
print("Number of Contours found = " + str(len(contours))) 

# Draw all contours 
# -1 signifies drawing all contours 
cv2.drawContours(image, contours, -1, (0, 255, 0), 3) 

cv2.imshow('Contours', image) 
'''
cv2.waitKey(0) 
cv2.destroyAllWindows() 
