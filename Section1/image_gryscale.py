import cv2

img = cv2.imread("Images/car.jpg")

img_gray = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)

cv2.imshow('Gray',img_gray)

cv2.waitKey(0)