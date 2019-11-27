#def lists
parseobject = []
command = []
Start = 0
Answer = ''

#def Classes
class Room:
    def __init__(self, Name, x, y, OIR):
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
pie = Object("pie", boom, False)
#def Rooms
#Room = Room(Position, objects in room)
FrontRoom = Room("FrontRoom", 0, 0,bomb)
RoomList = [FrontRoom]
#def Player
Player = Player(input(''.join(["what is player's name? >>> "])), [], [pie], 0, 20, 0, 0, FrontRoom)

#def look up tables and related lists
UsableCommands = ['take','look']
look = {'inventory': Player.Inventory}
CommandObjects = {'take': [Player.Room.OIR], 'look': [Player.Room.OIR, Player.Inventory]}
CommandList = {'take': Player.Inventory.append, 'look': print}

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
            print('You can not move to this room') #make program to fin the nearest room
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
        i = 0
        UsedCommand = CommandList[command[i]]
        NullCommand = 0
        objectN = 0
        Start = 0
        CommandObjectsVar1 = 0
        CommandObjectsVar2 = 0
        while i < len(command):
            if command[i] in UsableCommands:
                UsedCommand = CommandList[command[i]]
                Start = i
                break
        i = Start + 1
        while i < len(command):
            if command[i] == CommandObjects[command[Start]]:
                objectN = CommandObjects[UsedCommand]
                break
            elif CommandObjectsVar2 < len(CommandObjects[command[Start]]):
                CommandObjectsVar2 = CommandObjectsVar2 + 1
            elif CommandObjectsVar1 < len(CommandObjects[command[Start]]):
                CommandObjectsVar1 = CommandObjectsVar1 + 1
                CommandObjectsVar2 = 0
            i = i + 1
        UsedCommand(objectN)
