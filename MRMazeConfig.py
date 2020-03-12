#def lists
parseobject = []
command = []
Start = 0
Answer = ''
#def Varaible
objectN = 0
#def Classes
class Room:
    def __init__(self,Name,x, y, OIR,Descript,MDirections):
        self.x = x
        self.y = y
        self.OIR = OIR
        self.Descript = Descript
        self.MDirections = MDirections

class Player:
    def __init__(self, Name, Inventory, Hand, Score, Money, x, y, Room, RoomC):
        self.Inventory = Inventory
        self.Name = Name
        self.Hand = Hand
        self.Score = Score
        self.Money = Money
        self.x = x
        self.y = y
        self.RoomC = RoomC
        self.Room = Room

class Object:
    def __init__(self, Name, Func,):
        self.Name = Name
        self.Func = Func
#def functions
def Death(Message):
    print(Message)
    exit()

def boom():
    Death("You were blown up")

def Lookup(RequestedObject):
    print(f"{RequestedObject}")

#def Objects
bomb = Object("bomb", boom)
pie = Object("pie", boom)
#def Rooms Room = Room(Position, objects in room)
FrontRoom = Room("FrontRoom", 0, 0,(bomb),("You are in the frontroom./n You can move west, south, east, and north."),('west','east','north','south'))
RoomListXY = [(0,0)]
RoomList = [FrontRoom]
#def Player
Player = Player(input("what is player's name? >>> "), [], [pie],0,0,0,0,FrontRoom,(0,0))

#def of RoomControlls
def RoomControlls():
    i = 0
    NullRoom = 0
    NRoomList = []
    while i < len(RoomList):
        if Player.Room in RoomList:
            while Player.Room != Roomlist(i):
                i = i + 1
                Player.x = Player.Room(0)
                Player.y = Player.Room(1)
        else:
            print("No Room! You are moved back to the front room")
            Player.Room = (0,0)
#def parse
def parse():
        Answer = input("What do you want to do >")
        command = Answer.lower().split()
        UsedCommand = ""
        i = 0
        StartS = 0
        CommandFunc = ""
        while i < len(command):
            if command[i] == 'take':
                UsedCommand = append
                StartS = i
            elif command[i] == 'look':
                StartS = i
                if command[StartS+1] == 'around':
                    print((Player.Room).Descript)
            elif command[i] == 'move':
                StartS = i
                if command[StartS+1] == 'west':
                    Player.Room = (Player.x-1, Player.y)
                    print('You moved west')
                elif command[StartS+1] == 'east':
                    Player.Room = (Player.x+1, Player.y)
                    print('You moved east')
                elif command[StartS+1] == 'north':
                    Player.Room = (Player.x, Player.y+1)
                    print('You moved north')
                elif command[StartS+1] == 'south':
                    Player.Room = (Player.x, Player.y-1)
                    print('You moved south')
            i = i + 1
