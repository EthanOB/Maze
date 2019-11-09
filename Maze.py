#Imports
import time

#Variables
Inventory = []
option = 0
Fan = 0
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
a ={"pie":True, "cake":False}

#def a():
#    print(1)
#def c():
#    print(100)
#Classes
class Object:
    def __init__(self, Name, Func):
        self.Name = Name
        self.Func = Func

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
def go(direction):
     if direction == "west":
         Player.Pos[0] = Player.Pos[0] - 1

#Main Program
print ("This is an adventure game.\nThe goal of this game is to escape the room")
option = Question("Do you want to play a multiroom game 1 or single roomed game 2.\n (note only the single room game is working at the movement)")
if option == 2:
    option = Question("Do you want to eat the cake 1 or look around the room 2 >", 2)

    if option == 1:
        Death("You died because the cake was poisoned")
        if option == 2:
            while Gameover == 
            print ("There is a fan, a toybox, a door, and a window.")
            option = Question("Inspect fan 1, inspect toybox 2, inspect door 3, and inspect window 4 >", 4)
            if option == 1:
                if Fan == 0:
                    option = Question("The fan is old and is turned off\nThere is a light switch on wall\nTurn the switch on 1 or don't tough the switch 2 >", 2)
                    if Fan == 1:
                        option = Question("The fan is old and is turned on\nThere is a light switch on wall\nTurn the switch off 1 or don't tough the switch 2 >", 2)
                        if option == 1:
                            if Fan ==0:
                                Fan = 1
                                print ("The fan tuned on and the fan slowly started to turn")
if option == 1:
    return "Error"
