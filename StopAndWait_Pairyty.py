from operator import xor

class StopAndWait_Pairyty(object):
	"""docstring for StopAndWait"""
	def __init__(self, signal):

		self.signal = bin(signal)
		print(type(self.signal))
		print(self.signal)

	def parity(self):
		return(self.signal[-1])

