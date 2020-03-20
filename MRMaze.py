from MRMazeConfig import *
print("You are in a house.\nYou must escape.")
while True:
    parse()
    Player.Room = RoomList[RoomCList.index(Player.RoomC)]
