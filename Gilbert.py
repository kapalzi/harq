import random

class Gilbert(object):
    @staticmethod
    def Gilbert(frame):
        pdz = random.uniform(0, 1)
        pzd = random.uniform(0, 1)

        pD = pdz/(pdz+pzd)
        pZ = pzd/(pzd+pdz)

        if pD>pZ: d = True
        else: d = False

        return d


#a