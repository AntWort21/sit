import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cv2.startWindowThread()
capture = cv2.VideoCapture(0)

while(True):
    ret, frame = capture.read()
    frame = cv2.resize(frame, (640, 480))
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    detected_face = face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5)
    
    for x, y, w, h in detected_face:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)
 

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
# out.release()
cv2.destroyAllWindows()
cv2.waitKey(1)