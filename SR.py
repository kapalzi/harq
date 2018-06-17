from Pairyty import Pairyty
from BSC import BSC
from TMR import TMR
from CRC import CRC
from Gilbert import Gilbert
from Stats import Stats
import threading
import time

windowsSize = 8
actualTransmitted = 0
array = 0

timeOut = 2 #sekundy


def BSCParity(frame, originParity):
    while True:
            frame_out = TMR.TMR(BSC.BSC(frame), BSC.BSC(frame), BSC.BSC(frame))  # bedzie zgodny z bitem parzystosci wyliczonym            #
            frameParity = Pairyty.addPairityBit(frame_out)
            if Pairyty.getParityBit(originParity) == Pairyty.getParityBit(frameParity):  # z nadawanej ramki.                                      #
                Stats.ACKCounter += 1
                globals()["actualTransmitted"] = globals()["actualTransmitted"] - 1
                return frame_out # Korzysta z protokolow TMR i BSC                         #
            Stats.NACKCounter += 1

def GilbertParity(frame, originParity):
    while True:
            Gilbert.LoadGilbert()
            frame_out = TMR.TMR(Gilbert.Gilbert(frame), Gilbert.Gilbert(frame),
                                Gilbert.Gilbert(frame))  # bedzie zgodny z bitem parzystosci wyliczonym            #
            frameParity = Pairyty.addPairityBit(frame_out)
            if Pairyty.getParityBit(originParity) == Pairyty.getParityBit(frameParity):  # z nadawanej ramki.                                      #
                Stats.ACKCounter += 1
                globals()["actualTransmitted"] = globals()["actualTransmitted"] - 1
                return frame_out # Korzysta z protokolow TMR i BSC                         #

def BSCCRC(frame, originCRC):
    while True:
            frame_out = TMR.TMR(BSC.BSC(frame), BSC.BSC(frame), BSC.BSC(frame))
            frameCRC = CRC.CRC(frame_out)
            if frameCRC == originCRC:
                Stats.ACKCounter += 1
                globals()["actualTransmitted"] = globals()["actualTransmitted"] - 1
                return frame_out
            Stats.NACKCounter += 1


def GilbertCRC(frame, originCRC):
    while True:
            Gilbert.LoadGilbert()
            frame_out = TMR.TMR(Gilbert.Gilbert(frame), Gilbert.Gilbert(frame), Gilbert.Gilbert(frame))
            frameCRC = CRC.CRC(frame_out)
            if frameCRC == originCRC:
                Stats.ACKCounter += 1
                globals()["actualTransmitted"] = globals()["actualTransmitted"] - 1
                return frame_out
            Stats.NACKCounter += 1

class Watek(threading.Thread):
    def __init__(self, option, frame, originParity=0, originCRC=0):
        self.option = option
        self.frame = frame
        self.originParity = originParity
        self.originCRC = originCRC
        threading.Thread.__init__(self)

    def run(self):
        if self.option == 1:
            globals()["array"] = BSCParity(self.frame, self.originParity) - 50
        if self.option == 2:
            globals()["array"] = GilbertParity(self.frame, self.originParity) - 50
        if self.option == 3:
            globals()["array"] = BSCCRC(self.frame, self.originCRC) - 50
        if self.option == 4:
            globals()["array"] = GilbertCRC(self.frame, self.originCRC) - 50


class SR:
    @staticmethod
    def SR(array, width, height, option):  # option1: BSC+Parity, option2: Gilbert+Parity, option3: BSC+CRC32, option4: Gilbert+CRC32
        clock = time.time()
        if timeOut <= 0:
            while True:  # Powtarza wysylanie az bit parzystosci wyslanej ramki    #
                for x in range(0, width):
                    for y in range(0, height):
                        for rgb in range(0, 3):
                            if globals()["actualTransmitted"] < globals()["windowsSize"]:
                                if option == 1:
                                    originParity = Pairyty.addPairityBit(array[x, y, rgb])
                                    globals()["actualTransmitted"] += 1
                                    Watek(option, array[x, y, rgb], originParity).run()
                                    array[x, y, rgb] = globals()["array"]
                                if option == 2:
                                    originParity = Pairyty.addPairityBit(array[x, y, rgb])
                                    Watek(option, array[x, y, rgb], originParity).run()
                                    globals()["actualTransmitted"] += 1
                                    array[x, y, rgb] = globals()["array"]
                                if option == 3:
                                    originCRC = CRC.CRC(array[x, y, rgb])
                                    Watek(option, array[x, y, rgb], 0, originCRC).run()
                                    globals()["actualTransmitted"] += 1
                                    array[x, y, rgb] = globals()["array"]
                                if option == 4:
                                    originCRC = CRC.CRC(array[x, y, rgb])
                                    Watek(option, array[x, y, rgb], 0, originCRC).run()
                                    globals()["actualTransmitted"] += 1
                                    array[x, y, rgb] = globals()["array"]
                            if Stats.ACKCounter / 3 == (width * height):
                                return array
        else:
            while time.time() - clock < timeOut:
                for x in range(0, width):
                    for y in range(0, height):
                        for rgb in range(0, 3):
                            if time.time() - clock > timeOut:
                                return array

                            if globals()["actualTransmitted"] < globals()["windowsSize"]:
                                if option == 1:
                                    originParity = Pairyty.addPairityBit(array[x, y, rgb])
                                    globals()["actualTransmitted"] += 1
                                    Watek(option, array[x, y, rgb], originParity).run()
                                    array[x, y, rgb] = globals()["array"]
                                if option == 2:
                                    originParity = Pairyty.addPairityBit(array[x, y, rgb])
                                    Watek(option, array[x, y, rgb], originParity).run()
                                    globals()["actualTransmitted"] += 1
                                    array[x, y, rgb] = globals()["array"]
                                if option == 3:
                                    originCRC = CRC.CRC(array[x, y, rgb])
                                    Watek(option, array[x, y, rgb], 0, originCRC).run()
                                    globals()["actualTransmitted"] += 1
                                    array[x, y, rgb] = globals()["array"]
                                if option == 4:
                                    originCRC = CRC.CRC(array[x, y, rgb])
                                    Watek(option, array[x, y, rgb], 0, originCRC).run()
                                    globals()["actualTransmitted"] += 1
                                    array[x, y, rgb] = globals()["array"]
                            if Stats.ACKCounter / 3 == (width * height):
                                return array
        return array
