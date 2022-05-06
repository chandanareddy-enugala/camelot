from Messages import Message_
from Game_Initialize import Setup

class Activities_ForestPath_:
    def __init__(self, V):
        self.V = V
        setup = Setup(V)
        setup.Create()

        self.Status_TaskCompletion = ""
        self.Potion = ""
        self.camelotMessage = ""

        self.Angel_Talk_Limit = 3
        self.Angel_Attack_Limit = 2
        self.Well_BluePotion_Limit = 1
        self.Well_RedPotion_Limit = 1

        # ================================================================================= PLACES : DEFINING & CREATING
        self.Place_ForestPath = V.Place_ForestPath
        # ================================================================================= CHARACTERS : DEFINING & CREATING
        self.Char_Bob = V.Char_Bob
        self.Char_Angel = V.Char_Angel
        # ================================================================================= ITEMS: DEFINING & CREATING
        self.Item_BluePotion = V.Item_BluePotion
        self.Item_RedPotion = V.Item_RedPotion
        self.Item_CloseScroll = V.Item_CloseScroll
        self.Item_PurpleBook = V.Item_PurpleBook        # Instructions

        self.V.Set.Position(self.Item_CloseScroll.Name, self.Char_Angel.Name)  # Angel gives scroll to bob

        # ================================================================================= SOUND EFFECTS : DEFINING (only)
        self.SEffect_DarkMagic = self.V.SEffect_DarkMagic
        self.SEffect_Ominous = self.V.SEffect_Ominous
        self.SEffect_Potion = self.V.SEffect_Potion
        self.SEffect_Spell2 = self.V.SEffect_Spell2
        self.SEffect_Error = self.V.SEffect_Error
        self.SEffect_Spooky = self.V.SEffect_Spooky

        # ================================================================================= ICONS : DEFINING & ENABLING
        self.Icon_Attack = V.Icon_Attack
        self.Icon_Talk = V.Icon_Talk
        self.Icon_BluePotion = V.Icon_BluePotion
        self.Icon_RedPotion = V.Icon_RedPotion
        self.Icon_Drink = V.Icon_Drink
        self.Icon_ExitPlace = V.Icon_ExitPlace
        self.Icon_Well = V.Icon_Well

        self.Icon_Attack.EnableIcon(self.Char_Angel.Name, False)
        self.Icon_Talk.EnableIcon(self.Char_Angel.Name, True)
        self.Icon_BluePotion.EnableIcon(self.Place_ForestPath.Well, False)
        self.Icon_RedPotion.EnableIcon(self.Place_ForestPath.Well, False)
        self.Icon_Well.EnableIcon(self.Place_ForestPath.Well, True)
        self.Icon_Drink.EnableIcon(self.Item_RedPotion.Name, False)
        self.Icon_Drink.EnableIcon(self.Item_BluePotion.Name, False)

        # Item_PurpleBook is used for Game Instructions by enabling Icon_OpenScroll.
        self.Icon_OpenScroll = V.Icon_OpenScroll
        self.Icon_OpenScroll.ActionName = "Select Game Instructions"
        self.Icon_OpenScroll.DisplayName = "Game Instructions"
        self.Icon_OpenScroll.EnableIcon(self.Item_PurpleBook.Name)
        self.V.Char_Bob_Inventory.Add(self.Item_PurpleBook.Name, "Game Instructions")

        # ================================================================================= VISUAL EFFECTS : DEFINING & CREATING
        self.V.VEffect_Aura.CreateEffect(self.Char_Angel.Name)
        # self.V.VEffect_Magic.CreateEffect(self.Char_Bob.Name)

