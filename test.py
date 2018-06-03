import cv2
import datetime
import os
from face import *

timeF = 10
OUTPUT_DIR = "image"

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
c = 1

def deal_img(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    if len(faces) > 0:
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.rectangle(img, (0,img.shape[0] - 25),(270, img.shape[0]), (255,255,255), -1)
    cv2.putText(img, "Number of faces detected: " + str(len(faces)), (0,img.shape[0] - 10), cv2.FONT_HERSHEY_TRIPLEX,
                0.5,  (0,0,0), 1)
    return img


while True:
    ret,img = cap.read()
    output_dir = os.path.join(
        OUTPUT_DIR, datetime.datetime.now().strftime('%H_%M_%S'))

    if c % timeF == 0:
        cv2.imwrite(output_dir + '.jpg',img)
        information = face(output_dir + '.jpg')
        if len(information) > 0:
            print(information)
            print("Age:{}".format(information[0]["age"]))
        c = 1
    c += 1
    img = deal_img(img)
    cv2.imshow('img',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
