#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/8 10:59
# @Author  : zhuo_hf@foxmail.com
# @Site    : 
# @File    : Test_Server.py
# @Software: PyCharm
import socket
#import Image
import os,sys,pygame
#from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((320,240))
pygame.display.set_caption("web cam")

pygame.display.flip()
svrsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
svrsocket.bind(("10.125.156.227", 6000))
clock = pygame.time.Clock()    #计算帧速
while 1:
    print("Start the service ....")
    data, address = svrsocket.recvfrom(80000*4)
    print("recv the data")
    camshot = pygame.image.frombuffer(data, (320,240), "RGB")
    for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
    screen.blit(camshot, (0,0))
    pygame.display.update()
    print(clock.get_fps())    #在终端打印帧速
    clock.tick()