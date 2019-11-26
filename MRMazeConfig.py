#def lists
parseobject = []
command = []
Start = 0

#def Classes
class Room:
    def __init__(self, x, y, OIR):
        self.x = x
        self.y = y
        self.OIR = OIR

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

#def Rooms
#Room = Room(Position, objects in room)
FrontRoom = Room( 0, 0,[bomb])
RoomList = [FrontRoom]
#def Player
Player = Player(input(''.join(["what is player's name? >>> "])), [], [], 0, 20, 0, 0, FrontRoom)

#def look up tables and related lists
UsableCommands = ['take','look']
look = {'inventory': Player.Inventory}
CommandList = {'take': print('It works!'), 'look': Lookup(Player.Inventory)}

#def of Room controls
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
            print('You can not move to this room') #make program to fin the nearest room
            break
    i = 0
    while (i < len(NRoomList)):
        if Player.y == NRoomList[i].y:
            Player.Room = NRoomList[i]
        i = i + 1
    i = 0
#def parse
def parse(Input):
    i = 0
    command = Input.lower().split()
    while i < len(command):
        if command[i] in UsableCommands:
            Start = i
        i = i + 1
    i = Start + 1
    while i < len(command):
        if command[i] in Player.Room.OIR:
            objectN = 0
            i = 0
            while i < Player.Room.OIR:
                if objectN is Player.Room.OIR[i]:
                    objectN = Player.Room.OIR[i]
                    i = i + 1
        i = i + 1
    CommandList(command(Start))
