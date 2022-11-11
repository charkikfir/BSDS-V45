from Classes.ByteStream import ByteStream
from Classes.ClientsManager import ClientsManager
from Classes.Packets.PiranhaMessage import PiranhaMessage
from Database.DatabaseHandler import DatabaseHandler


class SeasonRewards(PiranhaMessage):

    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0
        

    def encode(self, fields, player):
        self.writeVInt(4)#4 - championship, 5 - psg, 1 - table?? (??)
        self.writeVInt(9)#count reward
        for x in range(9):
         #reward entry
            self.writeVInt(x+1)#idx
            self.writeVInt(1)#?
            self.writeVInt(x)#win
            self.writeBoolean(True)#gemoffer
            self.writeVInt(6)#id
            self.writeVInt(1)#count
            self.writeVInt(16)#dref
            self.writeVInt(0)
            self.writeVInt(0)#skin
            self.writeBoolean(False)#??
            #reward entry end
            self.writeBoolean(False)#??
    	

    def decode(self):
        return {}

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 24123

    def getMessageVersion(self):
        return self.messageVersion
