import pygame, sys, os
import time
from pygame.locals import *
from CPD import CPD
import numpy as np
from PIL import Image
from BSC import BSC
from CRC import CRC

simulationSpeed = 1 #1 - realtime
endToEndDelay = 5000 #5000ms
frameSize = 8
transmissionSpeed = 1

class SRController:

    def __init__(self):
        self.Timer = time.time()
        self.Timeout = 1
        self.ActualTransmitting = 0
        self.AmountTransmitting = 0
        self.Array = 0
        self.Frames = []
        self.Width = 0
        self.Height = 0
        self.frameCount = 0
        self.CorrectTransmitted = 0
        self.CPDTable = []
    def loadImg(self):
        img = Image.open("testimg.png")
        img.show()
        self.Array = np.array(img)
        self.Width, self.Height = img.size
        self.frameCount = self.Width*self.Height*3
    def recreateImg(self):
        temp=0
        for y in range (0, self.Height):
            for x in range (0, self.Width):
                for rgb in range (0, 3):
                    self.Array[y,x,rgb] = self.CPDTable[temp].Frame
                    temp+=1
                    
        imgSR = Image.fromarray(self.Array)
        imgSR.save('AfterSR.png')
        imgSR.show()
    def animation(self):
        self.loadImg()
        pygame.init()
        clock = pygame.time.Clock()
        window = pygame.display.set_mode((1000, 500),0,32)
        running = True

        temp = 0

        for y in range (0, self.Height):
            for x in range (0, self.Width):
                for rgb in range (0, 3):
                    self.CPDTable.append(CPD(window, temp+1, self.Array[y,x,rgb]))
                    if rgb == 0:
                        self.CPDTable[temp].SenderColor = (200, 0, 0)
                        self.CPDTable[temp].ReceiverColor = (200, 0, 0)
                    if rgb == 1:
                        self.CPDTable[temp].SenderColor = (0, 200, 0)
                        self.CPDTable[temp].ReceiverColor = (0, 200, 0)
                    if rgb == 2:
                        self.CPDTable[temp].SenderColor = (0, 0, 200)
                        self.CPDTable[temp].ReceiverColor = (0, 0, 200)
                    self.CPDTable[temp].updateColor()
                    temp += 1
        while running:
            self.CorrectTransmitted = 0
            window.fill((255, 255, 255))
            if time.time() - self.Timer >= self.Timeout:
                if self.ActualTransmitting < self.frameCount and self.AmountTransmitting < 8:
                    self.CPDTable[self.ActualTransmitting].transmittingPacket()
                    self.ActualTransmitting += 1
                    self.AmountTransmitting += 1
                    self.Timer = time.time()

            for x in self.CPDTable:
                x.draw()
                x.update()
                if x.Received:
                    if x.ACK:
                        self.CorrectTransmitted += 1
                        self.AmountTransmitting -= 1
            if self.CorrectTransmitted == self.frameCount:
                self.recreateImg()
                running = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    pygame.quit()
                    running = False

            pygame.display.update()
            clock.tick(60)

