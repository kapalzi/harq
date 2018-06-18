from sender import Sender
from receiver import Receiver
from Packet import Packet
import time
import pygame
from CRC import CRC
from BSC import BSC
from TMR import TMR
from Stats import Stats
from Pairyty import Pairyty

class CPD:
    def __init__(self, _surface, x, frame):
        self.PacketColor = (128, 128, 128)
        self.SenderColor = (0, 0, 255)
        self.ReceiverColor = (0, 0, 255)
        self.Surface = _surface
        self.X = x
        self.Frame = frame
        self.CCRC = CRC.CRC(self.Frame) #Correct CRC
        self.SCRC = CRC.CRC(TMR.TMR(BSC.BSC(self.Frame), BSC.BSC(self.Frame), BSC.BSC(self.Frame))) #SendCRC
        self.Sender = Sender(self.Surface, self.SenderColor, self.X)
        self.Receiver = Receiver(self.Surface, self.ReceiverColor, self.X, self.SCRC)
        self.Packet = []
        self.Timeout = 60 #30sec timeout
        self.Timer = time.time()
        self.Received = False
        self.Transmitting = False
        self.Retransmitting = False
        self.ACK = False
        self.Checked = False;
    def draw(self):
        for x in self.Packet:
            x.draw()
        self.Sender.draw()
        self.Receiver.draw()
    def update(self):
        for x in self.Packet:
            x.update()
            if x.rect.contains(self.Receiver.rect):
                if self.CCRC == self.Receiver.crc:
                    x.color = (0, 255, 0)
                else:
                    x.color = (255, 0, 0)
                x.direction = -5

            if x.rect.contains(self.Sender.rect):
                x.direction = 0
                self.Received = True
                if x.color == (255, 0, 0):
                    self.Retransmitting = True
                    self.Received = False
                    self.SCRC = CRC.CRC(TMR.TMR(BSC.BSC(self.Frame), BSC.BSC(self.Frame), BSC.BSC(self.Frame)))
                    self.Receiver.crc = self.SCRC
                    x.color = (128,128,128)
                if x.color == (0, 255, 0):
                    self.ACK = True
                    self.Received = True
                    self.Transmitting = False
                    del x


        if self.Retransmitting or (time.time() - self.Timer >= self.Timeout and self.Transmitting == True):
            self.transmittingPacket()
            Stats.NACKCounter+=1
            Stats.TransmittingCounter += 1
            self.Retransmitting = False
    def updateColor(self):
        self.Sender.color = self.SenderColor
        self.Receiver.color = self.ReceiverColor
    def transmittingPacket(self):
        self.Transmitting = True
        if not self.Received and self.Transmitting:
            self.Packet.append(Packet(self.Surface, self.PacketColor, self.X))
            self.Timer = time.time()

