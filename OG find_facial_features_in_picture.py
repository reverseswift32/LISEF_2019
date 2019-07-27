# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 14:36:55 2019

@author: LabCollin
"""

from PIL import Image, ImageDraw
import face_recognition



# Load the jpg file into a numpy array
ffimage = face_recognition.load_image_file("DeleteME.jpg")
#ffimage = face_recognition.load_image_file("Voldemort.jpg")

# Find all facial features in all the faces in the image
face_landmarks_list = face_recognition.face_landmarks(ffimage)

print("I found {} face(s) in this photograph.".format(len(face_landmarks_list)))

# Create a PIL imagedraw object so we can draw on the picture
pil_image = Image.fromarray(ffimage)
d = ImageDraw.Draw(pil_image)

for face_landmarks in face_landmarks_list:

    # Print the location of each facial feature in this image
    #for facial_feature in face_landmarks.keys():
    #    print("The {} in this face has the following points: {}".format(facial_feature, face_landmarks[facial_feature]))

    c = 0
    # Let's trace out each facial feature in the image with a line!
    for facial_feature in face_landmarks.keys():
        print(facial_feature)
        if(c != -1):
            d.line(face_landmarks[facial_feature], width=5)
            print("The {} in this face has the following points: {}".format(facial_feature, face_landmarks[facial_feature]))
        c += 1
        

    
# Show the picture
pil_image.show()


def drawFacialFeatures():
    myList = [1, 2, 3, 4, 5, 6]
    picture = None
    
    # Load the jpg file into a numpy array
    picture = face_recognition.load_image_file("Collin Li.jpg")
    
    # Find all facial features in all the faces in the image
    face_landmarks_list = face_recognition.face_landmarks(picture)
    
    print("I found {} face(s) in this photograph.".format(len(face_landmarks_list)))
    
    # Create a PIL imagedraw object so we can draw on the picture
    image_image = Image.fromarray(picture)
    d = ImageDraw.Draw(image_image)
    
    i = 0
    
    for face_landmarks in face_landmarks_list:
    
            
        # Let's trace out each facial feature in the image with a line!
        print("hi", end = "\n \n")
        print(i)
        for facial_feature in face_landmarks.keys():
            if i in myList: 
                d.line(face_landmarks[facial_feature], width=5)
            i += 1
    
    # Show the picture
    image_image.show()
    
    return image_image

dd = drawFacialFeatures()