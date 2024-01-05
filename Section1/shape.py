import cv2
import numpy as np

img = np.zeros((512,512,3))
img[:] = 240,220,200

# cv2.line(img, (0,0), (img.shape[1], img.shape[0]), (0,255,0),3)

cv2.rectangle(img, (2,2), (250,250), (0,255,0), 4)

cv2.circle(img,(250,250),100,(0,255,0),10)

# write text on image
cv2.putText(img,"Shape", (200,150),cv2.FONT_HERSHEY_TRIPLEX, 3,(0,223,10),2)

cv2.imshow('shAPE',img)
cv2.waitKey(0)