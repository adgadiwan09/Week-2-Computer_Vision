import numpy as np
import cv2

b=np.ones([300,300,3], dtype='uint8')#width height depth
print(b)
print(b.dtype)
print(b.ndim)
print(b.shape)
b[0:100,0:50]=[50,100,150] #not RGB its BGR here
b[100:250,50:200]=[60,100,115]
b[250:300,200:300]=[150,20,70]
cv2.imshow('Colorful',b)
cv2.waitKey()
cv2.destroyAllWindows()
