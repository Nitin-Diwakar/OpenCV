import cv2

img = cv2.imread("Images/lambo.png")
imghsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
lower = (0,24,101)
higher  = (19,255,255)

mask = cv2.inRange(imghsv, lower,higher)

color_img = cv2.bitwise_and(img,img,mask=mask)

cv2.imshow("Mask", color_img)
cv2.waitKey(0)