import cv2

img = cv2.imread("Images/lambo.png")

img_crop = img[100:300, 200:500] # height, width

cv2.imshow("crop",img_crop)
cv2.waitKey(0)