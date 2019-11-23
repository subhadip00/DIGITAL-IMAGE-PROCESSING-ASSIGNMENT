import cv2
import numpy as np 
def find_nearest_above(my_array,target):
	diff=my_array-target
	mask=np.ma.less_equal(diff,-1)
	if np.all(mask):
		c=np.abs(diff).argmin()
		return c
	masked_diff=np.ma.masked_array(diff,mask)
	return masked_diff.argmin()

def hist_match(original,specified):
	oldshape=original.shape
	original=original.ravel() #flattened the 2D array
	specified=specified.ravel()
	s_values,bin_idx,s_counts=np.unique(original,return_inverse=True,return_counts=True)
	t_values, t_counts=np.unique(specified,return_counts=True)
	s_quantiles=np.cumsum(s_counts).astype(np.float64)
	s_quantiles/=s_quantiles[-1]

	t_quantiles=np.cumsum(t_counts).astype(np.float64)
	t_quantiles/=t_quantiles[-1]

	sour=np.around(s_quantiles*255)
	temp=np.around(t_quantiles*255)

	b=[]
	for data in sour[:]:
		b.append(find_nearest_above(temp,data))
	b=np.array(b,dtype='uint8')

	return b[bin_idx].reshape(oldshape)



original=cv2.imread('pic.tif',0)
specified=cv2.imread('lena.tif',0)
cv2.imshow('Original',original)
cv2.imshow('Specified',specified)
matched=hist_match(original,specified)
cv2.imshow('Matched',np.array(matched,dtype='uint8'))
cv2.waitKey(0)