from Pairyty import Pairyty
from BSC import BSC
from TMR import TMR
from CRC import CRC

class SAW:
    @staticmethod
    def SAW(frame, originParity):
        while True:                                                 #   Powtarza wysylanie az bit parzystosci wyslanej ramki    #
            frame_out = TMR.TMR(BSC.BSC(frame),BSC.BSC(frame),BSC.BSC(frame))       #   bedzie zgodny z bitem parzystosci wyliczonym            #
            frameParity = Pairyty.addPairityBit(frame_out)
            if Pairyty.getParityBit(originParity) == Pairyty.getParityBit(frameParity):              #   z nadawanej ramki.                                      #
                break                                               #   Korzysta z protokolow TMR i BSC                         #
        return frame_out

    @staticmethod
    def SAW_CRC(frame, originCRC):
        while True:
            frame_out = TMR.TMR(BSC.BSC(frame), BSC.BSC(frame), BSC.BSC(frame))
            frameCRC = CRC.CRC(frame_out)
            if frameCRC == originCRC:
                break
        return frame_out