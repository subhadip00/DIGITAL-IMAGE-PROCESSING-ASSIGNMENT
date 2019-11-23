import cv2
import matplotlib.pyplot as plt 
img=cv2.imread("F:\\Image Processing\\misc\\damaged.jpg",0)
#img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
edgesx=cv2.Scharr(img,-1,dx=1,dy=0,scale=1,delta=0,borderType=cv2.BORDER_DEFAULT)
edgesy=edgesx=cv2.Scharr(img,-1,dx=0,dy=1,scale=1,delta=0,borderType=cv2.BORDER_DEFAULT)
edges=edgesx+edgesy
output=[img,edgesx,edgesy,edges]
titles=['original','dx=1 dy=0','dx=0 dy=1','Edges']

for i in range(4):
	plt.subplot(2,2,i+1)
	plt.imshow(output[i],cmap='gray')
	plt.title(titles[i])
	plt.xticks([])
	plt.yticks([])
plt.show()