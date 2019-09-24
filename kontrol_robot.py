import cv2
import numpy as np
import serial           # import libarary serial


arduino = serial.Serial("COM37", 9600)

faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
cam=cv2.VideoCapture(0);
rec=cv2.createLBPHFaceRecognizer();
rec.load("recognizer\\trainningData.yml")
id=0
font=cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL,3,1,0,2)
while(True):
    ret,img=cam.read();
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray,1.3,5);
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,225),2)
        id,conf=rec.predict(gray[y:y+h,x:x+w])
        if(id==1):
            id="Senyum"
            arduino.write('f')
        elif(id==2):
            id="Marah"
            arduino.write('r')
        elif(id==3):
            id="Sedih"
            arduino.write('l')
        elif(id==4):
            id="Kaget"
            arduino.write('b')
        elif(id==5):
            id="Datar"
            arduino.write('d')
        cv2.cv.PutText(cv2.cv.fromarray(img),str(id),(x,y+h),font,225);
    cv2.imshow("Face",img);
    if(cv2.waitKey(1)==ord('q')):
        break;
cam.release()
cv2.destroyAllWindows
