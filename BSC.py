import random

class BSC:
    @staticmethod
    def BSC(frame):
        _BER = 10
        _XOR = 1
        for i in range(0, 8):
            if random.randint(0, 5) < _BER:
                frame = frame ^ _XOR
            _XOR = _XOR * 2
        return frame


