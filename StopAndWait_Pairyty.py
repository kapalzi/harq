from operator import xor

class StopAndWait_Pairyty(object):
    """docstring for StopAndWait"""

    def __init__(self, signal):
        self.signal = bin(signal)

    def pairity(self):
        pairytyBit = int(self.signal[2])
        for x in self.signal[3:]:
            pairytyBit = xor(pairytyBit, int(x))

        self.signal = self.signal + str(pairytyBit)
        return (self.signal)
