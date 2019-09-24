import cv2
import numpy as np
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

servo_alis_ki = GPIO.PWM(14, 100)
servo_alis_ka = GPIO.PWM(15, 100)
servo_mata_hor = GPIO.PWM(18, 100)
servo_mata_ver = GPIO.PWM(23, 100)
servo_telinga_ki = GPIO.PWM(24, 100)
servo_telinga_ka = GPIO.PWM(25, 100)
servo_mulut_ats_ki = GPIO.PWM(8, 100)
servo_mulut_ats_ka = GPIO.PWM(7, 100)
servo_mulut_bwh_ki = GPIO.PWM(12, 100)
servo_mulut_bwh_ka = GPIO.PWM(16, 100)
servo_leher_hor = GPIO.PWM(20, 100)
servo_leher_ver = GPIO.PWM(21, 100)

servo_alis_ki.start(30)
servo_alis_ka.start(30)
servo_mata_hor.start(30)
servo_mata_ver.start(30)
servo_telinga_ki.start(45)
servo_telinga_ka.start(45)
servo_mulut_ats_ki.start(30)
servo_mulut_ats_ka.start(30)
servo_mulut_bwh_ki.start(30)
servo_mulut_bwh_ka.start(30)
servo_leher_hor.start(0)
servo_leher_ver.start(90)

def senyum():
    s1= float(30) / 10.0 + 2.5
    servo_alis_ki.ChangeDutyCycle(s1)
    s2= float(30) / 10.0 + 2.5
    servo_alis_ka.ChangeDutyCycle(s2)
    s3= float(30) / 10.0 + 2.5
    servo_mata_hor.ChangeDutyCycle(s3)
    s4= float(30) / 10.0 + 2.5
    servo_mata_ver.ChangeDutyCycle(s4)
    s5= float(45) / 10.0 + 2.5
    servo_telinga_ki.ChangeDutyCycle(s5)
    s6= float(45) / 10.0 + 2.5
    servo_telinga_ka.ChangeDutyCycle(s6)
    s7= float(90) / 10.0 + 2.5
    servo_mulut_ats_ki.ChangeDutyCycle(s7)
    s8= float(0) / 10.0 + 2.5
    servo_mulut_ats_ka.ChangeDutyCycle(s8)
    s9= float(0) / 10.0 + 2.5
    servo_mulut_bwh_ki.ChangeDutyCycle(s9)
    s10= float(90) / 10.0 + 2.5
    servo_mulut_bwh_ka.ChangeDutyCycle(s10)    
    s11= float(0) / 10.0 + 2.5
    servo_leher_hor.ChangeDutyCycle(s11)
    s12= float(90) / 10.0 + 2.5
    servo_leher_ver.ChangeDutyCycle(s12)

def marah():
    s1= float(60) / 10.0 + 2.5
    servo_alis_ki.ChangeDutyCycle(s1)
    s2= float(0) / 10.0 + 2.5
    servo_alis_ka.ChangeDutyCycle(s2)
    s3= float(30) / 10.0 + 2.5
    servo_mata_hor.ChangeDutyCycle(s3)
    s4= float(30) / 10.0 + 2.5
    servo_mata_ver.ChangeDutyCycle(s4)
    s5= float(0) / 10.0 + 2.5
    servo_telinga_ki.ChangeDutyCycle(s5)
    s6= float(90) / 10.0 + 2.5
    servo_telinga_ka.ChangeDutyCycle(s6)
    s7= float(20) / 10.0 + 2.5
    servo_mulut_ats_ki.ChangeDutyCycle(s7)
    s8= float(15) / 10.0 + 2.5
    servo_mulut_ats_ka.ChangeDutyCycle(s8)
    s9= float(40) / 10.0 + 2.5
    servo_mulut_bwh_ki.ChangeDutyCycle(s9)
    s10= float(10) / 10.0 + 2.5
    servo_mulut_bwh_ka.ChangeDutyCycle(s10)    
    s11= float(0) / 10.0 + 2.5
    servo_leher_hor.ChangeDutyCycle(s11)
    s12= float(90) / 10.0 + 2.5
    servo_leher_ver.ChangeDutyCycle(s12)

