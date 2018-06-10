import random

class Gilbert(object):
    isValid = True; #Status stanu
    BER1 = 100-7  # Procentowe prawdopodobienstwo wyjscia ze stanu dobrego (Pdz)
    BER2 = 100-12  # Procentowe prawdopodobienstwo wyjscia ze stanu zlego (Pzd)
    pd = 1 #Procentowe prawdopodobienstwa bledu w dobrym
    pz = 99 #Procentowe prawdopodobienstwa bledu w zlym
    PD = BER1/(BER1+BER2) #Prawdopodobienstwa graniczne pozostania w dobrym
    PZ = BER2/(BER1+BER2) #Prawdopodobienstwa graniczne pozostania w zlym
    Pe = (PD * pd + PZ * pz)/100; #Elementowa stopa bledow
    @staticmethod
    def Gilbert(frame):
        XOR = 1
        for i in range(0, 8):
            if not Gilbert.isValid:
                if random.randint(0, 99) < Gilbert.pz:
                    frame = frame ^ XOR
                    XOR = XOR * 2
                else:
                    XOR = XOR * 2
            else:
                if random.randint(0, 99) < Gilbert.pd:
                    frame = frame ^ XOR
                    XOR = XOR * 2
                else:
                    XOR = XOR * 2
            #print("Elementowa stopa bledu: ")
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
