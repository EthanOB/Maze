from MRMazeConfig import *
NList = []
while True:
    RoomControlls()
    parse()
    print(f"{Player.Name}")
    if len(Player.Inventory) > 0:
        NList.append(Player.Inventory)
        print(f"{str(Player.Inventory)}")
