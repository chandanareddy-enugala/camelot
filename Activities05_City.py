from Messages import Message_

class Activities_City_:
    def __init__(self, V):
        # ================================================================================= CLASS VARIABLES
        self.V = V
        self.Status_TaskCompletion = ""
        self.camelotMessage = ""

        # ================================================================================= PLACES : DEFINING & CREATING

        # ================================================================================= CHARACTERS : DEFINING & CREATING

        # ================================================================================= ITEMS: DEFINING & CREATING

        # ================================================================================= LISTS

        # ================================================================================= VISUAL EFFECTS : DEFINING & CREATING

        # ================================================================================= SOUND EFFECTS : DEFINING (only)

        # ================================================================================= Set Characters Positions
        self.V.Set.Position(self.V.Char_Emily_S.Name, self.V.Place_City.RedHouseDoor)
        self.V.Set.Position(self.V.Char_Tom_S.Name, self.V.Place_City.BlueHouseDoor)

        # ================================================================================= ICONS : DEFINING & ENABLING
        self.V.Icon_EvilBook.EnableIcon(self.V.Place_City.Fountain)
        self.V.Icon_Sword.EnableIcon(self.V.Place_City.Fountain)
        self.V.Icon_Talk.EnableIcon(self.V.Char_Emily_S.Name)
        self.V.Icon_Talk.EnableIcon(self.V.Char_Tom_S.Name)


    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # ===================================================  START  ==================================================
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    def SC_Start(self):
        self.V.Set.DisableInput()
        self.V.Set.CameraFocus(self.V.Place_City.NorthEnd)
        self.V.Set.CameraMode('track')
        self.V.Set.CameraBlend(3)
        self.V.Display.FadeIn()

        self.V.Char_Bob.Enter(self.V.Place_City.NorthEnd)
        self.V.Set.CameraFocus(self.V.Char_Bob.Name)
        self.V.Set.CameraMode('follow')
        self.V.Set.EnableInput()

    def UC_Select_Task(self):
        self.V.Set.EnableInput()
        self.V.SEffect_Ominous.Play()
        while True:
            self.camelotMessage = input()
            # -------------------------- Bob - Emily - Talk --------------------------
            if ("Icon Talk" in self.camelotMessage) and (self.V.Char_Emily_S.Name in self.camelotMessage):
                self.SC_Task01_Bob_Emily_Talk()

            # -------------------------- Bob - Fountain - Select Task - Sword --------------------------
            elif ("Icon Sword" in self.camelotMessage) and (self.V.Place_City.Fountain in self.camelotMessage):
                self.SC_Task02_Bob_Fountain_Sword()
            # -------------------------- Bob - Sword Task - Tom - Talk --------------------------
            elif ("Icon Talk" in self.camelotMessage) and (self.V.Char_Tom_S.Name in self.camelotMessage):
                self.SC_Task02_1_Bob_Tom_Talk()
            # -------------------------- Bob - Sword Task - Tom - Attack --------------------------
            elif ("Icon Attack" in self.camelotMessage) and (self.V.Char_Tom_S.Name in self.camelotMessage):
                self.SC_Task02_2_Bob_Tom_Attack()
            # -------------------------- Bob - Sword Task - Unlock - BlueHouseDoor --------------------------
            elif ("Icon Unlock" in self.camelotMessage) and (self.V.Place_City.BlueHouseDoor in self.camelotMessage):
                self.SC_Task02_3_Bob_Enter_Dungeon()
            # -------------------------- Bob - Sword Task - Unlock - CellDoor --------------------------
            elif ("Icon Unlock" in self.camelotMessage) and (self.V.Place_Dungeon.CellDoor in self.camelotMessage):
                self.SC_Task02_4_Bob_Unlock_Lock_CellDoor()
            # -------------------------- Bob - Sword Task - Priest - Talk --------------------------
            elif ("Icon Talk" in self.camelotMessage) and (self.V.Char_Priest.Name in self.camelotMessage):
                if "Task02" in self.Status_TaskCompletion:
                    self.SC_Task02_5_Bob_Priest_Talk()
            # -------------------------- Bob - Sword Task - Exit - City - Ruins --------------------------
            elif ("Icon City" in self.camelotMessage) and (self.V.Place_Dungeon.Door in self.camelotMessage):
                self.SC_Task02_6_Bob_Exit_to_Ruins()
                return

            # -------------------------- Bob - Fountain - Select Task - EvilBook --------------------------
            elif ("Icon EvilBook" in self.camelotMessage) and (self.V.Place_City.Fountain in self.camelotMessage):
                print(self.Status_TaskCompletion)
                self.SC_Task03_Bob_Fountain_EvilBook()
            # -------------------------- Bob - EvilBook Task - Enter - Farm --------------------------
            elif ("Icon Farm" in self.camelotMessage) and (self.V.Place_City.Fountain in self.camelotMessage):
                print(self.Status_TaskCompletion)
                self.SC_Task03_1_Bob_Exit_Enter_Farm()
            # -------------------------- Bob - EvilBook Task - Tom - Attack --------------------------
            elif ("Icon Talk" in self.camelotMessage) and (self.V.Char_Priest.Name in self.camelotMessage):
                print(self.Status_TaskCompletion)
                if "Task03" in self.Status_TaskCompletion:
                    self.SC_Task03_2_Bob_Priest_Talk()
            # -------------------------- Bob - EvilBook Task - Exit - City - Ruins --------------------------
            elif ("Icon City" in self.camelotMessage) and (self.V.Char_Priest.Name in self.camelotMessage):
                self.SC_Task03_3_Bob_Exit_to_Ruins()
                return


            # -------------------------- Bob - Hints --------------------------
            elif "Interact" in self.camelotMessage:
                print(self.Status_TaskCompletion)
                self.City_Hints()
            # -------------------------- Bob - Inventory --------------------------
            elif "Inventory" in self.camelotMessage: # input Key Inventory
                self.Activities_Bob_Inventory()
            # -------------------------- Pause | Resume --------------------------
            elif self.camelotMessage == "input Key Pause":
                self.V.Display.Menu_Show()

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    def SC_Task01_Bob_Emily_Talk(self): #
        self.V.Set.DisableInput()
        self.V.Char_Bob.WalkTo(self.V.Char_Emily_S.Name)
        _ = self.V.D_City_Bob_Emily_Talk.ShowDialogs(self.V.Char_Bob.Name, self.V.Char_Emily_S.Name)
        self.V.Icon_Talk.DisableIcon(self.V.Char_Emily_S.Name)
        self.Status_TaskCompletion = "Task01 --> "
        self.V.Set.EnableInput()
        return

    def SC_Task02_Bob_Fountain_Sword(self):
        self.V.Set.DisableInput()
        if "Task03" not in self.Status_TaskCompletion:
            _ = self.V.D_City_Bob_Fountain_Sword.ShowNarration()
            self.V.Char_Bob_Inventory.Add(self.V.Item_BobSword.Name)
            self.V.Icon_Sword.DisableIcon(self.V.Place_City.Fountain)
            self.V.Set.Position(self.V.Char_Priest.Name, self.V.Place_Dungeon.Bed)
            self.V.Icon_Talk.EnableIcon(self.V.Char_Tom_S.Name)
            self.V.Icon_Attack.EnableIcon(self.V.Char_Tom_S.Name)
            self.Status_TaskCompletion += "Task02 --> "
        else:
            _ = Message_(["You have already chosen a task to complete."], self.V.Action).ShowNarration()
        self.V.Set.EnableInput()
        return
    def SC_Task02_1_Bob_Tom_Talk(self):
        self.V.Set.DisableInput()
        _ = self.V.D_City_Bob_Tom_Talk.ShowDialogs(self.V.Char_Bob.Name, self.V.Char_Tom_S.Name)
        self.Status_TaskCompletion += "Task02_1 --> "
        self.V.Set.EnableInput()
        return
    def SC_Task02_2_Bob_Tom_Attack(self):
        self.V.Set.DisableInput()
        self.V.Char_Bob.Attack(self.V.Char_Tom_S.Name)
        self.V.Char_Tom_S.Attack(self.V.Char_Bob.Name)
        self.V.Char_Bob.Hold_Item_RightHand(self.V.Item_BobSword.Name)
        self.V.Char_Bob.Attack(self.V.Char_Tom_S.Name)
        self.V.Char_Tom_S.Die()
        self.V.Char_Bob.Pocket(self.V.Item_BobSword.Name)
        self.V.Icon_Unlock.EnableIcon(self.V.Place_City.BlueHouseDoor)
        self.V.Icon_Unlock.EnableIcon(self.V.Place_Dungeon.CellDoor)
        self.Status_TaskCompletion += "Task02_2 --> "
        self.V.Set.EnableInput()

    def SC_Task02_3_Bob_Enter_Dungeon(self):
        self.V.Set.DisableInput()
        self.V.Char_Bob.Exit(self.V.Place_City.BlueHouseDoor)
        self.V.Display.FadeOut()
        # self.V.Set.CameraFocus(self.V.Place_Dungeon.Door)
        self.V.Display.FadeIn()
        self.V.Char_Bob.Enter(self.V.Place_Dungeon.Door)
        if "Task02_3" not in self.Status_TaskCompletion:
            self.Status_TaskCompletion += "Task02_3 --> "
        self.V.Set.EnableInput()
        return
    def SC_Task02_4_Bob_Unlock_Lock_CellDoor(self):
        self.V.Set.DisableInput()
        self.V.Char_Bob.WalkTo(self.V.Place_Dungeon.CellDoor)
        self.V.Char_Bob.OpenFurniture(self.V.Place_Dungeon.CellDoor)
        #self.V.Icon_Unlock.DisableIcon(self.V.Place_Dungeon.CellDoor)
        self.V.Icon_Talk.EnableIcon(self.V.Char_Priest.Name)
        self.Status_TaskCompletion += "Task02_4 --> "
        self.V.Set.EnableInput()
        return
    def SC_Task02_5_Bob_Priest_Talk(self):
        self.V.Set.DisableInput()
        _ = self.V.D_City_SwordTask_Bob_Priest_Talk.ShowDialogs(self.V.Char_Bob.Name, self.V.Char_Priest.Name)
        self.V.Icon_Talk.DisableIcon(self.V.Char_Priest.Name)
        self.V.Icon_City.EnableIcon(self.V.Place_Dungeon.Door)
        self.V.Set.EnableInput()
        self.Status_TaskCompletion += "Task02_5 --> "
        return
    def SC_Task02_6_Bob_Exit_to_Ruins(self):
        self.V.Set.DisableInput()
        self.V.Char_Bob.Exit(self.V.Place_Dungeon.Door)
        self.V.Display.FadeOut()
        self.V.Display.FadeIn()
        self.V.Char_Bob.Enter(self.V.Place_City.BlueHouseDoor)
        self.V.Char_Bob.Exit(self.V.Place_City.WestEnd)
        self.V.Display.FadeOut()
        self.Status_TaskCompletion += "Task02_6 --> "
        return

