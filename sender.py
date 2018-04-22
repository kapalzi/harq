import threading
import receiver

timeout = 4000 #4000ms = 4s
message = 0
class Sender(object): #jeżeli timeouted to NACK
    def __init__(self):

    def Message(self):
        return message

    def getMessage(self, receiver): #odbieranie ACK
        if(receiver.ACK == -1) #powtórzenie wysyłania w przypadku niepowodzenia (NACK)
            self.sendPacket(self, receiver)
        else
            return
    def sendPacket(self, receiver): #wysylanie pakietu
    def Start(self):
        while (True)
            self.getMessage(receiver)
