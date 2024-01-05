import cv2

img = cv2.imread("Images/documentscanner2.jpg")

#settig the threshold value
lower_t = 100
higher_t = 120

# Apply canny edge detector
img_canny = cv2.Canny(img,lower_t, higher_t)
cv2.imshow("Edge",img_canny)
cv2.waitKey(0)