# ----------------------------
    def SC_Task03_Bob_Fountain_EvilBook(self):
        self.V.Set.DisableInput()
        if "Task02" not in self.Status_TaskCompletion:
            _ = self.V.D_City_Bob_Fountain_EvilBook.ShowNarration()
            self.V.Set.Position(self.V.Char_Priest.Name, self.V.Place_Farm.Horse)

            self.V.Icon_EvilBook.DisableIcon(self.V.Place_City.Fountain)
            self.V.Icon_Farm.EnableIcon(self.V.Place_City.Fountain)

            self.Status_TaskCompletion += "Task03 --> "
        else:
            _ = Message_(["You have already chosen a task to complete."], self.V.Action).ShowNarration()
        self.V.Set.EnableInput()
        return

    def SC_Task03_1_Bob_Exit_Enter_Farm(self):
        self.V.Set.DisableInput()
        self.V.Char_Bob.Exit(self.V.Place_City.EastEnd)
        self.V.Display.FadeOut()

        self.V.Set.CameraFocus(self.V.Place_Farm.Exit)
        self.V.Set.CameraMode('track')
        self.V.Display.FadeIn()
        self.V.Char_Bob.Enter(self.V.Place_Farm.Exit)
        self.V.Set.CameraFocus(self.V.Char_Bob.Name)
        self.V.Set.CameraMode('follow')

        self.Status_TaskCompletion += "Task03_1 --> "
        self.V.Icon_Talk.EnableIcon(self.V.Char_Priest.Name)
        self.V.Set.EnableInput()
        return

    def SC_Task03_2_Bob_Priest_Talk(self):
        self.V.Set.DisableInput()
        _ = self.V.D_City_EvilBookTask_Bob_Priest_Talk.ShowDialogs(self.V.Char_Bob.Name, self.V.Char_Priest.Name)
        self.V.Icon_City.EnableIcon(self.V.Char_Priest.Name)
        self.Status_TaskCompletion += "Task03_2 --> "
        self.V.Set.EnableInput()
        return
    def SC_Task03_3_Bob_Exit_to_Ruins(self):
        self.V.Set.DisableInput()
        self.V.Char_Bob.Exit(self.V.Place_Farm.Exit)
        self.V.Set.Display.FadeOut()
        self.V.Set.Display.FadeIn()
        self.V.Char_Bob.Enter(self.V.Place_City.EastEnd)
        self.V.Char_Bob.Exit(self.V.Place_City.WestEnd)
        self.V.Display.FadeOut()
        self.Status_TaskCompletion += "Task03_3 --> "
        return