def sedih():
    s1= float(0) / 10.0 + 2.5
    servo_alis_ki.ChangeDutyCycle(s1)
    s2= float(60) / 10.0 + 2.5
    servo_alis_ka.ChangeDutyCycle(s2)
    s3= float(60) / 10.0 + 2.5
    servo_mata_hor.ChangeDutyCycle(s3)
    s4= float(0) / 10.0 + 2.5
    servo_mata_ver.ChangeDutyCycle(s4)
    s5= float(90) / 10.0 + 2.5
    servo_telinga_ki.ChangeDutyCycle(s5)
    s6= float(0) / 10.0 + 2.5
    servo_telinga_ka.ChangeDutyCycle(s6)
    s7= float(0) / 10.0 + 2.5
    servo_mulut_ats_ki.ChangeDutyCycle(s7)
    s8= float(90) / 10.0 + 2.5
    servo_mulut_ats_ka.ChangeDutyCycle(s8)
    s9= float(90) / 10.0 + 2.5
    servo_mulut_bwh_ki.ChangeDutyCycle(s9)
    s10= float(0) / 10.0 + 2.5
    servo_mulut_bwh_ka.ChangeDutyCycle(s10)    
    s11= float(0) / 10.0 + 2.5
    servo_leher_hor.ChangeDutyCycle(s11)
    s12= float(90) / 10.0 + 2.5
    servo_leher_ver.ChangeDutyCycle(s12)

def kaget():
    s1= float(0) / 10.0 + 2.5
    servo_alis_ki.ChangeDutyCycle(s1)
    s2= float(60) / 10.0 + 2.5
    servo_alis_ka.ChangeDutyCycle(s2)
    s3= float(30) / 10.0 + 2.5
    servo_mata_hor.ChangeDutyCycle(s3)
    s4= float(30) / 10.0 + 2.5
    servo_mata_ver.ChangeDutyCycle(s4)
    s5= float(0) / 10.0 + 2.5
    servo_telinga_ki.ChangeDutyCycle(s5)
    s6= float(90) / 10.0 + 2.5
    servo_telinga_ka.ChangeDutyCycle(s6)
    s7= float(10) / 10.0 + 2.5
    servo_mulut_ats_ki.ChangeDutyCycle(s7)
    s8= float(90) / 10.0 + 2.5
    servo_mulut_ats_ka.ChangeDutyCycle(s8)
    s9= float(0) / 10.0 + 2.5
    servo_mulut_bwh_ki.ChangeDutyCycle(s9)
    s10= float(90) / 10.0 + 2.5
    servo_mulut_bwh_ka.ChangeDutyCycle(s10)    
    s11= float(0) / 10.0 + 2.5
    servo_leher_hor.ChangeDutyCycle(s11)
    s12= float(90) / 10.0 + 2.5
    servo_leher_ver.ChangeDutyCycle(s12)

def datar():
    s1= float(30) / 10.0 + 2.5
    servo_alis_ki.ChangeDutyCycle(s1)
    s2= float(30) / 10.0 + 2.5
    servo_alis_ka.ChangeDutyCycle(s2)
    s3= float(30) / 10.0 + 2.5
    servo_mata_hor.ChangeDutyCycle(s3)
    s4= float(30) / 10.0 + 2.5
    servo_mata_ver.ChangeDutyCycle(s4)
    s5= float(45) / 10.0 + 2.5
    servo_telinga_ki.ChangeDutyCycle(s5)
    s6= float(45) / 10.0 + 2.5
    servo_telinga_ka.ChangeDutyCycle(s6)
    s7= float(30) / 10.0 + 2.5
    servo_mulut_ats_ki.ChangeDutyCycle(s7)
    s8= float(30) / 10.0 + 2.5
    servo_mulut_ats_ka.ChangeDutyCycle(s8)
    s9= float(30) / 10.0 + 2.5
    servo_mulut_bwh_ki.ChangeDutyCycle(s9)
    s10= float(30) / 10.0 + 2.5
    servo_mulut_bwh_ka.ChangeDutyCycle(s10)    
    s11= float(0) / 10.0 + 2.5
    servo_leher_hor.ChangeDutyCycle(s11)
    s12= float(90) / 10.0 + 2.5
    servo_leher_ver.ChangeDutyCycle(s12)

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
            senyum()
        elif(id==2):
            id="Marah"
            marah()
        elif(id==3):
            id="Sedih"
            sedih()
        elif(id==4):
            id="Kaget"
            kaget()
        elif(id==5):
            id="Datar"
            datar()
        cv2.cv.PutText(cv2.cv.fromarray(img),str(id),(x,y+h),font,225);
    cv2.imshow("Face",img);
    if(cv2.waitKey(1)==ord('q')):
        break;
cam.release()
cv2.destroyAllWindows
