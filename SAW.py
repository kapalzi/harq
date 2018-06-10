from Pairyty import Pairyty
from BSC import BSC
from TMR import TMR
from CRC import CRC
from Gilbert import Gilbert
from Stats import Stats

class SAW:
    @staticmethod
    def SAW(frame, originParity):
        while True:                                                 #   Powtarza wysylanie az bit parzystosci wyslanej ramki    #
            frame_out = TMR.TMR(BSC.BSC(frame),BSC.BSC(frame),BSC.BSC(frame))       #   bedzie zgodny z bitem parzystosci wyliczonym            #
            frameParity = Pairyty.addPairityBit(frame_out)
            if Pairyty.getParityBit(originParity) == Pairyty.getParityBit(frameParity):              #   z nadawanej ramki.                                      #
                Stats.ACKCounter += 1
                break                                               #   Korzysta z protokolow TMR i BSC                         #
            Stats.NACKCounter += 1
        return frame_out

    @staticmethod
    def SAW_CRC(frame, originCRC):
        while True:
            frame_out = TMR.TMR(BSC.BSC(frame), BSC.BSC(frame), BSC.BSC(frame))
            frameCRC = CRC.CRC(frame_out)
            if frameCRC == originCRC:
                Stats.ACKCounter += 1
                break
            Stats.NACKCounter += 1
        return frame_out

    @staticmethod
    def SAWGilbert(frame, originParity):
        while True:  # Powtarza wysylanie az bit parzystosci wyslanej ramki    #
            frame_out = TMR.TMR(Gilbert.Gilbert(frame), Gilbert.Gilbert(frame),Gilbert.Gilbert(frame))  # bedzie zgodny z bitem parzystosci wyliczonym            #
            frameParity = Pairyty.addPairityBit(frame_out)
            if Pairyty.getParityBit(originParity) == Pairyty.getParityBit(
                    frameParity):  # z nadawanej ramki.                                      #
                Stats.ACKCounter += 1
                break  # Korzysta z protokolow TMR i BSC                         #
            Stats.NACKCounter += 1
        return frame_out

    @staticmethod
    def SAW_GilbertCRC(frame, originCRC):
        while True:
            frame_out = TMR.TMR(Gilbert.Gilbert(frame), Gilbert.Gilbert(frame), Gilbert.Gilbert(frame))
            frameCRC = CRC.CRC(frame_out)
            if frameCRC == originCRC:
                Stats.ACKCounter += 1
                break
            Stats.NACKCounter += 1
        return frame_out