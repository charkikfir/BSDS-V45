from Classes.ByteStream import ByteStream
from Classes.ClientsManager import ClientsManager
from Classes.Packets.PiranhaMessage import PiranhaMessage
from Database.DatabaseHandler import DatabaseHandler


class BattleLogMessage(PiranhaMessage):

    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0
        

    def encode(self, fields, player):
        self.writeBoolean(True)        
        self.writeVInt(0) # Count

    def decode(self):
        pass
       

    def getMessageType(self):
        return 23458

    def getMessageVersion(self):
        return self.messageVersion