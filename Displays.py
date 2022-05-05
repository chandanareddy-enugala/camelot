# Importing user defined functions
# ----------------------------------
from Actions import Actions

class Display:
    def __init__(self, action):
        self.Action = action

    # Menu --------------------------------------------------------------------------
    def SetMenuTitle(self, message):
        TF = self.Action.Execute_Command(f"SetTitle({message})", True)
        return TF
    def ShowMenu(self):
        TF = self.Action.Execute_Command(f"ShowMenu()", True)
        return TF
    def HideMenu(self):
        TF = self.Action.Execute_Command(f"HideMenu()", True)
        return TF
    def Quit(self):
        TF = self.Action.Execute_Command(f"Quit()")
        return True


    # Narration ---------------------------------------------------------------------
    def SetNarration(self, narration, wait=True):
        TF = self.Action.Execute_Command(f'SetNarration({narration})', wait)
        return TF
    def ShowNarration(self, narration, wait=True):
        TF = self.Action.Execute_Command(f'SetNarration({narration})', wait)
        TF = self.Action.Execute_Command('ShowNarration()')
        while wait:
            if input() == "input Close Narration":
                self.HideNarration()
                return True
                wait=False
        return True
    def HideNarration(self):
        TF = self.Action.Execute_Command('HideNarration()')
        return TF

    # Dialog ------------------------------------------------------------------------
    def SetDialog(self, dialog, wait=True):
        TF = self.Action.Execute_Command(f"SetDialog({dialog})", wait)
        return TF
    def ShowDialog(self, dialogs):
        self.Action.Execute_Command('ShowDialog()')
        TF = 0
        for key in dialogs.keys():
            TF += self.Action.Execute_Command(f"SetDialog({dialogs[key]})", True)
        if TF == len(dialogs):
            return True
    def HideDialog(self):
        TF = self.Action.Execute_Command('HideDialog()', True)
        return TF
    def ClearDialog(self):
        TF = self.Action.Execute_Command(f"ClearDialog()", True)
        return TF

    # Creadit -------------------------------------------------------------------------
    def ShowCredits(self):
        TF = self.Action.Execute_Command(f"ShowCredits()", True)
        return TF
    def HideCredits(self):
        TF = self.Action.Execute_Command(f"HideCredits()", True)
        return TF

    # Furniture ------------------------------------------------------------------------
    def ShowFurniture(self, Object):
        TF = self.Action.Execute_Command(f"ShowFurniture({Object})", True)
        return TF
    def HideFurniture(self, Object):
        TF = self.Action.Execute_Command(f"HideFurniture({Object})", True)
        return TF

    # List -----------------------------------------------------------------------------
    def ShowList(self):
        TF = self.Action.Execute_Command(f"ShowList()", True)
    def HideList(self):
        TF = self.Action.Execute_Command(f"HideList()", True)
        return TF

    # Fade IN | OUT ---
    def FadeIn(self):
        TF = self.Action.Execute_Command(f"FadeIn()", True)
        return TF
    def FadeOut(self):
        TF = self.Action.Execute_Command(f"FadeOut()", True)
        return TF

    # Set DAY-TIME | NIGHT-TIME ---
    def Day(self):
        TF = self.Action.Execute_Command(f"SetDay()")
        return TF

    def Night(self):
        TF = self.Action.Execute_Command(f"SetNight()")
        return TF