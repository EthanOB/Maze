#def lists
parseobject = []
command = []
Start = 0
Answer = ''
#def Varaible
objectN = 0
#def Classes
class Room:
    def __init__(self, Name, x, y, OIR,Descript):
        self.x = x
        self.y = y
        self.OIR = OIR
        self.Descript = Descript

class Player:
    def __init__(self, Name, Inventory, Hand, Score, Money, x, y, Room):
        self.Inventory = Inventory
        self.Name = Name
        self.Hand = Hand
        self.Score = Score
        self.Money = Money
        self.x = x
        self.y = y
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
bomb = Object("bomb", boom, False)
pie = Object("pie", boom, False)
#def Rooms Room = Room(Position, objects in room)
FrontRoom = Room("FrontRoom", 0, 0,(bomb),0)
RoomList = [FrontRoom]
#def Player
Player = Player(input("what is player's name? >>> "), [], [pie], 0, 20, [0,0])

#def of RoomControlls
def RoomControlls():
    i = 0
    NullRoom = 0
    NRoomList = []
    while i < len(RoomList):
        if Player.Room in RoomList:
            while Player.Room != Roomlist(i)
                i = i + 1
        else:
            print("No Room! You are moved back to the front room")
            Player.Room = [0,0]
#def parse
def parse():
        Answer = input("What do you want to do >")
        command = Answer.lower().split()
        UsedCommand = ""
        StartS = 0
        CommandFunc = ""
        while i < len(command):
            if command[i] == 'take':
                UsedCommand = append
                StartS = i
            elif command[i] == 'look':
                UsedCommand = print
                StartS = i
            elif command[i] == 'move':
                StartS = i
                if command[StartS+1] == 'west':
                    if


        i = i + 1
