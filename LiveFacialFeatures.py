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

msg = "Starting...!"
print(msg)
import numpy as np
import cv2
import dlib
from PIL import Image, ImageDraw
import PIL.ImageOps
import face_recognition
import keyboard
import os
import time 

capture = cv2.VideoCapture(0)
detector = dlib.get_frontal_face_detector();

success,image = capture.read()

theOGimage = image

count = 0


#below varables should all be ints
# LeftMost eyebrow line to RightMostBottom noseLine x2 (for right and left eye)
theSquare = []

rightEyeBox = []
leftEyeBox = []
    

# Collin's faceBags identification
def labelBags(iimage):
    

    iimage = face_recognition.load_image_file(iimage)

        
    # Find all facial features in all the faces in the image
    face_landmarks_list = face_recognition.face_landmarks(iimage)
    

    ll = []
    
    print("I found {} face(s) in this photograph.".format(len(face_landmarks_list)))
    
    # Create a PIL imagedraw object so we can draw on the picture
    pil_image = Image.fromarray(iimage)
    d = ImageDraw.Draw(pil_image)
    
    
    for face_landmarks in face_landmarks_list: 
        theSquare = [-1, -1, -1, -1]

        rightEyeBox = [-1, -1, -1, -1]
        leftEyeBox = [-1, -1, -1, -1]
        
        
    
            
    
        """
        # Print the location of each facial feature in this image
        for facial_feature in face_landmarks.keys():
            #print("The {} in this face has the following points: {}".format(facial_feature, face_landmarks[facial_feature]))
            print(facial_feature);
        """
    
        #s for section
        s = 0
        # Let's trace out each facial feature in the image with a line!
        for facial_feature in face_landmarks.keys():
    
            # just reseting ll (don't mind me)        
            ll = []    
            
            if (s == 1 or s == 2 or s == 3 or s == 5 or s == 6):
                d.line(face_landmarks[facial_feature], width=5)
                ll.append(face_landmarks[facial_feature])
                ll = ll[0]
                
          
            # For top_Left, Left Eyebrow
            # we want the smallest so start big
            
            if (s == 1):
                theSquare[0] = minmin(ll)[0]
                theSquare[1] = minmin(ll)[1]
                leftEyeBox[0] = minmin(ll)[0]
                leftEyeBox[1] = minmin(ll)[1]
                
                leftBrowL = [ ll [0]         [0], ll [0]         [1]]
                
                leftBrowR = [ ll [len(ll)-1] [0], ll [len(ll)-1] [1]]
                
                leftEyeBox[0] = leftBrowL[0]
                leftEyeBox[1] = leftBrowL[1]
                leftEyeBox[2] = leftBrowR[0]
                leftEyeBox[3] = leftBrowR[1]
                
                print("LEFT", ll)
                
                
                        
            # For bottom_right, x = farthest Right right_eyebrow && y = farthest(bottomest) nose line (vertical)
            # we want largest so start small
            
            
            # Right eyebrow so for x
            if (s == 2):
                theSquare[2] = maxmax(ll)[0]
                rightEyeBox[0] = maxmax(ll)[0]
                rightEyeBox[1] = minmin(ll)[1]
                
                rightBrowL = [ll[0][0], ll[0][1]]
                rightBrowR = [ll[len(ll)-1][0], ll[(len(ll)-1   )][1]]
                
                rightEyeBox[0] = rightBrowL[0]
                rightEyeBox[1] = rightBrowL[1]
                rightEyeBox[2] = rightBrowR[0]
                rightEyeBox[3] = rightBrowR[1]
                
                print("RIGHT", ll)
                
                 
            # Nose Tip so for y
            if (s == 3):
                # apperently, there is always 4 pairs (8 total numbers) for the 4 lines that make up the nose tip
                #   soo... the plan is to create something known as a "slope" that will determine for every 
                #   one unit to the right, the variable 'slope' will determine how much down (or up)
                # - if slope is negative, it means the line is like this: /
                # - if slope is positive, it means the line is like this: \
                
                
                noseTip0 = ll[0]
                noseTip3 = ll[len(ll)-1]
                
                x1 = (noseTip0[0])
                y1 = (noseTip0[1])
                
                x2 = (noseTip3[0])
                y2 = (noseTip3[1])
                print(ll)
                print(x1, y1, x2, y2)
                
                x1 = int(x1)
                y1 = int(y1)
                
                x2 = int(x2)
                y2 = int(y2)
                
                aaa = y1-y2
                bbb = x1-x2
                
                slope = 0
                if(bbb != 0):
                    slope = aaa / bbb
                print(slope + 0)
                
                
                
                
                
                theSquare[3] = maxmax(ll)[1]
                '''
                leftEyeBox[2] = maxmax(ll)[0]
                leftEyeBox[3] = maxmax(ll)[1]
                rightEyeBox[2] = minmin(ll)[0]
                rightEyeBox[3] = maxmax(ll)[1]
                print("The {} in this face has the following points: {}".format(facial_feature, face_landmarks[facial_feature]))
                print(ll)
                '''
                        
                        
            s = s + 1
            
        print("The Square:", theSquare)
        print("Right:", rightEyeBox)
        print("Left:", leftEyeBox)
        
        #actually draw the big rectange for eye bags
        #print(theSquare)
        d.rectangle(theSquare, fill=None, outline="white")
        
        #d.rectangle(rightEyeBox, fill=None, outline="white")
        #d.rectangle(leftEyeBox, fill=None, outline="white")
        
        #d.line(theSquare, width = 6)
        d.line(leftEyeBox, width = 6)
        d.line(rightEyeBox, width = 6)
                    
    
        # Left eyebrow = 1     * (left means left of picture, not person soo <--)
        # Right eyebrow = 2    * (Right means right of picture, not person soo -->)
        # Nose tip = 3         *
        # Right eye = 5
        # Left eye = 6
    
    
        '''
        imgg = Image.fromarray(face_recognition.load_image_file("theOG.jpg"))
        cropped_imgg = imgg.crop(correctCord(rightEyeBox))
        cropped_imgg.save("cropped_right.jpg")   # save frame as JPEG file  
        cropped_imgg.show()
        '''
        
            
        crop(theSquare, "cropped_all.jpg")
        
        #crop(rightEyeBox, "cropped_right.jpg")
        #crop(leftEyeBox, "croped_left.jpg")
        
         
        #cropped_imgg.show()
        
        #inverted_image = PIL.ImageOps.invert(cropped_imgg)
    
        #inverted_image.show()
        
        # Show the picture
        pil_image.show()

