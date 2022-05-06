
class Character_:
    # ----------------------------------------------------------------------------------------------- Characteristics of a Character
    def __init__(self, char, action):
        # char = {"Name", "BodyType", "SkinColor", "HairStyle", "HairColor", "Outfits", "Position"}
        self.Action = action

        self.Name = char["Name"]
        self.BodyType = char["BodyType"]
        self.SkinColor = char["SkinColor"]
        self.HairStyle = char["HairStyle"]
        self.HairColor = char["HairColor"]
        self.EyeColor = char["EyeColor"]
        self.Outfits = char["Outfits"]
        self.Role = char["Role"]

    # ----------------------------------------------------------------------------------------------- Creating a Character
    def CreateCharacter(self):
        TF = self.Action.Execute_Command('CreateCharacter' + '(' + self.Name + ', ' + self.BodyType + ')', True)
        if TF == False:
            self.Action.Execute_Command("Quit()")
        # ---------------------------------------- Costumes design
        else:
            TF = self.Costumes()
        return TF
    # ----------------------------------------------------------------------------------------------- Costumes
    def Costumes(self):
        self.SetHairStyle(self.HairStyle)
        self.SetHairColor(self.HairColor)
        self.SetSkinColor(self.SkinColor)
        self.SetEyeColor(self.EyeColor)
        self.SetClothing(self.Outfits)
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
    def SetClothing(self, outfitName, wait=False):
        TF = 0
        TF += self.Action.Execute_Command('SetClothing' + '(' + self.Name + ', ' + outfitName + ')', wait)
        return True
    def Sleep(self, place, wait=False):
        TF = self.Action.Execute_Command(f"Sleep({self.Name}, {place})", wait)
        return TF
    def Kneel(self, wait=True):
        TF = self.Action.Execute_Command(f"Kneel({self.Name})", wait)
        return TF
    def Cast(self, Object, color='red', wait=True):
        TF = self.Action.Execute_Command("PlaySound(Fireball)")
        TF = self.Action.Execute_Command(f"Cast({self.Name}, {Object}, {color})", wait)
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
        TF = self.Action.Execute_Command(f"Face({self.Name}, {place})", wait)
        return TF
    def Sit(self, place, wait=True):
        TF = self.Action.Execute_Command(f"Sit({self.Name}, {place})", wait)
        return TF
    def Give(self, item, to):
        # Character gives the item holding on his left hand to another character.
        command = f"Give({self.Name}, {item}, {to})"
        TF = self.Action.Execute_Command(command, True)
    def Drink(self):
        # Character drinks from the items they're holding in their left hand.
        command = f"Drink({self.Name})"
        TF = self.Action.Execute_Command(command, True)
    def Die(self):
        if self.BodyType in ['A', 'C', 'E', 'G']:
            self.Action.Execute_Command(f"PlaySound(Death1)")          # for Woman
        else:
            self.Action.Execute_Command(f"PlaySound(Death2)")          # for Woman
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
    def Attack(self, B):
        self.Action.Execute_Command(f"WalkTo({self.Name},{B})", True)
        self.Action.Execute_Command(f"Face({self.Name},{B})", True)
        '''if self.BodyType in ['A', 'C', 'E', 'G']:
            self.Action.Execute_Command(f"PlaySound(Attack1)")          # for Woman
        else:
            self.Action.Execute_Command(f"PlaySound(Attack2)")  '''        # for Man
        self.Action.Execute_Command(f"Attack({self.Name},{B})", True)
        return True
    def OpenFurniture(self, Furniture):
        self.Action.Execute_Command(f"PlaySound(OpenChest)")
        self.Action.Execute_Command(f"OpenFurniture({self.Name},{Furniture})", True)
        return True
    def CloseFurniture(self, Furniture):
        self.Action.Execute_Command(f"PlaySound(CloseChest)")
        self.Action.Execute_Command(f"CloseFurniture({self.Name},{Furniture})", True)
        return True
    def Pickup(self, Object, Place):
        self.Action.Execute_Command(f"PlaySound(Pocket)")
        self.Action.Execute_Command(f"Pickup({self.Name},{Object}, {Place})", True)
        return True
    def Put(self, Object, Place):
        self.Action.Execute_Command(f"Put({self.Name},{Object}, {Place})", True)
        return True
    def PutDown(self, Object):
        self.Action.Execute_Command(f"PutDown({self.Name},{Object})", True)
        return True
    def Take(self, Object, Position):
        self.Action.Execute_Command(f"PlaySound(Pocket)")
        self.Action.Execute_Command(f"Take({self.Name},{Object}, {Position})", True)
        return True
    def Pocket(self, Object):
        self.Action.Execute_Command(f"PlaySound(Pocket)")
        self.Action.Execute_Command(f"Pocket({self.Name},{Object})", True)
        return True
    def Unpocket(self, Object):
        self.Action.Execute_Command(f"PlaySound(Unpocket)")
        self.Action.Execute_Command(f"Unpocket({self.Name},{Object})", True)
        return True
    def Hold_Item_LeftHand(self, Item):
        self.Action.Execute_Command(f"SetPosition({Item}, {self.Name})")
        return True
    def Hold_Item_RightHand(self, Item):
        self.Action.Execute_Command(f"SetPosition({Item}, {self.Name})")
        self.Action.Execute_Command(f"Draw({self.Name}, {Item})")
        return True
    def Expression(self, expression):
        self.Action.Execute_Command(f"SetExpression({self.Name},{expression})", True)
        return True