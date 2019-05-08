'''
Created on 21-Mar-2019

@author: Gopinath Jayakumar
'''

import cv2

import numpy as np
import pyzbar.pyzbar as pyzbar


cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_DUPLEX

while True:
    _, frame = cap.read()
    decodedObject = pyzbar.decode(frame)
    
    for obj in decodedObject:
        # print("Data: ", obj.data)
        cv2.putText(frame, str(obj.data), (50, 50), font, 3, (255, 0, 0), 3)    
    
    cv2.imshow("Frame", frame)    
    key = cv2.waitKey(1)    
    
    if key == 27:
        break
    
if __name__ == '__main__':
    pass
