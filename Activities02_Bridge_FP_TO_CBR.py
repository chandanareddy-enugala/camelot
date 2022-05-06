from Messages import Message_

class Activities_Bridge_FP_to_CBR_:
    def __init__(self, V):
        self.V = V
        self.Status_TaskCompletion = ""
        # -------------------------------------------------- Creating Place
        self.Place_Bridge = V.Place_Bridge
        # -------------------------------------------------- Characters
        self.Char_Bob = V.Char_Bob
        self.Char_Amelia_S = V.Char_Amelia_S
        self.V.Set.Position(self.Char_Amelia_S.Name, self.Place_Bridge.Flowers)
        # -------------------------------------------------- Items
        self.Item_PurpleBook = V.Item_PurpleBook  # Instructions

        self.Icon_Talk = V.Icon_Talk
        self.Icon_ExitDoor = V.Icon_ExitDoor
        self.Icon_Talk.EnableIcon(self.Char_Amelia_S.Name)
        self.V.Char_Bob_Inventory.Add(self.Item_PurpleBook.Name, "Game Instructions")

        # -------------------------------------------------- Sounds
        self.SEffect_Danger1 = self.V.SEffect_Danger1
        # -------------------------------------------------- Narration Message
        Message = f"Going Home"
        _ = Message_([Message], self.V.Action).ShowNarration()
        # -------------------------------------------------- Camera Settings
        self.V.Set.CameraFocus(self.Place_Bridge.SouthEnd)
        self.V.Set.CameraMode('track')
        self.V.Set.CameraBlend(4)

    def SC_Start(self):
        self.V.Set.DisableInput()
        self.V.Display.FadeIn()

        self.Char_Bob.Enter(self.Place_Bridge.SouthEnd)
        self.V.Set.CameraFocus(self.Char_Bob.Name)
        self.V.Set.CameraMode('follow')
        return

    def UC_Select_Task(self):
        self.V.Set.EnableInput()
        self.SEffect_Danger1.Play()
        while True:
            self.camelotMessage = input()
            # -------------------------- Task01 - Bob - Talk - Amelia --------------------------
            if ("Talk" in self.camelotMessage) and (self.Char_Amelia_S.Name in self.camelotMessage):
                self.SC_Task01_Bob_Amelia_Talk()

            # -------------------------- Task02 - Bob - Exit - Bridge --------------------------
            elif ("Icon ExitDoor" in self.camelotMessage) and (self.Char_Amelia_S.Name in self.camelotMessage):
                self.SC_Task02_Bob_Exit_Bridge()
                self.SEffect_Danger1.Stop()
                return
            elif "Interact" in self.camelotMessage:
                self.Bridge_Hints()
            # -------------------------- Bob - Inventory --------------------------
            elif "Inventory" in self.camelotMessage:
                self.Activities_Bob_Inventory()
            # -------------------------- Pause | Resume --------------------------
            elif self.camelotMessage == "input Key Pause":
                self.V.Display.Menu_Show()

    def SC_Task01_Bob_Amelia_Talk(self):
        self.V.Set.DisableInput()
        self.D_Bridge_Bob_Amelia_Talk_English = self.V.D_Bridge_Bob_Amelia_Talk_English
        self.D_Bridge_Bob_Amelia_Talk_English.ShowDialogs(self.Char_Bob.Name, self.Char_Amelia_S.Name)
        self.V.SEffect_Pocket.Play()
        self.Icon_Talk.DisableIcon(self.Char_Amelia_S.Name)
        self.Icon_ExitDoor.EnableIcon(self.Char_Amelia_S.Name)
        self.Status_TaskCompletion = "Task01 --> "
        self.V.Set.EnableInput()

    def SC_Task02_Bob_Exit_Bridge(self):
        self.V.Set.DisableInput()
        self.Char_Bob.Exit(self.Place_Bridge.NorthEnd)
        self.V.Display.FadeOut()
        self.Icon_ExitDoor.DisableIcon(self.Char_Amelia_S.Name)
        self.Status_TaskCompletion += " Task02 --> "

    def Bridge_Hints(self):
        self.V.Set.DisableInput()
        if self.Status_TaskCompletion == "":
            Message = f"HINT : Talk to {self.Char_Amelia_S.Name}"
            _ = Message_([Message], self.V.Action).ShowNarration()
        elif "Task01" in self.Status_TaskCompletion:
            Message = f"HINT : Exit the place by selecting icon on {self.Char_Amelia_S.Name}"
            _ = Message_([Message], self.V.Action).ShowNarration()

    def Activities_Bob_Inventory(self):
        self.V.Set.DisableInput()
        self.V.Char_Bob_Inventory.Show()
        while True:
            self.camelotMessage = input()
            if (self.camelotMessage == "input Close List") or (self.camelotMessage == "input Key Pause"):
                self.V.Char_Bob_Inventory.Hide()
                self.V.Set.EnableInput()
                break
            elif "Game Instructions" in self.camelotMessage:
                self.V.Char_Bob_Inventory.Hide()
                self.V.D_GameInstructions.ShowDialogs(self.Char_Bob.Name)
                self.V.Set.EnableInput()
                self.V.Char_Bob_Inventory.Show()

'''from GlobalVariables import Variables
V = Variables()
ABFC = Activities_Bridge_FP_to_CBR_(V)
ABFC.SC_Start()
ABFC.UC_Select_Task()
'''