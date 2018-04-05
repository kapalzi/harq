import random

def BSC(frame):
    BER = 1
    XOR = 1
    for i in range (0,8):
        if random.randint(0,99) < BER:
            frame = frame ^ XOR
        XOR = XOR*2
    return frame
