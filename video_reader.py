import cv2
import numpy as np

fullbody_cascade = cv2.CascadeClassifier('cars.xml')
cap = cv2.VideoCapture('videos/video1.avi')


while True:
    ret, frame =  cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    bodies = fullbody_cascade.detectMultiScale(gray, 1.1, 1)
    for (x, y, w, h) in bodies:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255,0,0), 2)
    cv2.imshow('frame', frame)
    # cv2.imshow('gray', gray)
    if(cv2.waitKey(30) & 0xFF == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()