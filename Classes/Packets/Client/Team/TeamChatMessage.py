from Classes.Packets.PiranhaMessage import PiranhaMessage
from Classes.Messaging import Messaging
from Classes.Packets.Server.Team.TeamStream import TeamStream

class TeamChatMessage(PiranhaMessage):
    #14369
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0
        
    def decode(self):
        fields = {}      
        fields["Message"] = self.readString()
        super().decode(fields)
        return fields
        
    def process(self):
        self.player.ctick += 1  

    def encode(self, player, fields):
        #StreamEntry Start
        self.writeLong(0,1)#StreamEntryID
        self.writeLong(player.ID[0] , player.ID[1])
        self.writeString(player.Name)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)
        #StreamEntry End
        
        self.writeString(fields["Message"])
        self.writeVInt(0)#Винт появился с 43 версии  
        

    def execute(message, calling_instance, fields):
        fields["Socket"] = calling_instance.client
        Messaging.sendMessage(14359, fields, calling_instance.player)

    def getMessageType(self):
        return 14359

    def getMessageVersion(self):
        return self.messageVersion