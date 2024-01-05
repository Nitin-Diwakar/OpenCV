import cv2
import numpy as np

img = cv2.imread("Images/shapes.png")

# step1: Convert this image
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Step: Apply the canny edge detector
lower_thre = 100
higher_thre = 150

img_canny = cv2.Canny(img_gray,lower_thre, higher_thre)

# Step3: find the  contour
contour, hirearchy = cv2.findContours(img_canny.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

# step 4: find the length of contour
print(f" Length of the contour = {(str(len(contour)))}")

for con in contour:
    area = cv2.contourArea(con)

    # step 5: Draw the contour
    img_copy = img.copy()
    cv2.drawContours(img_copy,con,-1, (0,255,0),4)

    # find the arc lenght of contour
    prepi = cv2.arcLength(con,True)

cv2.imshow("contour",img_copy)
cv2.waitKey(0)