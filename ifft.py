import random
import numpy as np
x=[]
for i in range(11):
 	x.append(random.randint(0,500))
print(x)
z=np.fft.ifft(x)
#print(np.arange(100))
for p in z:
	print(p)