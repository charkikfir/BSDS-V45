from Database.DatabaseHandler import DatabaseHandler
from Classes.Packets.Server.Team.TeamMessage import TeamMessage
from Classes.Packets.PiranhaMessage import PiranhaMessage
from Classes.Messaging import Messaging
from Classes.Packets.Server.Team.TeamStream import TeamStream


class TeamPremadeChatMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, player, fields):
        self.writeLong(0,1) # StreamEntryID
        self.writeLong(player.ID[0] , player.ID[1]) # TargetID (НЕОБХОДИМ РЕАЛЬНЫЙ ID ИГРОКА)
        self.writeString(player.Name)#Nickame 
        self.writeVInt(1)
        self.writeVInt(0)
        self.writeBoolean(False)
        self.writeDataReference(40, 1)
        self.writeBoolean(False)
        self.writeString()#Unk String(maybe uselles string?)
        self.writeVInt(0)      
        self.writeVInt(1)

    def decode(self):
        return {}

    def execute(message, calling_instance, fields):
        fields["Socket"] = calling_instance.client
        Messaging.sendMessage(24131, fields, calling_instance.player)
                                                                                            
    def getMessageType(self):
        return 14369

    def getMessageVersion(self):
        return self.messageVersion