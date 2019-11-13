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

def List(List):
    temp = []
    i = 0
    while i < len(List):
        temp.append(Player.Inventory[i].Name)
        i = i + 1
    return ", ".join(temp)

def toggle():
    Fan.Uses = not Fan.Uses

def clear(times):
    print("\n"*times)

def togglelock():
    Key.Uses = not Key.Uses
    Door.Uses = not Door.Uses

def locked():
    if Door.Uses == False:
        print ("\nSorry, the door is locked and there is a keyhole")
    if Door.Uses == True:
        option = Question("The door is unlocked\nWould you like to leave the room 1 or stay in the room 2", 2)
        if option == 1:
            print ("You won the game and escaped the room!\nThe game is now terminating")
            exit()
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
Key = Object("Key", togglelock, False)
Fan = Object("Fan", toggle, False)
Door = Object("Fan", locked, False)

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
        option = Question("Inspect fan 1, cake 2, toybox 3, door 4, and window 5\nview inventory 6 >", 6) #Window???
        if option == 1:
            if Fan.Uses == False:
                option = Question("The fan is old and is turned off\nThere is a light switch on wall\nTurn the switch on 1 or don't touch the switch 2 >", 2)
                if option == 1:
                    Fan.Func()
                    print("the lights turned on and the fan started to slowerly turn")
            elif Fan.Uses == True:
                option = Question("The fan is old and is turned on\nThere is a light switch on wall\nTurn the switch off 1 or don't touch the switch 2 >", 2)
                if option == 1:
                    Fan.Func()
                    print("\nThe light turned off and the fan slowerly stopped")
        elif option == 2:
            Death("\nYou have dead because you at the poisoned cake")
        elif option == 3:
            option = Question("\nYou see an old blue toybox\nDo you want to open to toybox 1 or don't touch it 2 >", 2)
            if option == 1:
                option = Question("\nThere are some old toys and stuffed animals\nDo you want to investigate more 1 or go back to the room 2 >", 2)
                if option == 1:
                    option = Question("\nThere are keys in the bottom of the toybox\nDo you want to obtain the key 1 or go back to the room 2 >", 2)
                    if option == 1:
                        Player.Inventory.append(Key)
                        print("You obtained the key")
        elif option == 4:
            Door.Func()
        elif option == 5:
                    print("There is a slightly cracked window")

        elif option == 6 and len(Player.Inventory) > 0:
            option = Question(f"{List(Player.Inventory)} \nType in the number of the item you want to use", len(Player.Inventory))
            if option > len(Player.Inventory):
                Player.Inventory[-1].Func()
            elif option < len(Player.Inventory):
                Player.Inventory[0].Func()
            else:
                Player.Inventory[(option - 1)].Func()
        elif option == 6 and len(Player.Inventory) == 0:
            print("\nSorry, there is nothing in your inventory")
