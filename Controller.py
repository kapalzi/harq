import wave
from Pairyty import Pairyty
from BSC import BSC
from TMR import TMR
from SAW import SAW
import numpy as np
import numpy as np
from PIL import Image
import random
import matplotlib.pyplot as plt


class Controller(object):
    """docstring for Controller"""

    # def __init__(self, arg):
    #     super(Controller, self).__init__()
    #     self.arg = arg

    # def loadWave(self):
    #     file = wave.open("sample.wav")
    #     binary_data = file.readframes(file.getnframes())
    #     file.close()
    #     # print(len(binary_datanary_data))
    #     return  binary_data
    #
    # newFrame = []
    # # for x in  loadWave(1):
    # #     Pairyty.addPairityBit(x)
    # #     origin_parity = Pairyty.addPairityBit(x)
    # #     x = SAW.SAW(x, origin_parity)
    # #     newFrame.append(x)
    #
    # # data = loadWave()
    # file = 'sample.wav'
    #
    # with wave.open(file, 'r') as wav_file:
    #     # Extract Raw Audio from Wav File
    #     signal = wav_file.readframes(-1)
    #     signal = np.fromstring(signal, 'Int16')
    # fs = wav_file.getframerate()
    #
    # channels = [[] for channel in range(signal.getnchannels())]
    # Time=np.linspace(0, len(signal)/len(channels)/fs, len(signal)/len(channels))
    #
    #     #Plot
    #
    # plt.figure(1)
    # plt.title('Signal Wave...')
    # for channel in channels:
    #     plt.plot(Time,channel)
    # plt.show()
    # print(12)
    @staticmethod
    def loadImg():
        img = Image.open("testimg.png")
        img.show()
        array = np.array(img)
        height,width = img.size

        for x in range(0,width):
            for y in range(0,height):
                for rgb in range(0,3):
                    origin_parity = Pairyty.addPairityBit(array[x,y,rgb])
                    array[x,y,rgb] = SAW.SAW(array[x,y,rgb],origin_parity)

        img = Image.fromarray(array)
        img.save('new.png')
        img.show()