# ====================================================================================================================== START LEVEL_01
    def SC_Start(self):
        self.V.Set.DisableInput()
        self.V.Display.FadeIn()
        self.SEffect_Spooky.Play()
        self.Char_Bob.Enter(self.Place_ForestPath.EastEnd)
        self.V.Set.CameraFocus(self.Char_Bob.Name)
        self.V.Set.CameraMode('follow')
        self.V.VEffect_Aura.EnableEffect()
        self.Char_Angel.Enter(self.Place_ForestPath.WestEnd, False)

        N_FP01_Bob = self.V.N_FP01_Bob
        camelotMessage = N_FP01_Bob.ShowNarration()

        self.SEffect_Spooky.Stop()
        self.V.Set.EnableInput()
        return

    def UC_Select_Task(self):
        self.V.Set.EnableInput()
        self.V.SEffect_Ominous.Play()
        while True:
            self.camelotMessage = input()
            # -------------------------- Task01 - Bob - Talk1 - Angel --------------------------
            if ("Talk" in self.camelotMessage) & (f"{self.Char_Angel.Name}" in self.camelotMessage):
                if self.Angel_Talk_Limit == 3:
                    self.V.SEffect_Ominous.Stop()
                    self.SC_Task01_Bob_Angel_Talk()
                    self.V.SEffect_Ominous.Play()
                    self.Angel_Talk_Limit -= 1
                # -------------------------- Task04 - Bob - Talk2 - Angel --------------------------
                elif self.Angel_Talk_Limit == 2:
                    self.V.SEffect_Ominous.Stop()
                    self.SC_Task04_Bob_Angel_Talk()
                    self.V.SEffect_Ominous.Play()
                    self.Angel_Talk_Limit -= 1
                # -------------------------- Task06 - Bob - Talk3 - Angel --------------------------
                elif self.Angel_Talk_Limit == 1:
                    self.V.SEffect_Ominous.Stop()
                    self.SC_Task06_Bob_Angel_Talk()
                    self.V.SEffect_Ominous.Play()
                    self.Angel_Talk_Limit -= 1
                else:
                    self.SEffect_Error.Play()
            # -------------------------- Task02 - Bob - Attack - Angel --------------------------
            elif ("Attack" in self.camelotMessage) & (f"{self.Char_Angel.Name}" in self.camelotMessage):
                status = ""
                self.V.SEffect_Ominous.Stop()
                if self.Angel_Attack_Limit > 0:
                    status = self.SC_Task02_Bob_Angel_Attack()
                    self.V.SEffect_Ominous.Play()
                else:
                    self.SEffect_Error.Play()
                if status == "RESTART":
                    self.SC_Start()
                else:
                    self.V.Display.Menu_Quit()
                    return "QUIT"
            elif ("Icon Well" in self.camelotMessage) and (self.Place_ForestPath.Well in self.camelotMessage):
                self.V.Set.DisableInput()
                self.Char_Bob.WalkTo(self.Place_ForestPath.Well)
                self.V.Set.EnableInput()
            # -------------------------- Task03 - Bob - Select - Potion - Well --------------------------
            elif (("BluePotion" in self.camelotMessage) or ("RedPotion" in self.camelotMessage)) and (self.Place_ForestPath.Well in self.camelotMessage):
                self.V.SEffect_Ominous.Stop()
                self.SC_Task03_Select_Potion_At_Well()
                self.V.SEffect_Ominous.Play()

            # -------------------------- Task07 - Bob - Exit - FP --------------------------
            elif (self.camelotMessage == "input exited Bob position FP.EastEnd") or ("ExitPlace" in self.camelotMessage):
                self.V.SEffect_Ominous.Stop()
                self.SC_Task07_Bob_Exit_Place()
                if "Task06" in self.Status_TaskCompletion:
                    return
            # -------------------------- Bob - Hints --------------------------
            elif "Interact" in self.camelotMessage:
                    self.FP_Hints()
            # -------------------------- Bob - Inventory --------------------------
            elif "Inventory" in self.camelotMessage:
                self.Activities_Bob_Inventory()
            # -------------------------- Pause | Resume --------------------------
            elif self.camelotMessage == "input Key Pause":
                self.V.Display.Menu_Show()

# ====================================================================================================================== TASK01 - ANGEL_TALK
    def SC_Task01_Bob_Angel_Talk(self):
        self.V.Set.DisableInput()
        self.V.SEffect_Serenade.Play()
        self.Char_Bob.WalkTo(self.Char_Angel.Name)

        D_FP01_Bob_Angel = self.V.D_FP01_Bob_Angel_English
        camelotMessage = D_FP01_Bob_Angel.ShowDialogs(self.Char_Bob.Name, self.Char_Angel.Name)

        self.V.SEffect_Serenade.Stop()
        self.Status_TaskCompletion = "Task01 --> "
        self.Icon_Talk.DisableIcon(self.Char_Angel.Name)
        self.Icon_Attack.DisableIcon(self.Char_Angel.Name)
        self.V.Set.EnableInput()

