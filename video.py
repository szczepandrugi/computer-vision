import numpy as np
import os.path
import cv2
import win32api, win32con
from win32api import GetSystemMetrics

screenW = GetSystemMetrics(0)
screenH = GetSystemMetrics(1)

haarcascades = os.path.abspath(os.path.join(os.path.expandvars('%OPENCV_DIR%'), os.pardir, os.pardir, 'etc/haarcascades'))
face_cascade = cv2.CascadeClassifier(os.path.abspath(os.path.join(haarcascades,'haarcascade_frontalface_default.xml')))
eye_cascade = cv2.CascadeClassifier(os.path.abspath(os.path.join(haarcascades,'haarcascade_eye.xml')))

cap = cv2.VideoCapture(0)
width = cap.get(3)
height = cap.get(4)

font = cv2.FONT_HERSHEY_SIMPLEX

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    frame = cv2.flip( frame, 1 )

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)

        # find denter of face rect
        nx = x + (w/2)
        ny = y + (y/2)

        procx = nx/width*100
        procy = ny/height*100
        mouseX = int(round(screenW*procx/100))
        mouseY = int(round(screenH*procy/100))
        # mouse move
        win32api.SetCursorPos((mouseX,mouseY))

        msg = "%s, %s" % (nx,ny)
        cv2.putText(frame, msg, (x+w+4,y), font, .4, (244,255,200), 1, cv2.LINE_AA)
        msg = "%s%%, %s%%" % (int(round(procx)),int(round(procy)))
        cv2.putText(frame, msg, (x+w+4,y+16), font, .4, (244,255,200), 1, cv2.LINE_AA)

        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    # Display the resulting frame
    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
