import cv2
import numpy as np
img = cv2.imread("Images/documentscanner2.jpg")


kernel = np.ones((5,5), np.uint8)

#settig the threshold value
lower_t = 100
higher_t = 120

# Apply canny edge detector

img_canny = cv2.Canny(img,lower_t, higher_t)

#  apply dilation
# increase the thickess of the edges
img_dilation = cv2.dilate(img_canny, kernel=kernel, iterations=1)

# apply erosion
img_erode = cv2.erode(img_dilation, kernel,iterations=1)

cv2.imshow("Edge",img_canny)
cv2.imshow("Dialtion", img_dilation)

cv2.imshow("erosion",img_erode)
cv2.waitKey(0)