# ---------------------------------------------------

    def City_Hints(self):
        self.V.Set.DisableInput()
        if self.Status_TaskCompletion == "":
            Message = f"HINT : Ask People in City about Priest or Select Tasks at Fountain"
            _ = Message_([Message], self.V.Action).ShowNarration()

        elif "Task03" in self.Status_TaskCompletion:
            if "Task03_2" in self.Status_TaskCompletion:
                Message = f"HINT: Enter into City then Ruins"
                _ = Message_([Message], self.V.Action).ShowNarration()
            elif "Task03_1" in self.Status_TaskCompletion:
                Message = f"HINT: Talk to Priest"
                _ = Message_([Message], self.V.Action).ShowNarration()
            else:
                Message = f"HINT: Enter into Farm"
                _ = Message_([Message], self.V.Action).ShowNarration()

        elif "Task02" in self.Status_TaskCompletion:
            if "Task02_5" in self.Status_TaskCompletion:
                Message = f"HINT : Exit through Door and Enter into City then Ruins"
                _ = Message_([Message], self.V.Action).ShowNarration()
            elif "Task02_4" in self.Status_TaskCompletion:
                Message = f"HINT : Talk to Priest"
                _ = Message_([Message], self.V.Action).ShowNarration()
            elif "Task02_3" in self.Status_TaskCompletion:
                Message = f"HINT : Unlock CellDoor and Release Priest"
                _ = Message_([Message], self.V.Action).ShowNarration()
            elif "Task02_2" in self.Status_TaskCompletion:
                Message = f"HINT : Enter through BlueHouseDoor"
                _ = Message_([Message], self.V.Action).ShowNarration()
            elif ("Task02_1" in self.Status_TaskCompletion) and ("Task02_2" not in self.Status_TaskCompletion):
                Message = f"HINT : Kill Tom"
                _ = Message_([Message], self.V.Action).ShowNarration()
            else:
                Message = f"HINT : Talk to Tom or Kill Tom"
                _ = Message_([Message], self.V.Action).ShowNarration()

        elif "Task01" in self.Status_TaskCompletion:
            Message = f"HINT : Select one of the Tasks at Fountain"
            _ = Message_([Message], self.V.Action).ShowNarration()
        self.V.Set.EnableInput()

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

'''from GlobalVariables import Variables
V = Variables()
CBR = Activities_City_(V)
CBR.SC_Start()
CBR.UC_Select_Task()'''