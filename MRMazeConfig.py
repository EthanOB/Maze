#def lists
parseobject = []
command = []
#def Classes
class Room:
    def __init__(self,Name,C, OIR, OIRN, Descript, Lock):
        self.C = C
        self.OIR = OIR
        self.OIRN = OIRN
        self.Descript = Descript
        self.Lock = Lock

class Player:
    def __init__(self, Name, Inventory, InventoryN, Score, Money, Room, RoomC):
        self.Inventory = Inventory
        self.InventoryN = InventoryN
        self.Name = Name
        self.Score = Score
        self.Money = Money
        self.RoomC = RoomC
        self.Room = Room

class Object:
    def __init__(self, Name, Func,):
        self.Name = Name
        self.Func = Func
#def functions
def boom():
    print("Your Score was"+Player.Score)
    exit("You were blown up")

def SplatInTheFace():
    print("You slamed the pie into your own face")
    Player.Score = Player.Score+20

def eat():
    print("You ate the beans and it was tasty")
    Player.Score = Player.Score+20

def burn():
    print("You burned yourself on the lamp")
    Player.Score = Player.Score-5

def smell():
    print("You smelled the flowers")
    Player.Score = Player.Score + 10

def unlock():
    if Player.RoomC == [0,1]:
        Exit.Lock = True
        print("You unlocked the door")
#def Objects
bomb = Object("bomb", boom)
pie = Object("pie", SplatInTheFace)
beans = Object("can of beans", eat)
lamp = Object("lamp", burn)
flowers = Object("flowers", smell)
key = Object("key", unlock)
nothing = Object("nothing", boom)
#def Rooms Room = Room(Position, objects in room)
WestRoom = Room("WestRoom",[-1,0], pie, 'pie', ("You are in the westroom and it is very dark. \nYou can move east."), True)
FrontRoom = Room("FrontRoom",[0,0], bomb, 'bomb', ("You are in the frontroom.\nYou can move west, south, east, and north."), True)
EastRoom = Room("EastRoom",[1,0], beans, 'beans', ("You are in the eastroom.\nYou can move west"), True)
DiningRoom = Room("DiningRoom",[0,-1], lamp, 'lamp', ("You are in the diningroom.\nYou can move south and north"), True)
Garden = Room("Garden", [0,-2], flowers, 'flowers', ("You are in the garden.\nYou can move north."), True)
Entryway = Room("Entryway", [0,1], key, 'key', ("You are in the garden.\nYou can move north (if door is unlocked) and south"), True)
Exit = Room("Exit", [0,2], nothing, 'nothing', ("You won the game"), False)
RoomCList =[[-1,0], [0,0], [1,0], [0,-1], [0,-2], [0,1]]
RoomList = [WestRoom, FrontRoom, EastRoom, DiningRoom, Garden, Entryway]
#def Player
Player = Player(input("what is player's name? >>> "), [], [],0,0,FrontRoom,[0,0])
#def parse
def parse():
        command = input("What do you want to do >").lower().split()
        i = 0
        if 'quit' in command:
            exit('You requested to end the game')
        if 'use' in command:
            while i < len(command):
                if command[i] in Player.InventoryN:
                    (Player.Inventory[Player.InventoryN.index(command[i])]).Func()
                    break
                i = i+1
        if 'take' in command:
            if (Player.Room).OIRN in command:
                Player.Inventory.append((Player.Room).OIR)
                Player.InventoryN.append((Player.Room).OIRN)
                (Player.Room).OIR = ""
                (Player.Room).OIRN = ""
            else:
                print("that doesn't exist")
        elif 'look' in command or 'view' in command:
            if 'around' in command:
                print((Player.Room).Descript+"In the room, there is a "+(Player.Room).OIRN)
            elif 'inventory' in command:
                print(Player.InventoryN)
        elif 'move' in command or 'go' in command:
            if 'west' in command:
                if [Player.RoomC[0]-1, Player.RoomC[1]] in RoomCList:
                    Player.RoomC = [Player.RoomC[0]-1, Player.RoomC[1]]
                    Player.Room = RoomList[RoomCList.index(Player.RoomC)]
                    print('You moved west')
                else:
                    print("That room doesn't exist")
            elif 'east' in command:
                if [Player.RoomC[0]+1, Player.RoomC[1]] in RoomCList:
                    Player.RoomC = [Player.RoomC[0]+1, Player.RoomC[1]]
                    Player.Room = RoomList[RoomCList.index(Player.RoomC)]
                    print('You moved east')
                else:
                    print("That room doesn't exist")
            elif 'north' in command:
                if Player.RoomC== [0,1] and Exit.Lock == True:
                    print(f"Your Score was {Player.Score}")
                    exit("You won the game.\n if you would like to support me please give me three thousand dollars.")
                elif Player.RoomC == [0,1] and Exit.Lock == False:
                    print("The door is locked")
                elif [Player.RoomC[0], Player.RoomC[1]+1] in RoomCList:
                    Player.RoomC = [Player.RoomC[0], Player.RoomC[1]+1]
                    Player.Room = RoomList[RoomCList.index(Player.RoomC)]
                    print('You moved north')
                else:
                    print("That room doesn't exist")
            elif 'south' in command:
                if [Player.RoomC[0], Player.RoomC[1]-1] in RoomCList:
                    Player.RoomC = [Player.RoomC[0], Player.RoomC[1]-1]
                    Player.Room = RoomList[RoomCList.index(Player.RoomC)]
                    print('You moved south')
                else:
                    print("That room doesn't exist")
