import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('lena.tif',0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
print(fshift)
rows, cols = fshift.shape

mask=np.zeros((rows,cols),np.uint8)
r=rows//2
c=cols//2
for i in range(r-30,r+30):
	for j in range(c-30,c+30):
		mask[i][j]=1

fshift*=mask
magnitude_spectrum = 100*np.log(np.abs(fshift)+1)

f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)





plt.subplot(131),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])



plt.subplot(132),plt.imshow(img_back, cmap = 'gray')
plt.title('After LPF'), plt.xticks([]), plt.yticks([])

plt.subplot(133),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])


plt.show()

plt.hist(img_back.ravel(),bins=256,range=[0,256])
plt.show()
