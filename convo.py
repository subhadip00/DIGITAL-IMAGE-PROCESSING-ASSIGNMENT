import cv2
import numpy as np
image = cv2.imread("convolution.tif",cv2.IMREAD_GRAYSCALE).astype(float)/255.0
kernel = np.array([[1, 0, -1],
                   [1, 0, -1],
                   [1, 0, -1]])

filtered = cv2.filter2D(src=image,kernel=kernel,ddepth=-1)
cv2.imshow("horizontal edges",filtered)

                    



