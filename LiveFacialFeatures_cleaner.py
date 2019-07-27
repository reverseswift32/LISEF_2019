# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 11:06:47 2019

@author: LabCollin
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 14:44:44 2019

@author: LabCollin
"""

msg = "Hello World!"
print(msg)
print("Loading...")
import numpy as np
import cv2
import dlib
from PIL import Image, ImageDraw
import PIL.ImageOps
import face_recognition
import keyboard
import os
import time 
import math



# the plan for maxmax and minmin is to return a pair of the largest or smallest values (largest/smallest x, largest/smallest y)

def maxmax(ll):
    a = -1
    b = -1      
    for ii in ll:
        a = max(a, ii[0])
        b = max(b, ii[1])
    return [a, b]
    
def minmin(ll):
    a = 99999
    b = 99999
    for ii in ll:
        a = min(a, ii[0])
        b = min(b, ii[1])
    return [a, b]


# pA should be (x1, y1, x2, y2)
def crop(pA, name, prevName = "theOG.jpg"):

    area = correctCord(pA)
    
    
    imgg = Image.fromarray(face_recognition.load_image_file(prevName))
    cropped_imgg = imgg.crop(area)
    cropped_imgg.show()
    cropped_imgg.save(name)   # save frame as JPEG file  

# will arrange the cordinates
def correctCord(pA):
    return [ min(pA[0], pA[2]), min(pA[1], pA[3]), max(pA[0], pA[2]), max(pA[1], pA[3]) ]
    
# nose1 = (x1, y1), nose2 = (x2, y2), nose1 and nose2 are cordinates to the top and bottom ends of noseline
def actuallyRotate(iimage = "theOG.jpg", line = True):
    
    nose1 = [-1, -1]
    nose2 = [-1, -1]
    

    # Load the jpg file into a numpy array
    ffimage = face_recognition.load_image_file(iimage)
    
    # Find all facial features in all the faces in the image
    face_landmarks_list = face_recognition.face_landmarks(ffimage)
    
    if(len(face_landmarks_list) >= 2):
        print("NOOOOOO", len(face_landmarks_list))
    
    for face_landmarks in face_landmarks_list:
        print(face_landmarks)
    
        # Print the location of each facial feature in this image
        #for facial_feature in face_landmarks.keys():
        #    print("The {} in this face has the following points: {}".format(facial_feature, face_landmarks[facial_feature]))
        aarray = face_landmarks["nose_bridge"]
        nose1 = aarray[0]
        nose2 = aarray[ len(aarray)-1 ]
        
        # indented below
    
        colorImage = Image.open("theOG.jpg")
            
        if(line):
            IWillDrawOnYou = Image.fromarray(ffimage)
            ddd = ImageDraw.Draw(IWillDrawOnYou)
            bothNose1Nose2 = []
            bothNose1Nose2.append(nose1)
            bothNose1Nose2.append(nose2)
            ddd.line(bothNose1Nose2, fill = (3, 198, 252))
            IWillDrawOnYou.save("noseLineDrawn.jpg")
            colorImage = Image.open("noseLineDrawn.jpg")
            
        
        
        
        # Rotate it by x degrees
        rotated = colorImage.rotate(tellMeAngle(nose1, nose2))
        
        # rotated.show()
        
        # endProduct will be the image with lines
        endProduct = rotated
        
        endProduct.show()
        
        endProduct.save("afterRotate_img.jpg")
        
        # line is a boolean that identifies if the horizontal line will be drawn   
        drawFacialFeatures("afterRotate_img.jpg", line, nose1, nose2)
    
    
# noseTop = (x1, y1), noseBottom = (x2, y2); they are the coordinates of the top and bottom ends of nose line
def tellMeAngle(noseTop, noseBottom):
    x1 = int(noseTop[0])
    y1 = int(noseTop[1])
    x2 = int(noseBottom[0])
    y2 = int(noseBottom[1])
    
    height = abs(y1-y2)
    side = abs(x1-x2)
    
    if(side == 0):
        side = 1
    
    inRad = math.atan(side/height)
    inDeg = math.degrees(inRad)
    final = inDeg # this cus this is correct, look at drawings lol
        
    
    if(x1 > x2): # this means slanting down left / since top x is farther to x = 0 than bottom x (x wise)
        return final
        
    elif(x1 < x2): # this means slanting down right \ since top x is closer to x = 0 than bottom x (x wise)
        return -final # i mean i guess i could have done -1 * final butt...
    
    else: #this means no tilt
        return 0
    return 0 # idk why here but here because i do this in java soo... GET RECT-Collin at 12 oclock at night
    

# iimagee = (the picture)"blablabla.jpg", line = (boolean) true
# THIS IS ONE OF THE MOST IMPORTANT PROGRAMS CUZ IT WILL CROP EYES TOO
def drawFacialFeatures(iimagee, line, nose1, nose2, myList = [1, 2, 3, 4, 5, 6]):
    
    # Load the jpg file into a numpy array
    picture = face_recognition.load_image_file("afterRotate_img.jpg")
    
    # Find all facial features in all the faces in the image
    face_landmarks_list = face_recognition.face_landmarks(picture)
    
    print("In \"drawFacialFeatures\", I found {} face(s) in this photograph.".format(len(face_landmarks_list)))
    

    
    i = 0
    
    for face_landmarks in face_landmarks_list:
        # Create a PIL imagedraw object so we can draw on the picture
        # The reason we don't use theOG.jpg here cuz iimagee has a nose line on it (and we want it)
        gonnaDrawOnU = face_recognition.load_image_file(iimagee)
        image_image = Image.fromarray(gonnaDrawOnU)
        d = ImageDraw.Draw(image_image)
        
        theSquare = [-1, -1, -1, -1]
        leftEyeBox = [-1, -1, -1, -1]
        rightEyeBox = [-1, -1, -1, -1]
    
       
        
        # we actually just need the y coordinate of nose2
        nose2y = -1
        
        # Print the location of each facial feature in this image
        for facial_feature in face_landmarks.keys():
            ll = []
            if i in myList: 
                ll.append(face_landmarks[facial_feature])
                d.line(face_landmarks[facial_feature], fill = (67, 9, 184), width=2)
                
                print(facial_feature, ll)
                ll = ll[0]
                print(facial_feature, "2", ll)
                
                # For top_Left, Left Eyebrow
                # we want the smallest so start big
                
                if (i == 1):
                    theSquare[0] = minmin(ll)[0]
                    theSquare[1] = minmin(ll)[1]
                    leftEyeBox[0] = minmin(ll)[0]
                    leftEyeBox[1] = minmin(ll)[1]
                    
                            
                # For bottom_right, x = farthest Right right_eyebrow && y = farthest(bottomest) nose line (vertical)
                # we want largest so start small
                
                # Right eyebrow so for x
                if (i == 2):
                    theSquare[2] = maxmax(ll)[0]
                    rightEyeBox[0] = maxmax(ll)[0]
                    rightEyeBox[1] = minmin(ll)[1]
            
                # Nose Tip so for y
                if (i == 3):
                    # apperently, there is always 4 pairs (8 total numbers) for the 4 lines that make up the nose tip
                    #   soo... the plan is to create something known as a "slope" that will determine for every 
                    #   one unit to the right, the variable 'slope' will determine how much down (or up)
                    # - if slope is negative, it means the line is like this: /
                    # - if slope is positive, it means the line is like this: \
                    
                    nose2y = maxmax(ll)[1]
                    theSquare[3] = maxmax(ll)[1]
                    leftEyeBox[2] = maxmax(ll)[0]
                    leftEyeBox[3] = maxmax(ll)[1]
                    rightEyeBox[2] = minmin(ll)[0]
                    rightEyeBox[3] = maxmax(ll)[1]
                
                        
                        
            i += 1
            
        if(line):
            d.line((0, nose2y, 9999, nose2y))
        d.rectangle(theSquare, fill=None, outline="white")    
        d.rectangle(leftEyeBox, fill=None, outline="white")
        d.rectangle(rightEyeBox, fill=None, outline="white")
       
    # Show the picture
    image_image.show()
    
    return image_image










capture = cv2.VideoCapture(0)
detector = dlib.get_frontal_face_detector();
#print(capture.isOpened())

print("Starting...")
fIsPressed = False
while True:
    
    
    
    ret, frame = capture.read()
    cv2.imshow('frame',frame)
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detector(gray)
        numOfFaces = 0
        for face in faces:
            numOfFaces += 1
            x1,y1 = face.left(), face.top()
            x2,y2 = face.right(), face.bottom()
            
            horizSide = abs(x1 - x2)
            vertiSide = abs(y1 - y2)
            
            
            # the larger the number, the smaller the size is extended
            howMuchBigger = 4
            
            x1 -= horizSide / (howMuchBigger) 
            x2 += horizSide / (howMuchBigger)
            y1 -= vertiSide / (howMuchBigger) * 2
            y2 += vertiSide / (howMuchBigger) * 0.5
            
            x1 = int(x1)
            x2 = int(x2)
            y1 = int(y1)
            y2 = int(y2)
            
            name = str(numOfFaces) + ".jpg"
            
            cv2.rectangle(frame, (x1,y1), (x2,y2),(0.255,0),3)
            
            if(fIsPressed): 
                print(numOfFaces)
                crop((x1, y1, x2, y2), name)
                
                # this is going to do literally everything
                # just check the folder (with images) for eyebags, lines, drawings, etc
                actuallyRotate(iimage = name)
            
    fIsPressed = False
        

          
    if (keyboard.is_pressed('f') and not ret):
        print("no face detected")
    
    if (keyboard.is_pressed('f') and ret):
        print("face(s) being processed")
        fIsPressed = True
        success,image = capture.read()
        theOGimage = image
        #cv2.imwrite("orginall1_%d.jpg" % count, image)     # save frame as JPEG file  
        cv2.imwrite("theOG.jpg", image)     # save frame as JPEG file  
        # HEYYYYYYYYYYY WHYYYYYYYYYYYYY AMMMMMMMMMMMMMMM I COMMMMMMMENTTTEDDDDDDD OUTTTTTTTTTTTTT
        #actuallyRotate()
     
              
    # Display the resulting frame
    #cv2.imshow('gray',gray)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 


# When everything done, release the capture
capture.release()
cv2.destroyAllWindows()


