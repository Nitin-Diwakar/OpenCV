import cv2
import numpy as np

width = 940
height = 880

def preprocess_image(img):
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img_canny = cv2.Canny(img_gray, 450,600)
    kernel = np.ones((5,5), np.uint8)

    img_distance = cv2.dilate(img_canny,kernel,iterations=2)
    img_erosion = cv2.erode(img_distance, kernel, iterations=1)
    return img_erosion

def draw_contours(image):
    contour, hirearchy = cv2.findContours(image.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for con in contour:
        area = cv2.contourArea(con)
        print("Area:",area)
        maxArea = 0
        biggest = np.array([])
        if area > 5000:
            peri = cv2.arcLength(con, True)
            approx = cv2.approxPolyDP(con, 0.02*peri, True)
            if area > maxArea and len(approx) == 4:
                biggest = approx
    print("Biggest:",biggest)
    cv2.drawContours(img_contour, biggest, -1, (255,0,0),3)
    return biggest

def reorder(myPoints):
    myPoints = myPoints.reshape((4,2))
    myPointsNew = np.zeros((4,1,2),np.int32)

    add = myPoints.sum(1)
    myPointsNew[0] = myPoints[np.argmin(add)]
    myPointsNew[3] = myPoints[np.argmax(add)]
    diff = np.diff(myPoints, axis=1)
    myPointsNew[1] = myPoints[np.argmin(diff)]
    myPointsNew[2] = myPoints[np.argmax(diff)]

    return myPointsNew

def wrap_persceptive(img,biggest):
    biggest = reorder(biggest)
    pts1 = np.float32(biggest)
    pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
    matrix = cv2.getPerspectiveTransform(pts1,pts2)
    img_output = cv2.warpPerspective(img,matrix,(width,height))
    return img_output


img = cv2.imread("Images/documentscanner2.jpg")
# img_resize = cv2.resize(img,(640,400))
img_contour = img.copy()
process_img = preprocess_image(img)

biggest = draw_contours(process_img)
imgWarp = wrap_persceptive(img,biggest)
cv2.imshow("contour",img_contour)
cv2.imshow("Document",process_img)
cv2.imshow("warp",imgWarp)

cv2.waitKey(0)

cv2.destroyAllWindows()