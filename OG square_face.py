# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 14:44:44 2019

@author: LabCollin
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

msg = "Hello World!"
print(msg)
import numpy as np
import cv2
import dlib
capture = cv2.VideoCapture(0)
detector = dlib.get_frontal_face_detector();
#print(capture.isOpened())
while True:
    ret, frame = capture.read()
    cv2.imshow('frame',frame)
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detector(gray)
        for face in faces:
            x1,y1 = face.left(), face.top()
            x2,y2 = face.right(), face.bottom()
            cv2.rectangle(frame, (x1,y1), (x2,y2),(0.255,0),3)
            
            
        # Display the resulting frame
            cv2.imshow('gray',gray)
            cv2.imshow('frame',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
              break

# When everything done, release the capture
capture.release()
cv2.destroyAllWindows()


