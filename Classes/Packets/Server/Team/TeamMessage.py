from Classes.Packets.PiranhaMessage import PiranhaMessage
from Classes.Messaging import Messaging
import random


class TeamMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):
        self.writeVInt(0) # Room Type
        self.writeBoolean(False)
        self.writeVInt(0)

        self.writeLong(0, 1) # TeamID

        self.writeVInt(0)
        
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        
        self.writeDataReference(15, 7) # Map
        
        self.writeBoolean(False) # BattlePlayerMap
        
        self.writeVInt(1)  # Players Array
        for x in range(1):
         self.writeBoolean(True)  # Owner
         self.writeLong(player.ID[0], player.ID[1]) # Player ID
         self.writeDataReference(16, brawlerID) # Brawler
         self.writeDataReference(29, player.SelectedBrawlersSkins[0]) # Brawler Skin
         self.writeVInt(0) # ?
         self.writeVInt(0) # Brawler Trophies
         self.writeVInt(0) # Brawler Trophies for Rank
         self.writeVInt(1) # Brawler Level
         self.writeVInt(3) # Player State
         self.writeBoolean(False) # Ready
         self.writeVInt(0) # Team
         self.writeVInt(0)
         self.writeVInt(0)
         self.writeVInt(0)
         self.writeVInt(0)
         self.writeVInt(0)
         
         self.writeString(player.Name) # Player Name
         self.writeVInt(100)
         self.writeVInt(28000000 + player.Thumbnail) # Player Thumbnail
         self.writeVInt(43000000 + player.Namecolor) # Player Name Color
         self.writeVInt(-1) # Player Gradient Name Color
         self.writeDataReference(0, 0) # Starpower
         self.writeDataReference(0, 0) # Gadget
         self.writeDataReference(0, 0) # Gear
         self.writeDataReference(0, 0) # Gear
         self.writeVInt(0)
         self.writeVInt(0)
         self.writeVInt(0)
        
        self.writeVInt(0) # Invite Players
        for x in range(0):
         self.writeLong(0, 1) # Unk
         self.writeLong(8, 43928836) # PlayerID
         self.writeString(player.Name) # Name
         self.writeVInt(1) # Invite State
        self.writeVInt(0) # Team Join Request
        for x in range(0):
         self.writeInt(1)
         self.writeInt(1)
        self.writeVInt(0) # Bot Slots Disabled
        for x in range(0):
         self.writeVInt(x+ 1)
        self.writeBoolean(True) #Text Chat Enabled
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeVInt(0) # Modifiers
        for x in range(0):
         self.writeVInt(1) # Modifier ID
        self.writeVInt(0)
        self.writeVInt(0)
        
    def decode(self):
        fields = {}
        fields["TeamID"] = self.readVLong()
        fields["MessageCount"] = self.readVInt()
        super().decode(fields)
        return fields

    def execute(message, calling_instance, fields):
        fields["Socket"] = calling_instance.client
        Messaging.sendMessage(24124, fields, calling_instance.player)

    def getMessageType(self):
        return 24124

    def getMessageVersion(self):
        return self.messageVersion