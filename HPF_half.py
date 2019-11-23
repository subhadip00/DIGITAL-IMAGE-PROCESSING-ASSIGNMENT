import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('lena.tif',0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))

print(fshift)
rows, cols = fshift.shape
r=rows//2
c=cols//2
for i in range(0,rows):
	for j in range(0,c):
		fshift[i][j]=0+0j

print(fshift)
f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)


magnitude_spectrum = 100*np.log(np.abs(img_back))



plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])




plt.subplot(122),plt.imshow(img_back, cmap = 'gray')
plt.title('After HPF'), plt.xticks([]), plt.yticks([])



plt.show()

plt.hist(img_back.ravel(),bins=256,range=[0,256])
plt.show()