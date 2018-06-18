import random

class BSC(object):
    @staticmethod
    def BSC(frame):
        _BER = 0.0294
        _XOR = 1
        for i in range(0, 8):
            if random.randint(0, 99) < _BER*100:
                frame = frame ^ _XOR
            _XOR = _XOR * 2
        return frame


