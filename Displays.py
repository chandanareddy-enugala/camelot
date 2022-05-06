# Importing user defined functions
# ----------------------------------
class Display:
    def __init__(self, action):
        self.Action = action
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% MENU
    def Menu_Title_Set(self, message):
        TF = self.Action.Execute_Command(f"SetTitle({message})", True)
        return TF
    def Menu_Show(self):
        TF = self.Action.Execute_Command("PlaySound(Menu)")
        TF = self.Action.Execute_Command(f"ShowMenu()", True)
        while True:
            camelotMessage = input()
            for message in ["Start", "Resume", "Pause"]:
                if message in camelotMessage:
                    self.Menu_Hide()
                    self.Action.Execute_Command(f"EnableInput()", True)
                    return True
            if camelotMessage == "input Selected Start":
                TF = self.Menu_Hide()
                return True
            elif camelotMessage == "input Selected Credits":
                TF = self.Menu_Show_Credits()
            elif camelotMessage == "input Selected Quit":
                TF = self.Menu_Quit()
            elif camelotMessage == "input Selected Resume":
                TF = self.Menu_Hide()
            elif camelotMessage == "input Close Credits":
                TF = self.Menu_Hide_Credits()

    def Menu_Hide(self):
        TF = self.Action.Execute_Command("PlaySound(Button)")
        TF = self.Action.Execute_Command(f"HideMenu()", True)
        return TF
    # -------------------------------------------------------------- Credits
    def Menu_Show_Credits(self):
        TF = self.Action.Execute_Command("PlaySound(Menu)")
        TF = self.Action.Execute_Command(f"ShowCredits()", True)
        return TF
    def Menu_Hide_Credits(self):
        TF = self.Action.Execute_Command("PlaySound(Menu)")
        TF = self.Action.Execute_Command(f"HideCredits()", True)
        return TF
    def Menu_Quit(self):
        TF = self.Action.Execute_Command("PlaySound(Flute1)")
        TF = self.Action.Execute_Command(f"Quit()")
        return TF
    def Menu_Show_Resume(self):
        TF = self.Action.Execute_Command("PlaySound(Menu)")
        TF = self.Action.Execute_Command(f"ShowMenu()", True)
        return TF
    def Menu_Hide_Resume(self):
        TF = self.Action.Execute_Command("PlaySound(Menu)")
        TF = self.Action.Execute_Command(f"HideMenu()", True)
        return TF

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% FURNITURES
    def ShowFurniture(self, Object):
        TF = self.Action.Execute_Command(f"ShowFurniture({Object})", True)
        return TF
    def HideFurniture(self, Object):
        TF = self.Action.Execute_Command(f"HideFurniture({Object})", True)
        return TF

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% DAY | NIGHT
    # --------------------------------------------------------------- Fade IN | OUT
    def FadeIn(self):
        TF = self.Action.Execute_Command("PlaySound(Unpocket)")
        TF = self.Action.Execute_Command(f"FadeIn()", True)
        return TF
    def FadeOut(self):
        TF = self.Action.Execute_Command("PlaySound(Unpocket)")
        TF = self.Action.Execute_Command(f"FadeOut()", True)
        return TF
    # --------------------------------------------------------------- Set DAY-TIME | NIGHT-TIME
    def Day(self):
        TF = self.Action.Execute_Command(f"SetDay()")
        TF = self.Action.Execute_Command("PlaySound(Forest_Day)")
        TF = self.Action.Execute_Command("Wait(2)")
        return TF
    def Night(self):
        TF = self.Action.Execute_Command(f"SetNight()")
        TF = self.Action.Execute_Command("PlaySound(Forest_Night)")
        TF = self.Action.Execute_Command("Wait(2)")
        return TF

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% LISTS
    def AddToList(self, Object, Description=""):
        TF = self.Action.Execute_Command(f"AddToList({Object}, {Description})", True)
        return True
    def RemoveFromList(self, Object):
        TF = self.Action.Execute_Command(f"RemoveFromList({Object})", True)
        return True
    def ShowList(self, ObjectsList, Entity):
        for object in ObjectsList:
            self.AddToList(object)
        TF = self.Action.Execute_Command(f"ShowList({Entity})", True)
        return True

    def HideList(self):
        TF = self.Action.Execute_Command(f"HideList()", True)
        return TF
    def ClearList(self):
        TF = self.Action.Execute_Command(f"ClearList()", True)
        return TF
