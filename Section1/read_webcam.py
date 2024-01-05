import cv2

cap = cv2.VideoCapture(0)
cap.set(3,640) # width
cap.set(4,480) # height
cap.set(10,100)
while True:
    success, frame = cap.read()

    if success:
        cv2.imshow("Car",frame)
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()