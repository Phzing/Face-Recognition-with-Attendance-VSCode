import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

path = 'facesToLookFor'
images = []
classNames = []
myList = os.listdir(path)
print(myList)

for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0]) # append file name with file type excluded
print(classNames)

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return  encodeList

def markAttendance(name):
    with open('env/Attendance.csv','r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dateTimeString = now.strftime('%H:%M:%S')
            f.writelines(f'/n{name},{dateTimeString}')

knownFacesEncodeList = findEncodings(images)
print('Encoding complete')

# Use webcam to look for encoded faces
cap = cv2.VideoCapture(0)


while True:
    success, img = cap.read()
    imgSmall = cv2.resize(img,(0,0),None,0.25,0.25) # Make image smaller to increase efficiency
    imgSmall = cv2.cvtColor(imgSmall,cv2.COLOR_BGR2RGB)

    facesInCurFrame = face_recognition.face_locations(imgSmall)
    curFrameEncodings = face_recognition.face_encodings(imgSmall,facesInCurFrame)

    for encodeFace,faceLocation in zip(curFrameEncodings,facesInCurFrame):
        matches = face_recognition.compare_faces(knownFacesEncodeList,encodeFace)
        faceDistance = face_recognition.face_distance(knownFacesEncodeList,encodeFace)

        matchIndex = np.argmin(faceDistance) # index of closest matching image to face on webcam
        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            #print(name)
            y1,x2,y2,x1 = faceLocation
            y1,x2,y2,x1 = y1*4,x2*4,y2*4,x1*4 # undo down-scaling from above
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            markAttendance(name)

    cv2.imshow('Webcam',img)
    cv2.waitKey(1)
