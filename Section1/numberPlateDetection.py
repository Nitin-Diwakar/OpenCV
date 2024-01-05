import numpy as np
import cv2

cap = cv2.VideoCapture("Videos/demo.mp4")

numberplatecascade = cv2.CascadeClassifier("haarcascades/haarcascade_russian_plate_number.xml")
count =0
while True:
    sucess, frame = cap.read()
    if sucess:
        img_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        number_plate = numberplatecascade.detectMultiScale(img_gray,1.1, 10)
        for x,y,w,h in number_plate:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,255),3)
            cv2.putText(frame,"number plate",(x, y-5),cv2.FONT_HERSHEY_TRIPLEX,1, (0,255,0),2)
            frameROI = frame[y:y+h, x:x+w]
        cv2.imshow("Frame ROI", frameROI)
        cv2.imshow("Plate",frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.imwrite("Resources/NoPlate_" + str(count) + ".jpg",frameROI)
            cv2.waitKey(500)
            count = count+1
    else:
        break

