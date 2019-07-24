# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 15:25:32 2019

@author: LabCollin
"""

from PIL import Image, ImageDraw
import face_recognition

# Load the jpg file into a numpy array
image = face_recognition.load_image_file("Collin Li.jpg")

# Find all facial features in all the faces in the image
face_landmarks_list = face_recognition.face_landmarks(image)

#below varables should all be ints
# LeftMost eyebrow line to RightMostBottom noseLine x2 (for right and left eye)
rightEye = {0, 0, 0, 0}
leftEye = {0, 0, 0, 0}


theSquare = []
rightEyeBox = []
leftEyeBox = []

ll = []

print("I found {} face(s) in this photograph.".format(len(face_landmarks_list)))

# Create a PIL imagedraw object so we can draw on the picture
pil_image = Image.fromarray(image)
d = ImageDraw.Draw(pil_image)


for face_landmarks in face_landmarks_list:

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
        ll.clear      
        
        if (s == 1  or s == 2 or s == 3 or s == 5 or s == 6):
            d.line(face_landmarks[facial_feature], width=10)
            ll.append(face_landmarks[facial_feature])
        
        # For top_Left, Left Eyebrow
        # we want the smallest so start big
        theX = 9999
        theY = 9999
        
        if (s == 1):
            for i in ll:
                for ii in i:
                    theX = min(theX, ii[0])
                    theY = min(theY, ii[1])
            theSquare.append(theX)
            theSquare.append(theY)
                    
        # For bottom_right, x = farthest Right right_eyebrow && y = farthest(bottomest) nose line (vertical)
        # we want largest so start small
        
        theX = 0
        theY = 0
        
        # Right eyebrow so for x
        if (s == 2):
            for i in ll:
                for ii in i:
                    theX = max(theX, ii[0])
            theSquare.append(theX)
        
        # Nose Tip so for y
        if (s == 3):
            for i in ll:
                for ii in i:
                    theY = max(theY, ii[1])
            theSquare.append(theY)
        
                    
                    
        s = s + 1
    
    #actually draw the big rectange for eye bags
    #print(theSquare)
    d.rectangle(theSquare, fill=None, outline="white")
    #d.line(theSquare, width = 10)
        

    # Left eyebrow = 1     *    
    # Right eyebrow = 2    *
    # Nose tip = 3         *
    # Right eye = 5
    # Left eye = 6

# Show the picture
pil_image.show()

