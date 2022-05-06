from Messages import Message_

class Activities_Ruins:
    def __init__(self, V):
        self.V = V
        self.camelotMessage = ""

        self.V.Set.Position(self.V.Char_Jim_S.Name, self.V.Place_Ruins.Plant)
        self.V.Set.Position(self.V.Char_Jack_S.Name, self.V.Place_Ruins.DirtPile)
        self.V.Set.Position(self.V.Char_Devil.Name, self.V.Place_Ruins.Throne)
        self.V.Char_Devil.Sit(self.V.Place_Ruins.Throne)

        # Remove later
        self.V.Set.Position(self.V.Item_BobSword.Name, self.V.Char_Bob.Name)
        self.V.Char_Bob.Pocket(self.V.Item_BobSword.Name)
        self.V.Char_Bob_Inventory.Add(self.V.Item_BobSword.Name)

        self.V.Set.Position(self.V.Item_DevilSword.Name, self.V.Char_Devil.Name)
        self.V.Char_Devil.Pocket(self.V.Item_DevilSword.Name)

        self.V.Icon_Attack.EnableIcon(self.V.Item_Hammer.Name)

    def SC_Start(self):
        self.V.Set.CameraFocus(self.V.Place_Ruins.Exit)
        self.V.Set.CameraMode('track')
        self.V.Set.CameraBlend(2)
        self.V.Display.FadeIn()

        self.V.Char_Bob.Enter(self.V.Place_Ruins.Exit)
        self.V.Set.CameraFocus(self.V.Char_Bob.Name)
        self.V.Set.CameraMode('follow')

        self.V.Icon_Talk.EnableIcon(self.V.Char_Devil.Name)
        return
    def UC_Select_Task(self):
        self.V.Set.EnableInput()
        while True:
            self.camelotMessage = input()
            # ---------- Task01 - Bob - Devil - Talk ----------
            if ("Icon Talk" in self.camelotMessage) and (self.V.Char_Devil.Name in self.camelotMessage):
                self.SC_Task01_Bob_Devil_Talk()
                self.V.Set.Position(self.V.Char_Angel.Name, self.V.Place_Ruins.Chest)
                self.V.Icon_Talk.EnableIcon(self.V.Char_Angel.Name)

            # ---------- Task05 - Bob - Angel - Talk ----------
            elif ("Icon Talk" in self.camelotMessage) and (self.V.Char_Angel.Name in self.camelotMessage):
                self.SC_Task05_Bob_Angel_Talk()
                self.V.Icon_Take.EnableIcon(self.V.Char_Angel.Name)
            # ---------- Task06 - Bob - Angel - Medicine ----------
            elif ("Icon Take" in self.camelotMessage) and (self.V.Char_Angel.Name in self.camelotMessage):
                self.SC_Task06_Bob_Angel_Get_Medicine()
                self.V.Icon_Take.DisableIcon(self.V.Char_Angel.Name)
                self.V.Icon_ExitPlace.EnableIcon(self.V.Char_Angel.Name)
            # ---------- Task07 - Bob - Exit - Ruins ----------
            elif ("Icon ExitPlace" in self.camelotMessage) and (self.V.Char_Angel.Name in self.camelotMessage):
                self.SC_Task07_Bob_Exit_Ruins()
                return
            # -------------------------- Bob - Inventory --------------------------
            elif "Inventory" in self.camelotMessage:
                self.Activities_Bob_Inventory()
            # -------------------------- Pause | Resume --------------------------
            elif self.camelotMessage == "input Key Pause":
                self.V.Display.Menu_Show()

    # ---------- Task01 - Bob - Devil - Talk ----------
    def SC_Task01_Bob_Devil_Talk(self):
        self.V.Set.DisableInput()
        Message = ["BOB: I am here to get medicine to my wife Please give me",
                   "DEVIL: No I can not give To get it you need to win in the war",
                   "DEVIL: Hey warriors kill this person"]
        _ = Message_(Message, self.V.Action).ShowDialogs(self.V.Char_Bob.Name, self.V.Char_Devil.Name)
        self.V.Icon_Talk.DisableIcon(self.V.Char_Devil.Name)
        self.V.Icon_Take.EnableIcon(self.V.Item_BobSword.Name)
        self.V.Icon_Attack.EnableIcon(self.V.Char_Jim_S.Name)
        self.V.Char_Bob.Face(self.V.Char_Jim_S.Name)
        self.Status_TaskCompletion = "Task01 --> "
        self.V.Set.EnableInput()
        self.SC_Task02_Bob_Jim_Attack()
        return
    # ---------- Task02 - Bob - Jim - Attack ----------
    def SC_Task02_Bob_Jim_Attack(self):
        self.V.Set.DisableInput()
        self.V.Char_Jim_S.Face(self.V.Char_Jack_S.Name)
        self.V.Char_Jim_S.WalkTo(self.V.Char_Bob.Name)
        self.V.Char_Jim_S.Attack(self.V.Char_Bob.Name)
        self.V.Set.EnableInput()
        Jim_Life_Value = 100
        while Jim_Life_Value > 0:
            camelotMessage = input()
            # print(camelotMessage, self.V.Item_BobSword.Name)
            if ("Icon Attack" in camelotMessage) and (self.V.Char_Jim_S.Name in camelotMessage):
                self.V.Set.DisableInput()
                self.V.Char_Bob.Attack(self.V.Char_Jim_S.Name)
                Jim_Life_Value -= 30
                self.V.Set.EnableInput()
            # -------------------------- Bob - Inventory --------------------------
            elif "Inventory" in camelotMessage:
                _ = self.Activities_Bob_Inventory()
            # -------------------------- Pause | Resume --------------------------
            elif camelotMessage == "input Key Pause":
                self.V.Display.Menu_Show()
        self.V.Char_Jim_S.Die()
        self.V.Icon_Attack.DisableIcon(self.V.Char_Jim_S.Name)
        self.V.Icon_Attack.EnableIcon(self.V.Char_Jack_S.Name)
        self.Status_TaskCompletion = "Task02 --> "
        self.SC_Task03_Bob_Jack_Attack()
        return
    # ---------- Task03 - Bob - Jack - Attack ----------
    def SC_Task03_Bob_Jack_Attack(self):
        Jack_Life_Value = 100
        self.V.Char_Jack_S.WalkTo(self.V.Char_Bob.Name, False)
        while Jack_Life_Value > 0:
            camelotMessage = input()
            if ("Icon Attack" in camelotMessage) and (self.V.Char_Jack_S.Name in camelotMessage):
                self.V.Set.DisableInput()
                self.V.Char_Bob.Attack(self.V.Char_Jim_S.Name)
                Jack_Life_Value -= 50
                self.V.Set.EnableInput()
            # -------------------------- Pause | Resume --------------------------
            elif camelotMessage == "input Key Pause":
                self.V.Display.Menu_Show()
        self.V.Set.DisableInput()
        self.V.Char_Jack_S.Die()
        self.V.Icon_Attack.DisableIcon(self.V.Char_Jack_S.Name)
        self.V.Icon_Attack.EnableIcon(self.V.Char_Devil.Name)
        self.V.Icon_FireSpell.EnableIcon(self.V.Char_Devil.Name)
        self.Status_TaskCompletion = "Task03 --> "
        self.V.Set.EnableInput()
        self.SC_Task04_Bob_Devil_Attack()
        return
    # ---------- Task04 - Bob - Devil - Attack ----------
    def SC_Task04_Bob_Devil_Attack(self):
        Devil_Life_Value = 200
        self.V.Set.DisableInput()
        self.V.Char_Devil.WalkTo(self.V.Place_Ruins.Throne)
        self.V.Char_Devil.Unpocket(self.V.Item_DevilSword.Name)
        self.V.Char_Devil.Hold_Item_RightHand(self.V.Item_DevilSword.Name)
        self.V.Char_Devil.Face(self.V.Char_Bob.Name)
        self.V.Set.EnableInput()
        while Devil_Life_Value > 0:
            camelotMessage = input()
            if ("Icon Attack" in camelotMessage) and (self.V.Char_Devil.Name in camelotMessage):
                self.V.Set.DisableInput()
                self.V.Char_Bob.Attack(self.V.Char_Devil.Name)
                self.V.Char_Devil.Attack(self.V.Char_Bob.Name)
                Devil_Life_Value -= 30
                self.V.Set.EnableInput()
            elif ("Icon FireSpell" in camelotMessage) and (self.V.Char_Devil.Name in camelotMessage):
                self.V.Set.DisableInput()
                self.V.Char_Bob.Pocket(self.V.Item_BobSword.Name)
                self.V.Char_Bob.Cast(self.V.Char_Devil.Name)
                Devil_Life_Value -= 60
                self.V.Char_Bob.Unpocket(self.V.Item_BobSword.Name)
                self.V.Char_Bob.Hold_Item_RightHand(self.V.Item_BobSword.Name)
                self.V.Char_Devil.Attack(self.V.Char_Bob.Name)
                self.V.Set.EnableInput()
            elif ("Icon Attack" in camelotMessage) and (self.V.Item_Hammer.Name in camelotMessage):
                self.V.Set.DisableInput()
                self.V.Char_Bob.Pocket(self.V.Item_BobSword.Name)
                self.V.Char_Bob.Unpocket(self.V.Item_Hammer.Name)
                self.V.Char_Bob_Inventory.Remove(self.V.Item_Hammer.Name)
                self.V.Char_Bob.Attack(self.V.Char_Devil.Name)
                Devil_Life_Value -= 40
                self.V.Char_Bob.Unpocket(self.V.Item_BobSword.Name)
                self.V.Char_Bob.Hold_Item_RightHand(self.V.Item_BobSword.Name)
                self.V.Char_Devil.Attack(self.V.Char_Bob.Name)
                self.V.Set.EnableInput()
            # -------------------------- Pause | Resume --------------------------
            elif camelotMessage == "input Key Pause":
                self.V.Display.Menu_Show()
        self.V.Set.DisableInput()
        self.V.Char_Devil.Die()
        self.V.Icon_Attack.DisableIcon(self.V.Char_Devil.Name)
        self.V.Icon_FireSpell.DisableIcon(self.V.Char_Devil.Name)
        self.Status_TaskCompletion = "Task04 --> "
        self.V.Set.EnableInput()
        return
    # ---------- Task05 - Bob - Angel - Talk ----------
    def SC_Task05_Bob_Angel_Talk(self):
        self.V.Set.DisableInput()
        self.V.Char_Bob.Pocket(self.V.Item_BobSword.Name)
        Message = ["ANGEL: Lucky boy You have won the battle Come here and take the medicine",
                   "BOB: Okay Thank you so much for saving my wifes life"]
        _ = Message_(Message, self.V.Action).ShowDialogs(self.V.Char_Bob.Name, self.V.Char_Angel.Name, "happy", "happy")
        self.Status_TaskCompletion = "Task05 --> "
        self.V.Set.EnableInput()
        return
    # ---------- Task06 - Bob - Angel - Medicine ----------
    def SC_Task06_Bob_Angel_Get_Medicine(self):
        self.V.Set.DisableInput()
        self.V.Char_Angel.Give(self.V.Item_Bottle.Name, self.V.Char_Bob.Name)
        self.V.Char_Bob.Dance()
        self.V.Char_Bob.Pocket(self.V.Item_Bottle.Name)
        self.V.Char_Bob_Inventory.Add(self.V.Item_Bottle.Name)
        self.Status_TaskCompletion = "Task06 --> "
        self.V.Set.EnableInput()
        return
    # ---------- Task06 - Bob - Angel - Medicine ----------
    def SC_Task07_Bob_Exit_Ruins(self):
        self.V.Set.DisableInput()
        self.V.Char_Bob.Exit(self.V.Place_Ruins.Exit)
        _ = Message_(["Bob is happy and revives the Candy life by giving this medicine",
                      "--------- Game Ends ---------"], self.V.Action).ShowNarration()
        self.V.Display.FadeOut()
        self.V.Display.Menu_Quit()
        self.Status_TaskCompletion = "Task07 --> "
        return

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
                self.V.D_GameInstructions.ShowDialogs(self.V.Char_Bob.Name)
                self.V.Set.EnableInput()
                self.V.Char_Bob_Inventory.Show()
            elif ("Icon Take" in self.camelotMessage) and (self.V.Item_BobSword.Name in self.camelotMessage):
                self.V.Set.DisableInput()
                self.V.Char_Bob_Inventory.Remove(self.V.Item_BobSword.Name)
                self.V.Char_Bob_Inventory.Hide()
                self.V.Char_Bob.Unpocket(self.V.Item_BobSword.Name)
                self.V.Char_Bob.Hold_Item_RightHand(self.V.Item_BobSword.Name)
                self.V.Set.EnableInput()
                return self.camelotMessage

'''from GlobalVariables import Variables
V = Variables()
AR = Activities_Ruins(V)
AR.SC_Start()
AR.UC_Select_Task()'''