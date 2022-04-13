from Messages import Message_

class Activities_ForestPath_:
    def __init__(self, V):
        self.V = V
        self.Status_AFP = ""
        self.Angel_Talk_Limit = 2
        self.Angel_Attack_Limit = 3
        self.Well_BluePotion_Limit = 1
        self.Well_RedPotion_Limit = 1

        # ================================================================================= PLACES : DEFINING & CREATING
        self.Place_ForestPath = V.Place_ForestPath
        TF = self.Place_ForestPath.CreatePlace()
        if TF!=True:
            self.V.Display.Menu_Quit()
        # ================================================================================= CHARACTERS : DEFINING & CREATING
        self.Char_Bob = V.Char_Bob
        TF = self.Char_Bob.CreateCharacter()
        if TF != True:
            self.V.Display.Menu_Quit()

        self.Char_Angel = V.Char_Angel
        TF = self.Char_Angel.CreateCharacter()
        if TF != True:
            self.V.Display.Menu_Quit()

        # ================================================================================= ITEMS: DEFINING & CREATING
        self.Item_BluePotion = V.Item_BluePotion
        self.Item_BluePotion.CreateItem()

        self.Item_RedPotion = V.Item_RedPotion
        self.Item_RedPotion.CreateItem()

        self.Item_CloseScroll = V.Item_CloseScroll
        self.Item_CloseScroll.CreateItem()

        # ================================================================================= VISUAL EFFECTS : DEFINING & CREATING

        # ================================================================================= SOUND EFFECTS : DEFINING (only)
        self.SEffect_DarkMagic = self.V.SEffect_DarkMagic
        self.SEffect_Ominous = self.V.SEffect_Ominous
        self.SEffect_Potion = self.V.SEffect_Potion
        self.SEffect_Spell2 = self.V.SEffect_Spell2
        self.SEffect_Error = self.V.SEffect_Error
        self.SEffect_Spooky = self.V.SEffect_Spooky

        # ================================================================================= ICONS : DEFINING & ENABLING
        self.Icon_Talk = V.Icon_Talk
        TF = self.Icon_Talk.EnableIcon(self.Char_Angel.Name, True)
        self.Icon_Attack = V.Icon_Attack
        TF = self.Icon_Attack.EnableIcon(self.Char_Angel.Name, False)
        self.Icon_BluePotion = V.Icon_BluePotion
        TF = self.Icon_BluePotion.EnableIcon(self.Place_ForestPath.Well, False)
        self.Icon_RedPotion = V.Icon_RedPotion
        TF = self.Icon_RedPotion.EnableIcon(self.Place_ForestPath.Well, False)
        self.Icon_Star = V.Icon_Star
        TF = self.Icon_Star.EnableIcon(self.Place_ForestPath.Well, True)

        # ================================================================================= CAMERA SETTINGS
        TF = self.V.Set.CameraFocus(self.Place_ForestPath.EastEnd)
        TF = self.V.Set.CameraMode('track')
        TF = self.V.Set.CameraBlend(4)

        TF = self.V.Display.FadeOut()
        V.Set.Wait(5)
        TF = self.V.Display.Menu_Title_Set(self.V.Menu_Title)
        TF = self.V.Display.Menu_Show()
        self.Status_AFP = "ForestPath Setup "

