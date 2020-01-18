import cv2
import os
import numpy
root_path="./gtx/"
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
im=cv2.imread('1.jpg')

# cv2.rectangle(im, (0, 0), (200, 200), (255, 255, 0), 2)



grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
cv2.imwrite('grey.jpg',grey)
faces = face_detector.detectMultiScale(grey)
for x,y,w,h in faces:
    cv2.rectangle(grey,(x,y),(x+w,y+h),(255,255,0),2)
cv2.imshow('grey',grey)
cv2.waitKey(0)
cv2.destroyAllWindows()
