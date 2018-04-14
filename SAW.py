from Pairyty import Pairyty
from BSC import BSC
from TMR import TMR


class SAW:
    @staticmethod
    def SAW(frame, origin_parity):
        while True:                                                 #   Powtarza wysylanie az bit parzystosci wyslanej ramki    #
            frame_out = TMR.TMR(BSC.BSC(frame),BSC.BSC(frame),BSC.BSC(frame))       #   bedzie zgodny z bitem parzystosci wyliczonym            #
            if origin_parity == Pairyty.addPairityBit(frame_out):              #   z nadawanej ramki.                                      #
                break                                               #   Korzysta z protokolow TMR i BSC                         #
        return frame_out