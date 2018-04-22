from operator import xor


class Pairyty(object):
    @staticmethod
    def addPairityBit(frame):
        frame=bin(frame)
        pairytyBit = int(frame[2])
        for x in frame[3:]:
            pairytyBit = xor(pairytyBit, int(x))

        frame = frame + str(pairytyBit)
        return (frame)
    def getParityBit(self):
        print(self)
        return self[-1]

# class Pairyty(object):
#     @staticmethod
#     def addPairityBit(frame):
#         print(frame)
#         pairytyBit = frame[0]
#         for x in frame[1:]:
#             pairytyBit = xor(pairytyBit, int(x))
#
#         frame = frame + str(pairytyBit)
#         return (frame)
