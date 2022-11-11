from Classes.Packets.PiranhaMessage import PiranhaMessage
from Classes.Messaging import Messaging


class TeamStream(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):
        self.writeVLong(0,1) # TeamID
        self.writeVInt(1) # Messages Count

        for x in range(1):
          self.writeLong(0,1)
          self.writeLong(player.ID[0] , player.ID[1])
          self.writeString(player.Name)
          self.writeVInt(0)#PlayerRole
          self.writeVInt(0)
          self.writeBoolean(False)
        

    def decode(self):
        fields = {}
        super().decode(fields)
        return fields

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 24131

    def getMessageVersion(self):
        return self.messageVersion