def maxmax(ll):
    a = -1
    b = -1
    for ii in ll:
        a = max(a, ii[0])
        b = max(b, ii[1])
    return [a, b]
    
def minmin(ll):
    a = 9999
    b = 9999
    for ii in ll:
        a = min(a, ii[0])
        b = min(b, ii[1])
    return [a, b]
        
def crop(pA, name, prevName = "theOG.jpg"):

    area = correctCord(pA)
    
    
    imgg = Image.fromarray(face_recognition.load_image_file(prevName))
    cropped_imgg = imgg.crop(area)
    cropped_imgg.show()
    cropped_imgg.save(name)   # save frame as JPEG file  


def correctCord(pA):
    return [ min(pA[0], pA[2]), min(pA[1], pA[3]), max(pA[0], pA[2]), max(pA[1], pA[3]) ]








#print(capture.isOpened())
print("ready...")
while True:
    

    ret, frame = capture.read()
    cv2.imshow("frame",frame)
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detector(gray)
        

        for face in faces:
            face_landmarks_list = face_recognition.face_landmarks(image)
            x1,y1 = face.left(), face.top()
            x2,y2 = face.right(), face.bottom()
            cv2.rectangle(frame, (x1,y1), (x2,y2),(0.255,0),3)
            

            if keyboard.is_pressed('f'):
                print('f')
                success,image = capture.read()
                theOGimage = image
                #cv2.imwrite("orginall1_%d.jpg" % count, image)     # save frame as JPEG file  
                cv2.imwrite("theOG.jpg", image)     # save frame as JPEG file  
                
                
                success,image = capture.read()
                cv2.imwrite("frame2.jpg", image)
                
                
                '''
                #start {
                
                # THIS WAS THE OLD ONE (7/22/2019)
                print("wait")
                time.sleep(3)
                print("ok")
                ffimage = face_recognition.load_image_file("theOG.jpg")
                
                # Find all facial features in all the faces in the image
                face_landmarks_list = face_recognition.face_landmarks(ffimage)
                
                print("I found {} face(s) in this photograph.".format(len(face_landmarks_list)))
                
                # Create a PIL imagedraw object so we can draw on the picture
                pil_image = Image.fromarray(ffimage)
                d = ImageDraw.Draw(pil_image)
                
                for face_landmarks in face_landmarks_list:
                
                    # Print the location of each facial feature in this image
                    for facial_feature in face_landmarks.keys():
                        print("The {} in this face has the following points: {}".format(facial_feature, face_landmarks[facial_feature]))
                
                    # Let's trace out each facial feature in the image with a line!
                    for facial_feature in face_landmarks.keys():
                        d.line(face_landmarks[facial_feature], width=5)
                
                # Show the picture
                pil_image.show()
                #end }
                '''
                
                labelBags("theOG.jpg")

                print("Read a new frame: ", success)
                count += 1
                
    
            
            
        # Display the resulting frame
            #cv2.imshow('gray',gray)
            cv2.imshow('frame',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
              break

# When everything done, release the capture
capture.release()
cv2.destroyAllWindows()

