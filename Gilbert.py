import random

class Gilbert(object):
    isValid = True; #Status stanu
    BER1 = 100-1  # Procentowe prawdopodobienstwo wyjscia ze stanu dobrego
    BER2 = 100-99  # Procentowe prawdopodobienstwo wyjscia ze stanu zlego

    @staticmethod
    def Gilbert(frame):
        XOR = 1
        for i in range(0, 8):
            if not Gilbert.isValid:
                frame = frame ^ XOR
                XOR = XOR * 2
        return frame
    @staticmethod
    def LoadGilbert():
        if Gilbert.isValid:
            if random.randint(0, 99) < Gilbert.BER1:
                Gilbert.isValid = True
            else:
                Gilbert.isValid = False
        elif not Gilbert.isValid:
            if random.randint(0, 99) < Gilbert.BER2:
                Gilbert.isValid = False
            else:
                Gilbert.isValid = True
