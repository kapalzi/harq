import wave
from Pairyty import Pairyty
from BSC import BSC
from TMR import TMR
from SAW import SAW
import numpy as np
import numpy as np
from PIL import Image
import random
from CRC import CRC
import time
import matplotlib.pyplot as plt
from Stats import Stats
from SR import SR
from Gilbert import Gilbert

class Controller(object):
    """docstring for Controller"""

    @staticmethod
    def loadImg():

        # for x in range(1,9):
        #     imgArray = np.zeros([x,x*2,3], dtype=np.uint8)
        #     imgArray.fill(255)
        #     imgFromArray = Image.fromarray(imgArray.astype('uint8')).convert('RGBA')
        #     imgFromArray.save("%d.png"%x)

        img = Image.open("testimg.png")
        img.show()
        array = np.array(img)
        height,width = img.size

        print(height, width)
        for x in range(0,width):
            for y in range(0,height):
                for rgb in range(0,3):
                    Gilbert.LoadGilbert()
                    array[x,y,rgb] = Gilbert.Gilbert(array[x, y, rgb])

        imgBSC = Image.fromarray(array)
        imgBSC.save('BSC.png')
        imgBSC.show()

        array = np.array(img)
        print(height, width)
        for x in range(0, width):
            for y in range(0, height):
                for rgb in range(0, 3):
                    array[x, y, rgb] = BSC.BSC(array[x, y, rgb])

        imgBSC = Image.fromarray(array)
        imgBSC.save('BSC.png')
        imgBSC.show()



        # ramka + saw + bsc + bit parzystosci
        frameSawBscPairytyTimes = []
        frameSizes = []
        acks = []
        nacks = []
        prob = []
        for y in range (0,10):
            for x in range(1,9):
                    img = Image.open("%d.png"%x)
                    # img.show()
                    height, width = img.size
                    frameSizes.append(height*width*3)
                    Stats.StatsRestart()
                    start_time = time.time()
                    array = np.array(img)
                    for x in range(0,width):
                        for y in range(0,height):
                            for rgb in range(0,3):
                                originParity = Pairyty.addPairityBit(array[x,y,rgb])
                                array[x,y,rgb] = SAW.SAW(array[x,y,rgb], originParity)

                    imgSAW = Image.fromarray(array)
                    imgSAW.save('AfterSAW.png')
                    # imgSAW.show()
                    elapsed_time = time.time() - start_time
                    frameSawBscPairytyTimes.append(elapsed_time)
                    acks.append(Stats.ACKCounter)
                    nacks.append(Stats.NACKCounter)
                    prob.append(Stats.NACKCounter/Stats.ACKCounter)

        # plt.plot(frameSizes, prob)
        plt.scatter(frameSizes, prob)
        plt.xlabel("Rozmiar Ramki")
        plt.ylabel("nack/ack")
        plt.title("SAW + BSC + Bit parzystosci")
        plt.grid()
        plt.show()

        plt.scatter(frameSawBscPairytyTimes, frameSizes)
        plt.xlabel("Czas")
        plt.ylabel("Rozmiar Ramki")
        plt.title("SAW + BSC + Bit parzystosci")
        plt.grid()
        plt.show()

        plt.scatter(nacks, frameSizes)
        plt.xlabel("Retransmisje")
        plt.ylabel("Rozmiar Ramki")
        plt.title("SAW + BSC + Bit parzystosci")
        plt.grid()
        plt.show()


        # ramka + saw + bsc + crc
        frameSawBscPairytyTimes = []
        frameSizes = []
        prob = []
        for y in range(0, 10):
            for x in range(1, 9):
                img = Image.open("%d.png" % x)
                # img.show()
                height, width = img.size
                frameSizes.append(height * width * 3)
                Stats.StatsRestart()
                start_time = time.time()

                array = np.array(img)
                for x in range(0, width):
                    for y in range(0, height):
                        for rgb in range(0, 3):
                            originCRC = CRC.CRC(array[x, y, rgb])
                            array[x, y, rgb] = SAW.SAW_CRC(array[x, y, rgb], originCRC)

                imgSAW = Image.fromarray(array)
                imgSAW.save('AfterSAWCRC.png')
                # imgSAW.show()
                elapsed_time = time.time() - start_time
                frameSawBscPairytyTimes.append(elapsed_time)
                prob.append(Stats.NACKCounter/Stats.ACKCounter)

        # plt.plot(frameSizes, prob)
        plt.scatter(frameSizes, prob)
        plt.xlabel("Rozmiar Ramki")
        plt.ylabel("nack/ack")
        plt.title("SAW + BSC + CRC")
        plt.grid()
        plt.show()

        plt.scatter(frameSawBscPairytyTimes, frameSizes)
        plt.xlabel("Czas")
        plt.ylabel("Rozmiar Ramki")
        plt.title("SAW + BSC + CRC")
        plt.grid()
        plt.show()

        plt.scatter(nacks, frameSizes)
        plt.xlabel("Retransmisje")
        plt.ylabel("Rozmiar Ramki")
        plt.title("SAW + BSC + CRC")
        plt.grid()
        plt.show()

        # SR timeout 2 sekundy + BSC + Parzystosc
        SR.timeOut = 2
        frameSawBscPairytyTimes = []
        frameSizes = []
        prob = []
        for y in range(0, 10):
            for x in range(1, 9):
                img = Image.open("%d.png" % x)
                # img.show()
                height, width = img.size
                frameSizes.append(height * width * 3)
                Stats.StatsRestart()
                start_time = time.time()

                array = np.array(img)

                array = SR.SR(array,width,height,1)

                imgSAW = Image.fromarray(array)
                imgSAW.save('AfterSAWCRC.png')
                # imgSAW.show()
                elapsed_time = time.time() - start_time
                frameSawBscPairytyTimes.append(elapsed_time)
                prob.append(Stats.NACKCounter / Stats.ACKCounter)

        # plt.plot(frameSizes, prob)
        plt.scatter(frameSizes, prob)
        plt.xlabel("Rozmiar Ramki")
        plt.ylabel("nack/ack")
        plt.title("SR timeout 2 sekundy + BSC + Bit parzystości")
        plt.grid()
        plt.show()

        plt.scatter(frameSawBscPairytyTimes, frameSizes)
        plt.xlabel("Czas")
        plt.ylabel("Rozmiar Ramki")
        plt.title("SR timeout 2 sekundy + BSC + Bit parzystości")
        plt.grid()
        plt.show()

        plt.scatter(nacks, frameSizes)
        plt.xlabel("Retransmisje")
        plt.ylabel("Rozmiar Ramki")
        plt.title("SR timeout 2 sekundy + BSC + Bit parzystości")
        plt.grid()
        plt.show()

        # SR timeout 4 sekundy + BSC + Parzystosc
        SR.timeOut = 4
        frameSawBscPairytyTimes = []
        frameSizes = []
        prob = []
        for y in range(0, 10):
            for x in range(1, 9):
                img = Image.open("%d.png" % x)
                # img.show()
                height, width = img.size
                frameSizes.append(height * width * 3)
                Stats.StatsRestart()
                start_time = time.time()

                array = np.array(img)

                array = SR.SR(array, width, height, 1)

                imgSAW = Image.fromarray(array)
                imgSAW.save('AfterSAWCRC.png')
                # imgSAW.show()
                elapsed_time = time.time() - start_time
                frameSawBscPairytyTimes.append(elapsed_time)
                prob.append(Stats.NACKCounter / Stats.ACKCounter)

        # plt.plot(frameSizes, prob)
        plt.scatter(frameSizes, prob)
        plt.xlabel("Rozmiar Ramki")
        plt.ylabel("nack/ack")
        plt.title("SR timeout 4 sekundy + BSC + Bit parzystości")
        plt.grid()
        plt.show()

        plt.scatter(frameSawBscPairytyTimes, frameSizes)
        plt.xlabel("Czas")
        plt.ylabel("Rozmiar Ramki")
        plt.title("SR timeout 4 sekundy + BSC + Bit parzystości")
        plt.grid()
        plt.show()

        plt.scatter(nacks, frameSizes)
        plt.xlabel("Retransmisje")
        plt.ylabel("Rozmiar Ramki")
        plt.title("SR timeout 4 sekundy + BSC + Bit parzystości")
        plt.grid()
        plt.show()



        # Gilbert + parzystości timeout 2 sekundy
        SR.timeOut = 2
        frameSawBscPairytyTimes = []
        frameSizes = []
        prob = []
        for y in range(0, 10):
            for x in range(1, 9):
                img = Image.open("%d.png" % x)
                # img.show()
                height, width = img.size
                frameSizes.append(height * width * 3)
                Stats.StatsRestart()
                start_time = time.time()

                array = np.array(img)

                array = SR.SR(array,width,height,2)

                imgSAW = Image.fromarray(array)
                imgSAW.save('AfterSAWCRC.png')
                # imgSAW.show()
                elapsed_time = time.time() - start_time
                frameSawBscPairytyTimes.append(elapsed_time)
                prob.append(Stats.NACKCounter / Stats.ACKCounter)

        # plt.plot(frameSizes, prob)
        plt.scatter(frameSizes, prob)
        plt.xlabel("Rozmiar Ramki")
        plt.ylabel("nack/ack")
        plt.title("SR timeout 2 sekundy + Gilbert + Bit parzystości")
        plt.grid()
        plt.show()

        plt.scatter(frameSawBscPairytyTimes, frameSizes)
        plt.xlabel("Czas")
        plt.ylabel("Rozmiar Ramki")
        plt.title("SR timeout 2 sekundy + Gilbert + Bit parzystości")
        plt.grid()
        plt.show()

        plt.scatter(nacks, frameSizes)
        plt.xlabel("Retransmisje")
        plt.ylabel("Rozmiar Ramki")
        plt.title("SR timeout 2 sekundy + Gilbert + Bit parzystości")
        plt.grid()
        plt.show()

        # Gilbert + parzystości timeout 4 sekundy
        SR.timeOut = 4
        frameSawBscPairytyTimes = []
        frameSizes = []
        prob = []
        for y in range(0, 10):
            for x in range(1, 9):
                img = Image.open("%d.png" % x)
                # img.show()
                height, width = img.size
                frameSizes.append(height * width * 3)
                Stats.StatsRestart()
                start_time = time.time()

                array = np.array(img)

                array = SR.SR(array, width, height, 2)

                imgSAW = Image.fromarray(array)
                imgSAW.save('AfterSAWCRC.png')
                # imgSAW.show()
                elapsed_time = time.time() - start_time
                frameSawBscPairytyTimes.append(elapsed_time)
                prob.append(Stats.NACKCounter / Stats.ACKCounter)

        # plt.plot(frameSizes, prob)
        plt.scatter(frameSizes, prob)
        plt.xlabel("Rozmiar Ramki")
        plt.ylabel("nack/ack")
        plt.title("SR timeout 4 sekundy + Gilbert + Bit parzystości")
        plt.grid()
        plt.show()

        plt.scatter(frameSawBscPairytyTimes, frameSizes)
        plt.xlabel("Czas")
        plt.ylabel("Rozmiar Ramki")
        plt.title("SR timeout 4 sekundy + Gilbert + Bit parzystości")
        plt.grid()
        plt.show()

        plt.scatter(nacks, frameSizes)
        plt.xlabel("Retransmisje")
        plt.ylabel("Rozmiar Ramki")
        plt.title("SR timeout 4 sekundy + Gilbert + Bit parzystości")
        plt.grid()
        plt.show()

        # BSC + CRC timeout 2 sekundy
        SR.timeOut = 2
        frameSawBscPairytyTimes = []
        frameSizes = []
        prob = []
        for y in range(0, 10):
            for x in range(1, 9):
                img = Image.open("%d.png" % x)
                # img.show()
                height, width = img.size
                frameSizes.append(height * width * 3)
                Stats.StatsRestart()
                start_time = time.time()

                array = np.array(img)

                array = SR.SR(array, width, height, 3)

                imgSAW = Image.fromarray(array)
                imgSAW.save('AfterSAWCRC.png')
                # imgSAW.show()
                elapsed_time = time.time() - start_time
                frameSawBscPairytyTimes.append(elapsed_time)
                prob.append(Stats.NACKCounter / Stats.ACKCounter)

        # plt.plot(frameSizes, prob)
        plt.scatter(frameSizes, prob)
        plt.xlabel("Rozmiar Ramki")
        plt.ylabel("nack/ack")
        plt.title("SR timeout 2 sekundy + BSC + CRC")
        plt.grid()
        plt.show()

        plt.scatter(frameSawBscPairytyTimes, frameSizes)
        plt.xlabel("Czas")
        plt.ylabel("Rozmiar Ramki")
        plt.title("SR timeout 2 sekundy + BSC + CRC")
        plt.grid()
        plt.show()

        plt.scatter(nacks, frameSizes)
        plt.xlabel("Retransmisje")
        plt.ylabel("Rozmiar Ramki")
        plt.title("SR timeout 2 sekundy + BSC + CRC")
        plt.grid()
        plt.show()

        # BSC + CRC timeout 4 sekundy
        SR.timeOut = 4
        frameSawBscPairytyTimes = []
        frameSizes = []
        prob = []
        for y in range(0, 10):
            for x in range(1, 9):
                img = Image.open("%d.png" % x)
                # img.show()
                height, width = img.size
                frameSizes.append(height * width * 3)
                Stats.StatsRestart()
                start_time = time.time()

                array = np.array(img)

                array = SR.SR(array, width, height, 3)

                imgSAW = Image.fromarray(array)
                imgSAW.save('AfterSAWCRC.png')
                # imgSAW.show()
                elapsed_time = time.time() - start_time
                frameSawBscPairytyTimes.append(elapsed_time)
                prob.append(Stats.NACKCounter / Stats.ACKCounter)

        # plt.plot(frameSizes, prob)
        plt.scatter(frameSizes, prob)
        plt.xlabel("Rozmiar Ramki")
        plt.ylabel("nack/ack")
        plt.title("SR timeout 4 sekundy + BSC + CRC")
        plt.grid()
        plt.show()

        plt.scatter(frameSawBscPairytyTimes, frameSizes)
        plt.xlabel("Czas")
        plt.ylabel("Rozmiar Ramki")
        plt.title("SR timeout 4 sekundy + BSC + CRC")
        plt.grid()
        plt.show()

        plt.scatter(nacks, frameSizes)
        plt.xlabel("Retransmisje")
        plt.ylabel("Rozmiar Ramki")
        plt.title("SR timeout 4 sekundy + BSC + CRC")
        plt.grid()
        plt.show()

        # Gilbert + parzystości timeout 2 sekundy
        SR.timeOut = 2
        frameSawBscPairytyTimes = []
        frameSizes = []
        prob = []
        for y in range(0, 10):
            for x in range(1, 9):
                img = Image.open("%d.png" % x)
                # img.show()
                height, width = img.size
                frameSizes.append(height * width * 3)
                Stats.StatsRestart()
                start_time = time.time()

                array = np.array(img)

                array = SR.SR(array, width, height, 4)

                imgSAW = Image.fromarray(array)
                imgSAW.save('AfterSAWCRC.png')
                # imgSAW.show()
                elapsed_time = time.time() - start_time
                frameSawBscPairytyTimes.append(elapsed_time)
                prob.append(Stats.NACKCounter / Stats.ACKCounter)

        # plt.plot(frameSizes, prob)
        plt.scatter(frameSizes, prob)
        plt.xlabel("Rozmiar Ramki")
        plt.ylabel("nack/ack")
        plt.title("SR timeout 2 sekundy + Gilbert + CRC")
        plt.grid()
        plt.show()

        plt.scatter(frameSawBscPairytyTimes, frameSizes)
        plt.xlabel("Czas")
        plt.ylabel("Rozmiar Ramki")
        plt.title("SR timeout 2 sekundy + Gilbert + CRC")
        plt.grid()
        plt.show()

        plt.scatter(nacks, frameSizes)
        plt.xlabel("Retransmisje")
        plt.ylabel("Rozmiar Ramki")
        plt.title("SR timeout 2 sekundy + Gilbert + CRC")
        plt.grid()
        plt.show()

        # Gilbert + parzystości timeout 4 sekundy
        SR.timeOut = 4
        frameSawBscPairytyTimes = []
        frameSizes = []
        prob = []
        for y in range(0, 10):
            for x in range(1, 9):
                img = Image.open("%d.png" % x)
                # img.show()
                height, width = img.size
                frameSizes.append(height * width * 3)
                Stats.StatsRestart()
                start_time = time.time()

                array = np.array(img)

                array = SR.SR(array, width, height, 4)

                imgSAW = Image.fromarray(array)
                imgSAW.save('AfterSAWCRC.png')
                # imgSAW.show()
                elapsed_time = time.time() - start_time
                frameSawBscPairytyTimes.append(elapsed_time)
                prob.append(Stats.NACKCounter / Stats.ACKCounter)

        # plt.plot(frameSizes, prob)
        plt.scatter(frameSizes, prob)
        plt.xlabel("Rozmiar Ramki")
        plt.ylabel("nack/ack")
        plt.title("SR timeout 4 sekundy + Gilbert + CRC")
        plt.grid()
        plt.show()

        plt.scatter(frameSawBscPairytyTimes, frameSizes)
        plt.xlabel("Czas")
        plt.ylabel("Rozmiar Ramki")
        plt.title("SR timeout 4 sekundy + Gilbert + CRC")
        plt.grid()
        plt.show()

        plt.scatter(nacks, frameSizes)
        plt.xlabel("Retransmisje")
        plt.ylabel("Rozmiar Ramki")
        plt.title("SR timeout 4 sekundy+ Gilbert + CRC")
        plt.grid()
        plt.show()



