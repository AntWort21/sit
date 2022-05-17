import cv2
import numpy as np
import time

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cv2.startWindowThread()
capture = cv2.VideoCapture(0)

# out = cv2.VideoWriter(
#     'faceDetectionOutput.avi',
#     cv2.VideoWriter_fourcc(*'MJPG'),
#     15.,
#     (640,480)
# )

found = 0
notFound = 0

while(True):

    ret, frame = capture.read()

    frame = cv2.resize(frame, (640, 480))
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    detected_face = face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5)
    
    if(len(detected_face) > 0):
        for x, y, w, h in detected_face:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)
            found+=1
            notFound = 0 #if face is detected, reset notFound
            if found == 80:
                print("Occupied") #send the data somewhere, then break the program
    else:
        notFound += 1
        found = 0 #if face is not detected, reset found
        if notFound == 80:
            print("Vacant")
    
        # time.sleep(10)
        # print("output")
        #output 1 and 0 where face is detected and then save it into a notepad file
        #the result from notepad connect it to the android application
    

    # out.write(frame.astype('uint8'))
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
# out.release()
cv2.destroyAllWindows()
cv2.waitKey(1)