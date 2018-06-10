import random

class Stats(object):
    NACKCounter = 0;
    ACKCounter = 0;
    @staticmethod
    def StatsRestart():
        Stats.NACKCounter = 0;
        Stats.ACKCounter = 0;
        return
    @staticmethod
    def CalcProb(array, array2, width, height):
        badPixels = 0
        allPixels = width*height
        different = False
        for x in range(0,width):
            for y in range(0,height):
                for rgb in range(0,3):
                    if array[x, y, rgb] != array2[x, y, rgb]:
                        different = True
                if different == True:
                    badPixels+=1
                    different=False
        return badPixels/allPixels




