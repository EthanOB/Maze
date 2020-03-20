#def lists
parseobject = []
command = []
Start = 0
Answer = ''
#def Varaible
objectN = 0
#def Classes
class Room:
    def __init__(self,Name,C, OIR, OIRN, Descript, MDirections):
        self.C = C
        self.OIR = OIR
        self.OIRN = OIRN
        self.Descript = Descript
        self.MDirections = MDirections

class Player:
    def __init__(self, Name, Inventory, Hand, Score, Money, Room, RoomC):
        self.Inventory = Inventory
        self.Name = Name
        self.Hand = Hand
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
    exit("You were blown up")

def Lookup(RequestedObject):
    print(f"{RequestedObject}") # this is the way to display death for future use

#def Objects
bomb = Object("bomb", boom)
pie = Object("pie", boom)

Table = {"bomb": bomb, "pie": pie}
#def Rooms Room = Room(Position, objects in room)
WestRoom = Room("WestRoom",[-1,0], pie, 'pie', ("You are in the westroom and it is very dark. \nYou can move east."),('east'))
FrontRoom = Room("FrontRoom",[0,0], bomb, 'bomb', ("You are in the frontroom.\nYou can move west, south, east, and north."),('west','east','north','south'))
RoomCList =[[0,0], [-1,0]]
RoomList = [FrontRoom, WestRoom]
#def Player
Player = Player(input("what is player's name? >>> "), [], [pie],0,0,FrontRoom,[0,0])

#def parse
def parse():
        Answer = input("What do you want to do >")
        command = Answer.lower().split()
        i = 0
        StartS = 0
        while i < len(command):
            if command[i] == 'use':
                StartS = i
                if command[StartS+1] in Player.Inventory:
                    print ("this is okay")

            if command[i] == 'take':
                StartS = i
                if command[StartS+1] == (Player.Room).OIRN:
                    print('This is working')
                    Player.Inventory.append((Player.Room).OIR)
            elif command[i] == 'look':
                StartS = i
                if command[StartS+1] == 'around':
                    print(((Player.Room).Descript, (Player.Room)))
                    break
                if command[StartS+1] == 'inventory':
                    print((Player.Inventory).Name)
                    break
            elif command[i] == 'move':
                StartS = i
                if command[StartS+1] == 'west':
                    if [Player.RoomC[0]-1, Player.RoomC[1]] in RoomCList:
                        Player.RoomC = [Player.RoomC[0]-1, Player.RoomC[1]]
                        print('You moved west')
                        break
                    else:
                        print("That room doesn't exist")
                elif command[StartS+1] == 'east':
                    if [Player.RoomC[0]+1, Player.RoomC[1]] in RoomCList:
                        Player.RoomC = [Player.RoomC[0]+1, Player.RoomC[1]]
                        print('You moved east')
                        break
                    else:
                        print("That room doesn't exist")
                elif command[StartS+1] == 'north':
                    if [Player.RoomC[0], Player.RoomC[1]+1] in RoomCList:
                        Player.RoomC = [Player.RoomC[0], Player.RoomC[1]+1]
                        print('You moved north')
                        break
                    else:
                        print("That room doesn't exist")
                elif command[StartS+1] == 'south':
                    if [Player.RoomC[0], Player.RoomC[1]-1] in RoomCList:
                        Player.RoomC = [Player.RoomC[0], Player.RoomC[1]-1]
                        print('You moved south')
                        break
                    else:
                        print("That room doesn't exist")
            i = i + 1
