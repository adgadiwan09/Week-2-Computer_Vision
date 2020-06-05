import numpy as np
import cv2

b=np.zeros([350,350])
print(b)
print(b.ndim)
print(b.shape)
print(b.dtype)

cv2.imshow('Black Background', b)
cv2.waitKey(0)
cv2.destroyAllWindows()
