#Imports
import time

#Variables
Inventory = []
option = 0
Light/Fan = 0
Gameover + 0

#Function setup
def Question(Prompt, Max):
    Answer = int(input(Prompt))
    if Answer > Max or Answer < 1:
        return "Error"
    return Answer

option = Question("HI >>> ", 2)

def Death(Message):
    print(Message)
    exit()
#Player setup
class Player:
    def __init__(self, Name, Inventory, Hand, Score, Money,x,y):
        self.Inventory = Inventory
        self.Name = Name
        self.Hand = Hand
        self.Score = Score
        self.Money = Money
        self.x = x
        self.y = y
Player = Player(input(''.join(["what is player's name? >>> "])), [], [], 0, 20, 1, 1)

#Main Program
print ("This is an adventure game.\nThe goal of this game is to escape the room")
option = int(input("Do you want to eat the cake 1 or look around the room 2 >"))

if option == 1:
    Death("You died because the cake was poisoned")
if option == 2:
    while Gameover != 1:
    print ("There is a fan, a toybox, a door, and a window.")
option = int(input("Inspect fan 1, inspect toybox 2, inspect door 3, and inspect window 4 >"))
if option == 1:
    if Light/Fan == 0:
        option = int(input("The fan is old and is turned off\nThere is a light switch on wall\nTurn the switch on 1 or don't tough the switch 2 >"))
    if Light/Fan == 1:
        option = int(input("The fan is old and is turned on\nThere is a light switch on wall\nTurn the switch off 1 or don't tough the switch 2 >"))
    if option == 1:
        if Light/Fan ==0:
            Light/Fan = 1
            print ("The fan tuned on and the fan slowly started to turn")