# ====================================================================================================================== TASK00 - START LEVEL_01
    def SC_AFP_Start(self):
        TF = self.V.Set.DisableInput()
        TF = self.V.Display.FadeIn()
        TF = self.SEffect_Spooky.Play()
        TF = self.Char_Bob.Enter(self.Place_ForestPath.EastEnd)
        TF = self.V.Set.CameraFocus(self.Char_Bob.Name)
        TF = self.V.Set.CameraMode('follow')
        TF = self.Char_Bob.Face(self.Place_ForestPath.Plant)
        TF = self.V.Set.CameraBlend(4)
        TF = self.V.Set.Wait(1)
        TF = self.Char_Bob.Face(self.Place_ForestPath.Well)
        TF = self.V.Set.CameraBlend(4)
        TF = self.V.Set.Wait(1)
        TF = self.Char_Bob.Face(self.Place_ForestPath.EastEnd)
        TF = self.V.Set.CameraBlend(4)
        TF = self.Char_Angel.Enter(self.Place_ForestPath.WestEnd, False)
        TF = self.Char_Bob.Face(self.Place_ForestPath.WestEnd)
        TF = self.V.Set.Wait(1)
        N_FP01_Bob = self.V.N_FP01_Bob
        camelotMessage = N_FP01_Bob.ShowNarration()

        self.SEffect_Spooky.Stop()
        TF = self.V.Set.EnableInput()
        self.Status_AFP += " --> Player Entered ForestPath "

        return self.Status_AFP

    def UC_Task00_Select_Task(self):
        TF = self.V.Set.EnableInput()
        TF = self.V.SEffect_Ominous.Play()
        while True:
            camelotMessage = input()
            # ------------------------------------------------------------------------------ PLAYER TASK Bob Talks Angel
            if "Talk" in camelotMessage:
                TF = self.V.SEffect_Ominous.Stop()
                if self.Angel_Talk_Limit > 0:
                    TF = self.SC_Task01_Angel_Talk()
                else:
                    TF = self.SEffect_Error.Play()
            # ------------------------------------------------------------------------------ PLAYER TASK: Bob Attacks Angel
            elif "Attack" in camelotMessage:
                status = ""
                TF = self.V.SEffect_Ominous.Stop()
                if self.Angel_Attack_Limit > 0:
                    status = self.SC_Task02_Angel_Attack()
                else:
                    TF = self.SEffect_Error.Play()
                if status == "RESTART":
                    self.Status_AFP = "ForestPath Setup "
                    self.Angel_Talk_Limit = 2
                    self.Angel_Attack_Limit = 3
                    self.Well_BluePotion_Limit = 1
                    self.Well_RedPotion_Limit = 1

                    self.SC_AFP_Start()
                else:
                    self.V.Display.Menu_Quit()
                    return "QUIT"
            # ------------------------------------------------------------------------------ PLAYER TASK: Bob Uses LeftMouseClick
            elif "Icon Star" in camelotMessage:
                _ = Message_(["Select one of Blue or Red Potions Carefully"], self.V.Action).ShowNarration()
                TF = self.SEffect_Error.Play()
            # ------------------------------------------------------------------------------ PLAYER TASK: Bob Choose BluePotion
            elif "BluePotion" in camelotMessage:
                if (self.Angel_Talk_Limit < 2) & (self.Well_BluePotion_Limit > 0):
                    TF = self.V.SEffect_Ominous.Stop()
                    TF = self.SC_Task03_Well_BluePotion()
                    if TF == True:
                        self.Status_AFP = "--> BluePotion " + f" --> Spell:{self.V.SecretSpell_Angel}"
                        return self.Status_AFP
                else:
                    TF = self.SEffect_Error.Play()
                    _ = Message_(["Talk with Angel"], self.V.Action).ShowNarration()
            # ------------------------------------------------------------------------------ PLAYER TASK: Bob Choose BluePotion
            elif "RedPotion" in camelotMessage:
                if (self.Angel_Talk_Limit < 2) & (self.Well_RedPotion_Limit > 0):
                    TF = self.V.SEffect_Ominous.Stop()
                    TF = self.SC_Task04_Well_RedPotion()
                    if TF == True:
                        self.Status_AFP = " --> RedPotion "
                        return self.Status_AFP
                else:
                    TF = self.SEffect_Error.Play()
                    _ = Message_(["Talk with Angel"], self.V.Action).ShowNarration()
            elif camelotMessage == "input Selected Start":
                TF = self.V.Display.Menu_Start()
            elif camelotMessage == "input Selected Credits":
                TF = self.V.Display.Menu_Show_Credits()
            elif camelotMessage == "input Selected Quit":
                TF = self.V.Display.Menu_Quit()
            elif camelotMessage == "input Selected Resume":
                TF = self.V.Display.Menu_Show_Resume()
            elif camelotMessage == "input Close Credits":
                TF = self.V.Display.Menu_Hide_Credits()
            elif camelotMessage == "input Key Pause":
                if self.V.EscapeCount == 0:
                    # Show the Player list
                    self.V.EscapeCount += 1

                elif self.V.EscapeCount == 1:
                    TF = self.V.Display.Menu_Show_Resume()
                    self.V.EscapeCount += 1
                elif self.V.EscapeCount == 2:
                    TF = self.V.Display.Menu_Hide_Resume()
                    self.V.EscapeCount += 1
                elif self.V.EscapeCount == 3:
                    # Hide the Player list
                    self.V.EscapeCount = 0
                    pass

# ====================================================================================================================== TASK01 - ANGEL_TALK
    def SC_Task01_Angel_Talk(self):
        TF = self.V.Set.DisableInput()
        TF = self.V.SEffect_Serenade.Play()

        if self.Angel_Talk_Limit==2:
            TF = self.Char_Bob.WalkTo(self.Char_Angel.Name)
            TF = self.Char_Bob.Face(self.Char_Angel.Name)
            D_FP01_Bob_Angel = self.V.D_FP01_Bob_Angel
            camelotMessage = D_FP01_Bob_Angel.ShowDialogs(self.Char_Bob.Name, self.Char_Angel.Name)
            self.Angel_Talk_Limit -= 1
            TF = self.V.SEffect_Serenade.Stop()
            return True

        elif self.Angel_Talk_Limit == 1:
            TF = self.Char_Bob.WalkTo(self.Char_Angel.Name)
            TF = self.Char_Bob.Face(self.Char_Angel.Name)
            D_FP02_Bob_Angel = self.V.D_FP02_Bob_Angel
            camelotMessage = D_FP02_Bob_Angel.ShowDialogs(self.Char_Bob.Name, self.Char_Angel.Name)
            TF = self.V.SEffect_Serenade.Stop()
            self.Angel_Talk_Limit -= 1
            return True
        TF = self.V.Set.EnableInput()



