
class Variables:
    def __init__(self):
        # Character Parameters : [<Name>, <BodyType>, <HairStyle>, <HairColor>, <EyeColor>, <Outfits>, <Position>]
        self.characters = {
            "Bob"       : {"Name": "Bob",   "BodyType": "B",    "SkinColor": "5",   "HairStyle": "Long",    "HairColor": "black",   "EyeColor": "black", "Outfits": "Peasant",   "Position": "BobsHouse.Door"},               # Child Character
            "Angel"     : {"Name": "Angel", "BodyType": "C",    "SkinColor": "5",   "HairStyle": "Long",    "HairColor": "black",   "EyeColor": "red", "Outfits": "Witch",   "Position": "ForestPath.WestEnd"},       # Professor Character
            }
        # Places Parameter : [<Name>, <Type>]
        self.places = {
            "BobsHouse"     : {"Name": "BobsHouse",     "Type": "Cottage"},
            "ForestPath"    : {"Name": "ForestPath",    "Type": "ForestPath"}
            }
        # Item Parameters : [<Name>, <Type>]
        self.items = {
            "BluePotion"    : {"Name": "BluePotion",    "Type": "BluePotion",   "Position": "Angel"},
            "RedPotion"     : {"Name": "RedPotion",     "Type": "RedPotion",    "Position": "Angel"}
            }
        self.icons = {}

