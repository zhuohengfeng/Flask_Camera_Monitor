#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/8 10:59
# @Author  : zhuo_hf@foxmail.com
# @Site    : 
# @File    : Test_Client.py
# @Software: PyCharm
import socket
import cv2
#import Image
#from VideoCapture import Device
#cam = Device()
#cam.setResolution(320,240)
clisocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
cap = cv2.VideoCapture(0)
while 1:
    #im = cam.getImage()
    #im = im.resize((160,120))
    #da = im.tostring()
    ret, frame = cap.read()
    print(frame.shape)
    dst = cv2.resize(frame, (160, 120))
    print(dst.shape)
    clisocket.sendto(dst, ("127.0.0.1", 1234))
s.close()