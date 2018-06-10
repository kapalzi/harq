import random

class Gilbert(object):
    @staticmethod
    def Gilbert(frame):
        BER1 = 5 #Procentowe prawdopodobienstwo pozostania w stanie dobrym (Wyjscie ze stanu 1-BER1)
        BER2 = 2 #Procentowe prawdopodobienstwo pozostania w stanie zlym (Wyjscie ze stanu 1-BER2)
        isValid = True #Status stanu
        XOR = 1
        for i in range(0, 8):
            if isValid:
                if random.randint(0,99) < BER1:
                    XOR = XOR * 2
                    isValid = True
                else:
                    isValid = False
            elif not isValid:
                if random.randInt(0,99) < BER2:
                    frame = frame ^ _XOR
                    _XOR = _XOR * 2
                    isValid = False
                else:
                    isValid = True
        return frame