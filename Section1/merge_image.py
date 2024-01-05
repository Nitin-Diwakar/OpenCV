import numpy as np
import cv2

img1 = cv2.imread("Images/cards.jpg")
img1_re = cv2.resize(img1,(200,200))
img2 = cv2.imread("Images/cards2.jpg")
img2_re = cv2.resize(img2,(200,200))

merge = np.hstack((img1_re,img2_re))

cv2.imshow("Merger",merge)
cv2.waitKey(0)