from Actions import Actions
from Displays import Display

class Character:
    # Characteristics of a Character -----------------------------------------------------------------------------------------------
    def __init__(self, char, action):
        # char = {"Name", "BodyType", "SkinColor", "HairStyle", "HairColor", "Outfits", "Position"}
        self.Action = action
        self.Display = Display(self.Action)

        self.Name = char["Name"]
        self.BodyType = char["BodyType"]
        self.SkinColor = char["SkinColor"]
        self.HairStyle = char["HairStyle"]
        self.HairColor = char["HairColor"]
        self.EyeColor = char["EyeColor"]
        self.Outfits = char["Outfits"]
        self.Position = char["Position"]

        # self.Create_Character()

    # Creating a Character -------------------------------------------------------------------------------------------------------
    def Create_Character(self):
        TF = self.Action.Execute_Command('CreateCharacter' + '(' + self.Name + ', ' + self.BodyType + ')', True)
        # ---------------------------------------- Costumes design
        if TF==True:
            TF = self.Costumes()
        return True

    def Costumes(self):
        TF=0
        TF += self.SetHairStyle(self.HairStyle)
        TF += self.SetHairColor(self.HairColor)
        TF += self.SetSkinColor(self.SkinColor)
        TF += self.SetEyeColor(self.EyeColor)
        TF += self.SetClothing(self.Outfits)
        return True

    def SetHairStyle(self, styleName):
        TF = 0
        TF += self.Action.Execute_Command('SetHairStyle' + '(' + self.Name + ', ' + styleName + ')')
        return True

    def SetHairColor(self, colorName):
        TF = 0
        TF += self.Action.Execute_Command('SetHairColor' + '(' + self.Name + ', ' + colorName + ')')
        return True
    def SetSkinColor(self, colorName):
        TF = 0
        TF += self.Action.Execute_Command('SetSkinColor' + '(' + self.Name + ', ' + colorName + ')')
        return True
    def SetEyeColor(self, colorName):
        TF = 0
        TF += self.Action.Execute_Command('SetEyeColor' + '(' + self.Name + ', ' + colorName + ')')
        return True
    def SetClothing(self, outfitName):
        TF = 0
        TF += self.Action.Execute_Command('SetClothing' + '(' + self.Name + ', ' + outfitName + ')')
        return True

    # Position of a Character ---------------------------------------------------------------------------------------------------
    def Set_Position(self, Position):
        TF = self.Action.Execute_Command('SetPosition(' + self.Name + ', ' + Position + ')', True)
        return TF

    def Sleep(self, place, wait=False):
        TF = self.Action.Execute_Command(f"Sleep({self.Name}, {place})", wait)
        return TF

    def Kneel(self, wait=True):
        TF = self.Action.Execute_Command(f"Kneel({self.Name})", wait)
        return TF

    def Clap(self, wait=True):
        TF = self.Action.Execute_Command(f"PlaySound(Clap)", False)
        TF = self.Action.Execute_Command(f"Clap({self.Name})", wait)
        return TF

    def Enter(self, place, wait=True):
        TF = self.Action.Execute_Command(f"Enter({self.Name}, {place})", wait)
        return TF

    def Exit(self, place, wait=True):
        TF = self.Action.Execute_Command(f"Exit({self.Name}, {place})", wait)
        return TF

    def WalkTo(self, place, wait=True):
        TF = self.Action.Execute_Command(f"WalkTo({self.Name}, {place})", wait)
        return TF

    def Sit(self, place, wait=True):
        TF = self.Action.Execute_Command(f"Sit({self.Name}, {place})", wait)
        return TF
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    def Give(self, item, to):
        # Character gives the item holding on his left hand to another character.
        command = f"Give({self.Name}, {item}, {to})"
        TF = self.Action.Execute_Command(command, True)

    def Drink(self):
        # Character drinks from the items they're holding in their left hand.
        command = f"Drink({self.Name})"
        TF = self.Action.Execute_Command(command, True)

    def Die(self):
        # Character dies.
        command = f"Die({self.Name})"
        TF = self.Action.Execute_Command(command, True)

    def Dance(self):
        # Character dances.
        command = f"Dance({self.Name})"
        TF = self.Action.Execute_Command(command, True)

    def Face(self, object):
        # Character face or look towards the object.
        command = f"Face({self.Name}, {object})"
        TF = self.Action.Execute_Command(command, True)

    def Wave(self):
        # Character waves his hand.
        command = f"Wave({self.Name})"
        TF = self.Action.Execute_Command(command, True)

    def WalkToSpot(self, X, Y, Z):
        # Character walks to a specified path.
        command = f"WalkToSpot({self.Name}, {X}, {Y}, {Z})"
        Tf = self.Action.Execute_Command(command, True)
    def Attack(self, B, Die=""):
        self.Action.Execute_Command(f"WalkTo({self.Name},{B})")
        self.Action.Execute_Command(f"Face({self.Name},{B})")
        self.Action.Execute_Command(f"PlaySound(Draw)", False)
        self.Action.Execute_Command(f"Attack({self.Name},{B})")
        if Die == "A":
            self.Action.Execute_Command(f"Die({self.Name})")
        elif Die == "B":
            self.Action.Execute_Command(f"Die({B})")
        else:
            return True
    def OpenFurniture(self, Furniture):
        self.Action.Execute_Command(f"OpenFurniture({self.Name},{Furniture})", True)
        return True
    def Pickup(self, Object):
        self.Action.Execute_Command(f"Pickup({self.Name},{Object})", True)
        return True
    def Take(self, Object, Position):
        self.Action.Execute_Command(f"Take({self.Name},{Object}, {Position})", True)
        return True
    def Pocket(self, Object):
        self.Action.Execute_Command(f"Pocket({self.Name},{Object})", True)
        return True
    def Unpocket(self, Object):
        self.Action.Execute_Command(f"Unpocket({self.Name},{Object})", True)
        return True