# ====================================================================================================================== TASK02 - ANGEL_ATTACK
    def SC_Task02_Angel_Attack(self):
        if self.Angel_Attack_Limit > 0:
            TF = self.V.Set.DisableInput()
            self.Angel_Attack_Limit -= 1

            TF = self.V.SEffect_Danger2.Play()

            TF = self.Char_Bob.Attack(self.Char_Angel.Name)
            TF = self.V.Set.CameraBlend(2)
            TF = self.V.Set.CameraMode('track')
            TF = self.Char_Angel.Cast(self.Char_Bob.Name)
            self.Char_Bob.Die()

            TF = self.V.SEffect_Danger2.Stop()

            D_FP00_Bob_Die = self.V.D_FP00_Bob_Die              # Dialogs
            camelotMessage = D_FP00_Bob_Die.ShowDialogs()

            if "RESTART" in camelotMessage:
                TF = self.V.Set.EnableInput()
                return "RESTART"
            else:
                return "QUIT"
        else:
            TF = self.SEffect_Error.Play()
            return "LIMIT EXCEEDED"

# ====================================================================================================================== TASK02 - WELL_BLUEPOTION
    def SC_Task03_Well_BluePotion(self):
        self.V.Set.DisableInput()
        TF = self.V.SEffect_Serenade.Play()
        self.Char_Bob.Face(self.Char_Angel.Name)
        self.Char_Bob.WalkTo(self.Place_ForestPath.Well)
        self.SEffect_Potion.Play()
        self.V.Set.Position(self.Item_BluePotion.Name, self.Char_Bob.Name)
        self.Char_Bob.WalkTo(self.Char_Angel.Name)
        self.Char_Bob.Face(self.Char_Angel.Name)
        self.V.Set.CameraMode(2)
        self.V.Set.CameraMode('focus')
        self.V.Set.Wait(1)
        self.Char_Bob.Drink()
        self.Char_Bob.SetExpression("surprised")
        self.V.Set.Wait(1)
        D_FP02_Bob_Angel_BluePotion = self.V.D_FP02_Bob_Angel_BluePotion
        camelotMessage = D_FP02_Bob_Angel_BluePotion.ShowDialogs(self.Char_Bob.Name, self.Char_Angel.Name)

        self.SEffect_Spell2.Play()
        self.V.SecretSpell_Angel = "OmBhimBhush"
        self.V.Set.CameraMode('follow')
        self.Char_Angel.Exit(self.Place_ForestPath.EastEnd, False)
        self.Char_Bob.Face(self.Char_Angel.Name)
        self.Char_Bob.Exit(self.Place_ForestPath.WestEnd)
        self.V.Display.FadeOut()
        TF = self.V.SEffect_Serenade.Stop()
        self.V.Set.EnableInput()
        return True

# ====================================================================================================================== TASK02 - WELL_REDPOTION
    def SC_Task04_Well_RedPotion(self):
        self.V.Set.DisableInput()
        TF = self.V.SEffect_Serenade.Play()
        self.Char_Bob.Face(self.Char_Angel.Name)
        self.Char_Bob.WalkTo(self.Place_ForestPath.Well)
        self.SEffect_Potion.Play()
        self.V.Set.Position(self.Item_RedPotion.Name, self.Char_Bob.Name)
        self.Char_Bob.Face(self.Char_Angel.Name)
        self.Char_Bob.WalkTo(self.Place_ForestPath.WestEnd)
        self.Char_Bob.Face(self.Char_Angel.Name)
        self.Char_Bob.WalkTo(self.Char_Angel.Name)
        self.Char_Angel.Face(self.Char_Bob.Name)
        self.V.Set.CameraMode('focus')
        self.V.Set.Wait(1)
        self.Char_Bob.Drink()
        self.Char_Bob.SetExpression("happy")
        self.V.Set.Wait(1)

        D_FP03_Bob_RedPotion = self.V.D_FP03_Bob_Angel_RedPotion
        camelotMessage = D_FP03_Bob_RedPotion.ShowDialogs(self.Char_Bob.Name, self.Char_Angel.Name)

        self.V.SecretSpell_Angel = ""
        self.V.Set.CameraMode('track')
        self.V.Set.Position(self.Item_CloseScroll.Name, self.Char_Angel.Name)  # Angel gives scroll to bob
        self.SEffect_Spell2.Play()
        #self.Char_Angel.Give(self.Item_CloseScroll.Name, self.Char_Bob.Name)
        self.Char_Bob.Take(self.Item_CloseScroll.Name, self.Char_Angel.Name)
        self.V.SEffect_Pocket.Play()
        self.Char_Bob.Pocket(self.Item_CloseScroll.Name)
        self.Char_Angel.Exit(self.Place_ForestPath.EastEnd, False)
        self.Char_Bob.Face(self.Char_Angel.Name)
        self.Char_Bob.Exit(self.Place_ForestPath.WestEnd, False)
        self.V.Display.FadeOut()
        TF = self.V.SEffect_Serenade.Stop()
        self.V.Set.EnableInput()
        return True

'''from GlobalVariables import Variables
V = Variables()
AFP = Activities_ForestPath_(V)
AFP.SC_Task01_Start()'''