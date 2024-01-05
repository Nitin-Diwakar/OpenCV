import cv2

image = cv2.imread("Images/car.jpg")

img_blur = cv2.GaussianBlur(image, (87,57),0)

cv2.imshow("blur",img_blur)
cv2.waitKey(0)