import sender
import random

message = 0
ACK = -1
class Receiver(object):
    def __init__(self):

    def getMessage(self, sender): #odbieranie pakietu
            message = sender.Message()

    def sendACK(self, sender): #wysylanie ACK

    def sendMessage(self, sender): #jeżeli
        ER = 5 #error rate - możliwość utraty pakietu
        if random.randint(0, 99) < ER:
            return
        else:
            self.sendACK(sender)
    def Start(self, sender): #pętla nieskończona w oczekiwaniu na pakiet
        while(True)
            self.getMessage(sender)