# ====================================================================================================================== TASK02 - ANGEL_ATTACK
    def SC_Task02_Bob_Angel_Attack(self):
        if self.Angel_Attack_Limit > 0:
            self.V.Set.DisableInput()
            self.V.SEffect_Danger2.Play()
            self.Char_Bob.Attack(self.Char_Angel.Name)
            self.V.Set.CameraBlend(2)
            self.V.Set.CameraMode('track')
            self.Char_Angel.Cast(self.Char_Bob.Name)
            self.Char_Bob.Die()
            self.V.SEffect_Danger2.Stop()
            self.Angel_Attack_Limit -= 1

            D_FP00_Bob_Die = self.V.D_FP00_Bob_Die_English              # Dialogs
            camelotMessage = D_FP00_Bob_Die.ShowDialogs()

            if "RESTART" in camelotMessage:
                self.Status_TaskCompletion = ""
                self.V.Set.EnableInput()
                return "RESTART"
            else:
                self.Status_TaskCompletion += " Task02 --> "
                return "QUIT"
        else:
            self.SEffect_Error.Play()
            return "LIMIT EXCEEDED"

# ====================================================================================================================== TASK02 - WELL_BLUEPOTION
    def SC_Task03_Select_Potion_At_Well(self):
        self.V.Set.DisableInput()
        if ("Task01" in self.Status_TaskCompletion) and ("Task03" not in self.Status_TaskCompletion):
            self.Char_Bob.WalkTo(self.Place_ForestPath.Well)
            if "BluePotion" in self.camelotMessage:
                self.Potion = self.Item_BluePotion.Name
                self.V.Char_Bob_Inventory.Add(self.Potion, "SecretSpell")
            else:
                self.Potion = self.Item_RedPotion.Name
                self.V.Char_Bob_Inventory.Add(self.Potion, "SecrectScroll")

            self.SEffect_Potion.Play()
            self.V.Set.Position(self.Potion, self.Char_Bob.Name)
            self.Char_Bob.Pocket(self.Potion)
            self.Icon_Talk.EnableIcon(self.Char_Angel.Name)
            self.Status_TaskCompletion += " Task03 --> "
        else:
            self.SEffect_Error.Play()
        self.V.Set.EnableInput()

    def SC_Task04_Bob_Angel_Talk(self):
        self.V.Set.DisableInput()
        self.Char_Bob.WalkTo(self.Char_Angel.Name)
        self.V.D_FP02_Bob_Angel_English.ShowDialogs(self.Char_Bob.Name, self.Char_Angel.Name)
        self.Icon_Talk.DisableIcon(self.Char_Angel.Name)
        self.Status_TaskCompletion += " Task04 --> "
        self.V.Set.EnableInput()

    def SC_Task05_Bob_Drink_Potion(self):
        self.V.Set.DisableInput()
        if "Task04" in self.Status_TaskCompletion:
            self.V.Set.CameraMode("focus")
            self.Char_Bob.Unpocket(self.Potion)
            self.Char_Bob.Drink()
            if self.Potion == "RedPotion":
                self.Char_Bob.Expression("surprised")
                self.V.Set.Wait(2)
            else:
                self.Char_Bob.Expression("sad")
                self.V.Set.Wait(1)
            self.Char_Bob.Expression("neutral")
            self.Char_Bob.PutDown(self.Potion)
            self.V.Set.Wait(1)
            self.V.Set.CameraMode("follow")
            self.V.Char_Bob_Inventory.Remove(self.Potion)
            self.Icon_Drink.DisableIcon(self.Item_BluePotion.Name)
            self.Icon_Drink.DisableIcon(self.Item_RedPotion.Name)
            self.Icon_Talk.EnableIcon(self.Char_Angel.Name)
            self.Status_TaskCompletion += " Task05 --> "
        self.V.Set.EnableInput()

    def SC_Task06_Bob_Angel_Talk(self):
        self.V.Set.DisableInput()
        self.Char_Bob.WalkTo(self.Char_Angel.Name)
        if self.Potion == "BluePotion":
            self.D_FP03_Bob_Angel_BluePotion = self.V.D_FP03_Bob_Angel_BluePotion
            cameloMessage = self.D_FP03_Bob_Angel_BluePotion.ShowDialogs(self.Char_Bob.Name, self.Char_Angel.Name)
            self.SEffect_Spell2.Play()
            self.V.SecretSpell_Angel = "OmBhimBhush"
        else:
            self.D_FP03_Bob_Angel_RedPotion_English = self.V.D_FP03_Bob_Angel_RedPotion_English
            self.D_FP03_Bob_Angel_RedPotion_English.ShowDialogs(self.Char_Bob.Name, self.Char_Angel.Name)
            self.Char_Bob.Take(self.Item_CloseScroll.Name, self.Char_Angel.Name)
            self.Char_Bob.Pocket(self.Item_CloseScroll.Name)
            self.V.SEffect_Pocket.Play()
            self.V.Char_Bob_Inventory.Add(self.Item_CloseScroll.Name)

        self.Icon_Talk.DisableIcon(self.Char_Angel.Name)
        self.Icon_ExitPlace.EnableIcon(self.Char_Angel.Name)
        self.Status_TaskCompletion += " Task06 --> "
        self.V.Set.EnableInput()

    def SC_Task07_Bob_Exit_Place(self):
        if "Task06" in self.Status_TaskCompletion:
            self.Char_Bob.Face(self.Place_ForestPath.EastEnd)
            #self.Char_Bob.WalkTo(self.Place_ForestPath.EastEnd)
            self.Char_Bob.Exit(self.Place_ForestPath.EastEnd)
            self.V.Display.FadeOut()
            self.Icon_ExitPlace.DisableIcon(self.Char_Angel.Name)
            self.V.Bob_Drink_Potion = self.Potion
            self.Status_TaskCompletion += " Task07 --> "

    def FP_Hints(self):
        self.V.Set.DisableInput()
        if self.Status_TaskCompletion == "":
            Message = f"HINT : Talk to {self.Char_Angel.Name}"
            _ = Message_([Message], self.V.Action).ShowNarration()
        elif "Task06" in self.Status_TaskCompletion:
            Message = f"HINT : Exit the Place"
            _ = Message_([Message], self.V.Action).ShowNarration()
        elif "Task05" in self.Status_TaskCompletion:
            Message = f"HINT : Talk to {self.Char_Angel.Name}"
            _ = Message_([Message], self.V.Action).ShowNarration()
        elif "Task04" in self.Status_TaskCompletion:
            Message = f"HINT : Drink Potion"
            _ = Message_([Message], self.V.Action).ShowNarration()
        elif "Task03" in self.Status_TaskCompletion:
            Message = f"HINT : Talk to {self.Char_Angel.Name}"
            _ = Message_([Message], self.V.Action).ShowNarration()
        elif "Task01" in self.Status_TaskCompletion:
            Message = f"HINT : Select one of the Potion at Well"
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
            # -------------------------- Task05 - Bob - Drink - Potion --------------------------
            elif (("BluePotion" in self.camelotMessage) or ("RedPotion" in self.camelotMessage)) and ("Icon Drink" in self.camelotMessage):
                self.V.Char_Bob_Inventory.Hide()
                self.SC_Task05_Bob_Drink_Potion()
                self.V.Set.EnableInput()
                break
            elif "Game Instructions" in self.camelotMessage:
                self.V.Char_Bob_Inventory.Hide()
                self.V.D_GameInstructions.ShowDialogs(self.Char_Bob.Name)
                self.V.Set.EnableInput()
                self.V.Char_Bob_Inventory.Show()

'''
from GlobalVariables import Variables
V = Variables()
AFP = Activities_ForestPath_(V)
AFP.SC_Start()
AFP.UC_Select_Task()'''