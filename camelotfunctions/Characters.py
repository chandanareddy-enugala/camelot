
from Functions.Actions import Actions


class Character:
    # char = {"Name": "Tom", "BodyType": "B", "SkinColor": "7", "HairStyle": "Long", "HairColor": "black", "Outfits": "Peasant"}
    # Characteristics of a Character -----------------------------------------------------------------------------------------------
    def __init__(self, char):
        # char = {"Name", "BodyType", "SkinColor", "HairStyle", "HairColor", "Outfits", "Position"}

        self.Name = char["Name"]
        self.BodyType = char["BodyType"]
        self.SkinColor = char["SkinColor"]
        self.HairStyle = char["HairStyle"]
        self.HairColor = char["HairColor"]
        self.EyeColor = char["EyeColor"]
        self.Outfits = char["Outfits"]
        self.Position = char["Position"]

        self.action = Actions()

        self.Create_Character()             # Creating Character
        self.Create_Design()

    # Creating a Character -------------------------------------------------------------------------------------------------------
    def Create_Character(self):
        self.action.run_command('CreateCharacter' + '(' + self.Name + ', ' + self.BodyType + ')', True)

    def Create_Design(self):
        self.action.run_command('SetSkinColor' + '(' + self.Name + ', ' + self.SkinColor + ')', True)         # Integer in [0, 10]
        self.action.run_command('SetHairStyle' + '(' + self.Name + ', ' + self.HairStyle + ')', True)   # MALE: Long, Mage, Musketeer, Short, Spiky; FEMALE: Bun, Long, Ponytail, Spiky, Straight
        self.action.run_command('SetHairColor' + '(' + self.Name + ', ' + self.HairColor + ')', True)         # gray, black, brown, red, or blonde
        self.action.run_command('SetEyeColor' + '(' + self.Name + ', '  + self.EyeColor + ')', True)  # gray, black, brown, red, or blonde
        self.action.run_command('SetClothing' + '(' + self.Name + ', '  + self.Outfits + ')', True)            # MALE: Bandit, Beggar, HeavyArmour, LightArmour, King, Merchant, Naked, Noble, Peasant, Priest, Warlock

    # Position of a Character ---------------------------------------------------------------------------------------------------
    def Set_Position(self, Position="None"):

        Name = self.Name
        if Position == "None":
            Position = self.Position
        self.action.run_command('SetPosition(' + Name + ', ' + Position + ')', True)

    def WalkTo(self, position):
        command = f"WalkTo({self.Name}, {position})"
        self.action.run_command(command, True)

    def WalkToSpot(self, X, Y, Z):
        command = f"WalkToSpot({self.Name}, {X}, {Y}, {Z})"
        self.action.run_command(command, True)

    def Exit(self, From, TF='false'):
        # Character walks to, opens, and exits through a door.
        # command = "Exit(" + self.Name + ", " + From + ", " + TF
        command = f"Exit({self.Name}, {From}, {TF})"
        self.action.run_command(command, True)

    def Enter(self, To, TF='false'):
        # Character enters from a door.
        # command = "Exit(" + self.Name + ", " + From + ", " + TF
        command = f"Enter({self.Name}, {To}, {TF})"
        self.action.run_command(command, True)
    def Give(self, item, to):
        # Character walks to and hands an item to another character with their left hand.
        command = f"Give({self.Name}, {item}, {to})"
        self.action.run_command(command, True)

    def Drink(self):
        # Character drinks from the items they're holding in their left hand.
        command = f"Drink({self.Name})"
        self.action.run_command(command, True)

    def Die(self):
        # Character drinks from the items they're holding in their left hand.
        command = f"Die({self.Name})"
        self.action.run_command(command, True)

    def Dance(self):
        # Character drinks from the items they're holding in their left hand.
        command = f"Dance({self.Name})"
        self.action.run_command(command, True)

    def Face(self, object):
        command = f"Face({self.Name}, {object})"
        self.action.run_command(command, True)
    def Clap(self):
        command = f"Clap({self.Name})"
        self.action.run_command(command, False)
        command = f"PlaySound(Clap)"
        self.action.run_command(command, True)

    def Wave(self):
        command = f"Wave({self.Name})"
        self.action.run_command(command, True)

    def do(self, functionName, charName, itemName):
        self.action.run_command(functionName + "(" + charName + ", " + itemName + ")", True)