import cv2

img = cv2.imread("Images/image.jpg")

img_resize = cv2.resize(img, (1920,1080))

cv2.imshow("Original",img)
cv2.imshow("resize",img_resize)

cv2.waitKey(0)