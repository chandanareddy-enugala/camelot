from Set import Set_
class Message_:
    def __init__(self, message, action):
        self.Action = action
        self.Message = message
        self.Set = Set_(action)

        self.ShowDialogCount = 0   # To track how many times the Dialog window is opened.

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% NARRATIONS
    def SetNarration(self, narration, wait=True):
        TF = self.Action.Execute_Command(f"SetNarration('{narration}')", wait)
        return TF
    def ShowNarration(self, wait=True):
        TF = self.Action.Execute_Command('ShowNarration()', wait)
        for narration in self.Message:
            TF = self.SetNarration(narration)
            self.Set.Wait(1)
        while True:
            camelotMessage = input()
            if camelotMessage == "input Close Narration":
                TF = self.HideNarration()
                return camelotMessage
    def HideNarration(self):
        TF = self.Action.Execute_Command('HideNarration()')
        return TF

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% DIALOGS
    def ShowDialogs(self, Entity_1='null', Entity_2='null'):
        TF = self.Action.Execute_Command("DisableInput()")
        TF = self.ShowDialogBox(Entity_1, Entity_2)
        for dialog in self.Message:
            self.SetDialog(dialog)
        self.SetDialog("--------------")
        self.SetDialog("To close this DialogBox: Click 'CLOSE' or Press 'ESC'")
        self.SetDialog("[CLOSE|CLOSE]")
        camelotMessage = input()
        if ("QUIT" in camelotMessage):
            self.ClearDialog()
            self.SetDialog("|----- STORY ENDS -----|")
            self.ShowDialog()
            self.Action.Execute_Command("Wait(3)")
            self.ClearDialog()
            while self.ShowDialogCount>0:
                self.HideDialog()
                self.ShowDialogCount -= 1
            else:
                self.HideDialog()
                self.ShowDialogCount -= 1
        elif ("Key" in camelotMessage) or ("CLOSE" in camelotMessage) or ("RETURN" in camelotMessage) or ("RESTART" in camelotMessage):
            self.ClearDialog()
            while self.ShowDialogCount > 0:
                self.HideDialog()
                self.ShowDialogCount -= 1
            else:
                self.HideDialog()
                self.ShowDialogCount -= 1
            self.Action.Execute_Command("EnableInput()")
        return camelotMessage

    def ShowDialogBox(self, Entity_1='null', Entity_2='null', wait=True):
        if Entity_1 != 'null':  TF = self.Action.Execute_Command(f"SetLeft({Entity_1})", wait)
        if Entity_2 != 'null': TF = self.Action.Execute_Command(f"SetRight({Entity_2})", wait)
        TF = self.ShowDialog()
        return True
    def ShowDialog(self):
        TF = self.Action.Execute_Command('ShowDialog()', True)
        self.ShowDialogCount += 1
        return TF
    def SetDialog(self, dialog, wait=True):
        TF = self.Action.Execute_Command(f'SetDialog("{dialog}")', wait)
        return TF
    def ClearDialog(self):
        TF = self.Action.Execute_Command(f"ClearDialog()", True)
        return TF
    def HideDialog(self):
        TF = self.Action.Execute_Command('HideDialog()', True)
        self.ShowDialogCount -= 1
        return TF

