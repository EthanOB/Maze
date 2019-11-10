#Imports
import time

#Variables
option = 0
Gameover = 0
#Function setup
def Question(Prompt, Max):
    Answer = int(input(Prompt))
    if Answer > Max or Answer < 1:
        return "Error"
    return Answer

def Death(Message):
    print(Message)
    exit()

#a ={"pie":True, "cake":False}

def toggle():
    if Fan.Uses == 0:
        Fan.Uses = 1
    elif Fan.Uses == 0:
        Fan.Uses = 1

def clear(times):
    if times == 1:
        print("\n")
    if times == 2:
        print("\n\n")
    if times == 3:
        print ("\n\n\n")

def unlock():
    if Key.Uses == 0:
        Door.Uses = 1
        Key.Uses = 1
    if Key.Uses == 1:
        print("Sorry, you have already unlocked the door")

def lock()
    if Door.Uses == 0:
        print ("Sorry, the dorr is locked")
    if the Door.Uses == 1:
#Classes
class Object:
    def __init__(self, Name, Func, Uses):
        self.Name = Name
        self.Func = Func
        self.Uses = Uses


#sadfasdf = Object("A", a)
#hi = Object("A", c)
#hi.Func()
#sadfasdf.Func()
class Player:
    def __init__(self, Name, Inventory, Hand, Score, Money):
        self.Inventory = Inventory
        self.Name = Name
        self.Hand = Hand
        self.Score = Score
        self.Money = Money
        self.Pos = [0, 0]

Player = Player(input(''.join(["what is player's name? >>> "])), [], [], 0, 20)

#Player.Pos[0] is x
#Player.Pos[1] is y
#def go(direction):
#     if direction == "west":
#         Player.Pos[0] = Player.Pos[0] - 1
#def Objects
Key = Object("Key", unlock, 0)
Fan = Object("Fan", toggle, 0)
Door = object("Fan", locked, 0)

#Main Program
print ("This is an adventure game.\nThe goal of this game is to escape the room")
option = Question("Hello\nDo you want to play a multiroom game 1 or single roomed game 2\n(note only the single room game is working at the movement) >", 2)
clear(2)
if option == 1:
    print ("Error\nThis part of the program doesn't exist at the moment")
    exit()
if option == 2:
    while 1==1:
        clear(2)
        print ("There is a fan, a cake, a toybox, a door, and a window in the room")
        clear(1)
        option = Question("Inspect fan 1, cake 2, inspect toybox 3, inspect door 4, and inspect window 5 >", 5)
        if option == 1:
            if Fan.Uses == 0:
                option = Question("The fan is old and is turned off\nThere is a light switch on wall\nTurn the switch on 1 or don't touch the switch 2 >", 2)
                if option == 1:
                    Fan.Func()
                    print("the lights turned on and the fan started to slowerly turn")
            elif Fan.Uses == 1:
                option = Question("The fan is old and is turned on\nThere is a light switch on wall\nTurn the switch off 1 or don't touch the switch 2 >", 2)
                if option == 1:
                    Fan.Func()
                    print("The light turned off and the fan slowerly stopped")
        if option == 2:
            Death("You have dead because you at the poisoned cake")
        if option == 3:
            option = Question("You see an old blue toybox\nDo you want to open to toybox 1 or don't touch it 2", 2)
            if option == 1:
                option = Question("There are some old toys and stuffed animals\nDo you want to investigate more 1 or go back to the room 2", 2)
                if option == 1:
                    option = Question("There are keys in the bottom of the toybox\nDo you want to obtain the key 1 or go back to the room 2", 2)
                    if option == 1:
                        Player.Inventory = Player.Inventory + Key
