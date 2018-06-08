#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/8 10:59
# @Author  : zhuo_hf@foxmail.com
# @Site    : 
# @File    : Test_Server.py
# @Software: PyCharm
import socket
import cv2
import os,sys,pygame
#from pygame.locals import *
import numpy

svrsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
svrsocket.bind(("192.168.0.8", 6000))
print("Start the service ....")
while 1:
    stringData, address = svrsocket.recvfrom(65500)
    #print("recv the data={}".format(len(stringData)))
    data = numpy.fromstring(stringData, dtype='uint8')
    img = cv2.imdecode(data, 1)
    cv2.imshow("Dst Img", img)  # 显示处理后的函数
    if cv2.waitKey(10) & 0xff == 27: # ESC键
        break

svrsocket.close()
cv2.destroyAllWindows()
