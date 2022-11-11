from Classes.Packets.PiranhaMessage import PiranhaMessage
from Classes.Wrappers.AllianceHeaderEntry import AllianceHeaderEntry
from Database.DatabaseHandler import ClubDatabaseHandler, DatabaseHandler
from Classes.ClientsManager import ClientsManager
import json

class AllianceLeagueDataMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0
        
    def encode(self, fields, player):
        playerData = DatabaseHandler().getPlayer(player.ID)
        self.writeByte(0)

        self.writeVInt(False) #State
        self.writeVInt(1)
        self.writeVInt(999999) #Timer
        self.writeVInt(0) #Unk
        self.writeVInt(0) #Event Days' Maps

        self.writeBoolean(True) #League Boolean

        self.writeVLong(0, 1) # LeagueID
        self.writeVInt(playerData['club_rank']) # Rank
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVLong(0, 1) #Club?
        self.writeVInt(0) # Day number
        self.writeVInt(playerData['club_trophies']) #Trophies
        self.writeVInt(1)
        self.writeBoolean(False)
        self.writeVInt(playerData['club_trophies']) # Season score
        self.writeVInt(0) # Season leaderboard place
        self.writeVInt(0) # League State?

        self.writeBoolean(True) #Registration is not closed

        self.writeVLong(0, 1)
        self.writeVInt(playerData['club_tickets']) #Used normal tickets
        self.writeVInt(0) #Max Golden Tickets
        self.writeVInt(playerData['club_tickets']) #Season used normal tickets
        self.writeVInt(0) #Golden tickets
        self.writeVInt(0) # Used golden tickets

        self.writeVInt(1)
        self.writeVInt(0)
        self.writeVInt(999999)
        self.writeVInt(4)
        self.writeVInt(3)

        self.writeVInt(1)
        self.writeVInt(4)
        self.writeDataReference(15, 7)
        self.writeVInt(0)

        self.writeVInt(2)
        self.writeVInt(4)
        self.writeDataReference(15, 25)
        self.writeVInt(1)

        self.writeVInt(3)
        self.writeVInt(4)
        self.writeDataReference(15, 5)
        self.writeVInt(0)

    def decode(self):
        return {}

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 22161

    def getMessageVersion(self):
        return self.messageVersion