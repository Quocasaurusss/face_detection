# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 05:47:57 2020

@author: Quocamole
"""

import cv2 as cv
import serial
from time import sleep

vid = cv.VideoCapture(0)
ser = serial.Serial('COM3', 9600)

while (True) :
    ret, frame = vid.read()
    face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_alt.xml')
    found = face_cascade.detectMultiScale(frame, minSize=(20, 20))
    amount_found = len(found)
    if amount_found > 0:
        ser.write('1'.encode('utf-8'))
        sleep(0.1)
        for (x, y, height, width) in found:
            cv.rectangle(frame,  (x, y), (x + height, y + width), (0, 255, 0), 2)
    else:
        ser.write('0'.encode('utf-8'))
        sleep(0.1)
    cv.imshow('frame', frame)
    if (cv.waitKey(1) & 0xFF == ord('o')):
        break
    

    
vid.release()
cv.destroyAllWindows()
    