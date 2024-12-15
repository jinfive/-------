import cv2
import numpy as np
import sys

cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    #frame=cv2.flip(frame,1)
    if ret:
        try:
            cv2.imshow('video',frame)

        except Exception as e:
            print(e)
    if cv2.waitKey(1)&0xff==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()