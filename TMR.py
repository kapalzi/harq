class TMR:

    @staticmethod
    def TMR(frame, frame2, frame3):                                  # frame - x, frame2 - y, frame3 - z
        TMRFrame = (frame & frame2) | (frame2 & frame3) | (frame | frame3) # Majority Logic Gate, porównanie przez głosowanie
        return TMRFrame                                                    # xy v yz v xz
