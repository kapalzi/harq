from operator import xor

class CRC:

    def CRC(frame):
        crc = 0
        crc = 0xffffffff & ~crc

        frame = str(frame)
        for char in frame:
            byte = ord(char)
            crc = crc ^ byte
            for j in range (8):
                crc = (crc >> 1) ^ (0x04c11db7 & -(crc & 1))
        return 0xffffffff & ~crc















