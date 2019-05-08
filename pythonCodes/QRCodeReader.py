'''
Created on 21-Mar-2019

@author: Gopinath Jayakumar
'''
import cv2

import numpy as np
import pyzbar.pyzbar as pyzbar


img = cv2.imread("D:\\QR Code\\sample.png", 0)

decodedObject = pyzbar.decode(img)

for obj in decodedObject:
    print("Data: ", obj.data)

cv2.imshow('Image', img)
cv2.waitKey(0)

if __name__ == '__main__':
    pass
