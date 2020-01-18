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
    def __init__(self, Name, Func, Uses):
        self.Name = Name
        self.Func = Func
        self.Uses = Uses
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
FrontRoom = Room("FrontRoom", 0, 0,(bomb),(bomb.Name))
RoomList = [FrontRoom]
#def Player
Player = Player(input("what is player's name? >>> "), [], [pie], 0, 20, 0, 0, FrontRoom)

#def of RoomControlls
def RoomControlls():
    i = 0
    NullRoom = 0
    NRoomList = []
    while i < len(RoomList):
        if Player.x == RoomList[i].x:
            NRoomList.append(RoomList[i])
        else:
            NullRoom = NullRoom + 1
        i = i + 1
        if (NullRoom == len(RoomList)):
            print('You can not move to this room') #make program to find the nearest room
            break
    i = 0
    while (i < len(NRoomList)):
        if Player.y == NRoomList[i].y:
            Player.Room = NRoomList[i]
        i = i + 1
    i = 0
#def parse
def parse():
        Answer = input("What do you want to do >")
        command = Answer.lower().split()
        CommandFunc = ""
        while i < len(command):
            if command[i] = 'take'
                
            elif command[i] = 'look'

            elif command[i] = 'move'

        i = i + 1


        UsedCommand(objectN)
