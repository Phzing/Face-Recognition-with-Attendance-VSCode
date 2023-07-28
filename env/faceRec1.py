import cv2
import numpy as np
import face_recognition

imgBill = face_recognition.load_image_file('imagesMain/Bill Gates.jpg')
imgBill = cv2.cvtColor(imgBill,cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file('imagesMain/Bill Gates Test.jpg')
imgTest = cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)

faceLocation = face_recognition.face_locations(imgBill)[0]
encodeBill = face_recognition.face_encodings(imgBill)[0]
cv2.rectangle(imgBill,(faceLocation[3],faceLocation[0]),(faceLocation[1],faceLocation[2]),(255,0,255),2)

faceLocationTest = face_recognition.face_locations(imgTest)[0]
encodeTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest,(faceLocationTest[3],faceLocationTest[0]),(faceLocationTest[1],faceLocationTest[2]),(255,0,255),2)

results = face_recognition.compare_faces([encodeBill],encodeTest)
faceDistance = face_recognition.face_distance([encodeBill],encodeTest)
print(results,faceDistance)
cv2.putText(imgTest, f'{results} {round(faceDistance[0],2)}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255,),2)

cv2.imshow('Bill Gates', imgBill)
cv2.imshow('Bill Gates Test', imgTest)
cv2.waitKey(0)
