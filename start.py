import numpy as np
import os.path
import cv2

# imagePath = 'img/img.jpg'
imagePath = 'img/IMG_4115.JPG'
haarcascades = os.path.abspath(os.path.join(os.path.expandvars('%OPENCV_DIR%'), os.pardir, os.pardir, 'etc/haarcascades'))
face_cascade = cv2.CascadeClassifier(os.path.abspath(os.path.join(haarcascades,'haarcascade_frontalface_default.xml')))
eye_cascade = cv2.CascadeClassifier(os.path.abspath(os.path.join(haarcascades,'haarcascade_eye.xml')))

img = cv2.imread(imagePath)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
cv2.imwrite('img/save-2.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
