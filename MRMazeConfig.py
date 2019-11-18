#def lists
parseobject = []
command = []
Start = 0

#def Classes
class Room:
    def __init__(self, Pos, OIR):
        self.Pos = Pos
        self.OIR = OIR

class Player:
    def __init__(self, Name, Inventory, Hand, Score, Money, Pos):
        self.Inventory = Inventory
        self.Name = Name
        self.Hand = Hand
        self.Score = Score
        self.Money = Money
        self.Pos = [0,0]
#Player.Pos[0] is x
#Player.Pos[1] is y
#def go(direction):

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
FrontRoom = Room([0,0],bomb)

#def Player
Player = Player(input(''.join(["what is player's name? >>> "])), [], [], 0, 20, [0,0])

#def look up tables and related lists
b = ['take','look']
take = {'bomb': bomb}
look = {'inventory': Player.Inventory}
a = {'take': Player.Inventory.append(bomb), 'look': Lookup(Player.Inventory)}
#def parse

def parse(Input):
    i = 0
    command = Input.lower().split()
    print (command)
    while i < len(command):
        if command[i] in b:
            Start = i
        i = i + 1
    i = Start + 1
    a('take')
#ask to look at Kalebs dictionary python program
