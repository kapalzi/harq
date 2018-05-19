from operator import xor

class CRC:

    def CRC(frame):
        P = 0x04c11db7 #wielomian dla crc-32
        crc32 = 0xffffffff  #wartosc poczatkowa crc32 (2^32)-1

        frame_reversed = frame[::-1] #odwrocenie ramki

        for i in range(0, 24): #rozszerzenie odwroconej ramki
            frame_reversed.append(0)

        for j in range(0,8):
            if frame_reversed[j] != 0:
                frame_reversed[j] =  xor (frame_reversed, P[j])

        frame = frame_reversed[::-1] #ponowne odwrocenie ramki















