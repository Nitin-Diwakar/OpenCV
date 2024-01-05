import cv2
import numpy as np

cap = cv2.VideoCapture(0)
face = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")
while True:
    sucess,frame = cap.read()

    if sucess:
        img_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = face.detectMultiScale(img_gray,1.1,4)

        for x,y,w,h in faces:
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0), 3)
        cv2.imshow("Camera",frame)

        if cv2.waitKey(1) & 0xFF==ord('1'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()