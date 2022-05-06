from Messages import Message_

class Activities_CastleBedRoom_:
    def __init__(self, V):
        self.V = V
        self.Status_TaskCompletion = ""
        self.camelotMessage = ""

        # --------------------------- PLACES ---------------------------
        self.Place_CastleBedRoom = self.V.Place_CastleBedRoom
        # --------------------------- CHARACTERS ---------------------------
        self.Char_Bob = V.Char_Bob
        self.Char_Candy = V.Char_Candy
        self.Char_Lilly_S = V.Char_Lilly_S

        # # --------------------------- ITEMS ---------------------------
        self.Item_Coin = V.Item_Coin
        self.Item_BlueKey = V.Item_BlueKey
        self.Item_Compass = V.Item_Compass
        self.Item_Hammer = V.Item_Hammer
        self.Item_LitTorch = V.Item_LitTorch
        self.Item_PurpleBook = V.Item_PurpleBook  # Instructions

        # # --------------------------- ICONS ---------------------------
        self.Icon_BlueKey = V.Icon_BlueKey
        self.Icon_Talk = V.Icon_Talk
        self.Icon_Dress = V.Icon_Dress
        self.Icon_GiveMoney = V.Icon_GiveMoney
        self.Icon_TakeMoney = V.Icon_TakeMoney
        self.Icon_FirePlace = V.Icon_FirePlace
        self.Icon_Chest = V.Icon_Chest
        self.Icon_Unlock = V.Icon_Unlock
        self.Icon_Torch = V.Icon_Torch
        self.Icon_Take = V.Icon_Take
        self.Icon_City = V.Icon_City

        # # --------------------------- SOUND EFFECTS ---------------------------
        self.SEffect_Fireball = V.SEffect_Fireball
        self.SEffect_Pocket = V.SEffect_Pocket
        self.SEffect_Fireplace = V.SEffect_Fireplace
        self.SEffect_Dramatic = V.SEffect_Dramatic
        self.SEffect_DarkMagic = V.SEffect_DarkMagic
        self.SEffect_Ominous = V.SEffect_Ominous
        self.SEffect_Potion = V.SEffect_Potion
        self.SEffect_Spell2 = V.SEffect_Spell2
        self.SEffect_Error = V.SEffect_Error
        self.SEffect_Spooky = V.SEffect_Spooky

        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

        # --------------------------- VISUAL EFFECT ---------------------------
        self.VEffect_Campfire = self.V.VEffect_Campfire
        self.VEffect_Campfire.CreateEffect(self.Place_CastleBedRoom.Fireplace)

        # --------------------------- SET POSITION ---------------------------
        self.V.Set.Position(self.Char_Candy.Name, self.Place_CastleBedRoom.Bed)
        self.Char_Candy.Sleep(self.Place_CastleBedRoom.Bed)
        self.V.Set.Position(self.Char_Lilly_S.Name, self.Place_CastleBedRoom.SmallTable)
        self.Char_Lilly_S.Face(self.Char_Candy.Name)
        self.Char_Lilly_S.Kneel()

        # # --------------------------- INVENTORY ---------------------------
        self.Char_Bob_Inventory = V.Char_Bob_Inventory
        self.CBR_Item_Chest_Inventory = V.CBR_Item_Chest_Inventory
        #self.Char_Lilly_S_Inventory = V.Char_Lilly_S_Inventory
        #self.Char_Lilly_S_Inventory.Add(self.Item_BlueKey.Name, "To Open Chest")
        #self.Char_Lilly_S_Inventory.Add(self.Item_LitTorch.Name, "To Put Fire at Fireplace")
        self.CBR_Item_Chest_Inventory.Add(self.Item_Compass.Name, "To Show the Directions")
        self.CBR_Item_Chest_Inventory.Add(self.Item_Hammer.Name, "To Show the Directions")


        # --------------------------- ENABLE ICONS ---------------------------

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # ===================================================  START  ==================================================
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    def SC_Start(self):
        self.V.Set.DisableInput()
        self.V.Set.CameraFocus(self.Place_CastleBedRoom.Door)
        self.V.Set.CameraMode('track')
        self.V.Set.CameraBlend(3)
        self.V.Display.FadeIn()

        self.V.Char_Bob.Enter(self.Place_CastleBedRoom.Door)
        self.V.Set.CameraFocus(self.Char_Bob.Name)
        self.V.Set.CameraMode('follow')

        self.Icon_Talk.EnableIcon(self.Char_Candy.Name, False)
        self.Icon_FirePlace.EnableIcon(self.Item_LitTorch.Name, True)
        self.Icon_Chest.EnableIcon(self.Item_BlueKey.Name, True)
        self.Icon_GiveMoney.EnableIcon(self.Item_Coin.Name)
        self.Icon_Take.EnableIcon(self.Item_Compass.Name)
        self.Icon_Take.EnableIcon(self.Item_Hammer.Name)
        return

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # ================================================  USER CONTROL  ==============================================
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    def UC_Select_Task(self):
        TF = self.V.Set.EnableInput()
        TF = self.V.SEffect_Ominous.Play()
        while True:
            self.camelotMessage = input()
            # -------------------------- Lilly - Open - Door --------------------------
            if ("Unlock" in self.camelotMessage) and (self.Place_CastleBedRoom.Door in self.camelotMessage):
                self.SC_Task01_Lilly_Open_Door()
            # -------------------------- Bob - Talk - Candy --------------------------
            elif ("Talk" in self.camelotMessage) and (self.Char_Candy.Name in self.camelotMessage):
                self.SC_Task02_Bob_Candy_Talk()
            # -------------------------- Bob - Talk-Clap - Lilly --------------------------
            elif ("Talk" in self.camelotMessage) and (self.Char_Lilly_S.Name in self.camelotMessage):
                self.SC_Task03_Bob_Lilly_Talk1()
            # -------------------------- Bob - LiTourch - Lilly --------------------------
            elif ("Torch" in self.camelotMessage) and (self.Char_Lilly_S.Name in self.camelotMessage):
                self.SC_Task04_Bob_Lilly_LitTourch()
            # -------------------------- Bob - LiTourch - FirePlace --------------------------
            elif ("Torch" in self.camelotMessage) and (self.Place_CastleBedRoom.Fireplace in self.camelotMessage):
                self.SC_Task05_Bob_Fireplace_LitTourch()
            # -------------------------- Bob - Closet - Dress --------------------------
            elif ("Icon Dress" in self.camelotMessage) and (self.Place_CastleBedRoom.Closet in self.camelotMessage):
                self.SC_Task06_Bob_Closet_Dress()
            # -------------------------- Bob - Closet - Coin --------------------------
            elif ("Icon TakeMoney" in self.camelotMessage) and (self.Place_CastleBedRoom.Closet in self.camelotMessage):
                self.SC_Task07_Bob_Closet_Money()
            # -------------------------- Bob - Talk - Ask Key - Lilly --------------------------
            elif ("BlueKey" in self.camelotMessage) and (self.Char_Lilly_S.Name in self.camelotMessage):
                self.SC_Task08_Bob_Lilly_ChestKey()
            # -------------------------- Bob - Key - Chest - Open --------------------------
            elif ("Unlock" in self.camelotMessage) and (self.Place_CastleBedRoom.Chest in self.camelotMessage):
                self.SC_Task09_Bob_Chest_Open()
            # -------------------------- Bob - Key - Chest - Take Compass --------------------------
            elif ("Icon Take" in self.camelotMessage) and (self.Item_Compass.Name in self.camelotMessage):
                self.SC_Task10_Bob_Chest_Compass()
            # -------------------------- Bob - Key - Chest - Take Compass --------------------------
            elif ("Icon Take" in self.camelotMessage) and (self.Item_Hammer.Name in self.camelotMessage):
                self.SC_Task11_Bob_Chest_Hammer()
            # -------------------------- Bob - Door - Exit - City --------------------------
            elif ("Icon City" in self.camelotMessage) and (self.Place_CastleBedRoom.Door in self.camelotMessage):
                self.SC_Task12_Bob_Door_Exit()
                return
            # -------------------------- Bob - Hints -------------------------- E : input Key Interact
            elif "Interact" in self.camelotMessage:
                self.CBR_Hints()
            # -------------------------- Bob - Inventory -------------------------- I: input Key Inventory
            elif "Inventory" in self.camelotMessage:
                self.Activities_Bob_Inventory()
            # -------------------------- Pause | Resume -------------------------- Esc : input Key Pause
            elif self.camelotMessage == "input Key Pause":
                self.V.Display.Menu_Show()

    # -------------------------- Lilly - Open - Door --------------------------
    def SC_Task01_Lilly_Open_Door(self):
        self.V.Set.DisableInput()
        self.Char_Lilly_S.WalkTo(self.Place_CastleBedRoom.Door)
        self.Char_Lilly_S.OpenFurniture(self.Place_CastleBedRoom.Door)
        self.Char_Bob.Enter(self.Place_CastleBedRoom.Door)
        self.V.Set.CameraFocus(self.Char_Bob.Name)
        self.V.Set.CameraBlend(3)

        self.Icon_Talk.EnableIcon(self.Char_Candy.Name, False)
        self.Icon_FirePlace.EnableIcon(self.Item_LitTorch.Name, True)
        self.Icon_Chest.EnableIcon(self.Item_BlueKey.Name, True)
        self.Icon_GiveMoney.EnableIcon(self.Item_Coin.Name)
        self.Icon_Take.EnableIcon(self.Item_Compass.Name)
        self.Icon_Take.EnableIcon(self.Item_Hammer.Name)

        self.V.Set.CameraMode('follow')
        self.Status_TaskCompletion = "Task01 --> "
        self.V.Set.EnableInput()
        return

    def SC_Task02_Bob_Candy_Talk(self):
        self.V.Set.DisableInput()

        self.D_CBR01_Bob_Candy_Talk_1_English = self.V.D_CBR01_Bob_Candy_Talk_1_English
        camelotMessage = self.D_CBR01_Bob_Candy_Talk_1_English.ShowDialogs(self.Char_Bob.Name, self.Char_Candy.Name)

        self.Icon_Talk.EnableIcon(self.Char_Lilly_S.Name, False)
        self.Status_TaskCompletion += " Task02 --> "
        self.V.Set.EnableInput()
        return
    def SC_Task03_Bob_Lilly_Talk1(self):
        self.V.Set.DisableInput()

        self.D_CBR03_Bob_LillyS_Talk_English = self.V.D_CBR03_Bob_LillyS_Talk_English
        camelotMessage = self.D_CBR03_Bob_LillyS_Talk_English.ShowDialogs(self.Char_Bob.Name, self.Char_Lilly_S.Name)

        self.Icon_Talk.DisableIcon(self.Char_Lilly_S.Name)
        self.Icon_Torch.EnableIcon(self.Char_Lilly_S.Name)
        self.Status_TaskCompletion += " Task03 --> "
        self.V.Set.EnableInput()
        return

    # -------------------------- Bob - LiTourch - Lilly --------------------------
    def SC_Task04_Bob_Lilly_LitTourch(self):
        self.V.Set.DisableInput()
        self.V.Set.Position(self.Item_LitTorch.Name, self.Char_Lilly_S.Name)
        self.Char_Lilly_S.Give(self.Item_LitTorch.Name, self.Char_Bob.Name)
        #self.Char_Lilly_S_Inventory.Remove(self.Item_BlueKey.Name)
        self.Icon_Torch.DisableIcon(self.Char_Lilly_S.Name)
        self.Icon_Torch.EnableIcon(self.Place_CastleBedRoom.Fireplace)
        self.Status_TaskCompletion += " Task04 --> "
        self.V.Set.EnableInput()
        return
    # -------------------------- Bob - LiTourch - FirePlace --------------------------
    def SC_Task05_Bob_Fireplace_LitTourch(self):
        self.V.Set.DisableInput()
        self.Char_Bob.WalkTo(self.Place_CastleBedRoom.Fireplace)
        self.Char_Bob.Kneel()
        self.Char_Bob.PutDown(self.Item_LitTorch.Name)
        self.VEffect_Campfire.EnableEffect()

        self.Icon_Torch.DisableIcon(self.Place_CastleBedRoom.Fireplace)
        self.Icon_Dress.EnableIcon(self.Place_CastleBedRoom.Closet)
        self.Icon_TakeMoney.EnableIcon(self.Place_CastleBedRoom.Closet)

        self.Status_TaskCompletion += " Task05 --> "
        self.V.Set.EnableInput()
        return
    # -------------------------- Bob - Closet - Dress --------------------------
    def SC_Task06_Bob_Closet_Dress(self):
        self.V.Set.DisableInput()
        self.Char_Bob.WalkTo(self.Place_CastleBedRoom.Closet)
        self.Char_Bob.SetClothing("Noble")
        self.SEffect_Pocket.Play()
        self.Icon_Dress.DisableIcon(self.Place_CastleBedRoom.Closet)
        if "Task07" in self.Status_TaskCompletion:
            self.Icon_BlueKey.EnableIcon(self.Char_Lilly_S.Name)
        self.Status_TaskCompletion += " Task06 --> "
        self.V.Set.EnableInput()
        return
    # -------------------------- Bob - Closet - Coin --------------------------
    def SC_Task07_Bob_Closet_Money(self):
        self.V.Set.DisableInput()
        self.Char_Bob.WalkTo(self.Place_CastleBedRoom.Closet)
        self.V.Set.Position(self.Item_Coin.Name, self.Char_Bob.Name)
        self.SEffect_Pocket.Play()
        self.Char_Bob.Pocket(self.Item_Coin.Name)
        self.V.Char_Bob_Inventory.Add(self.Item_Coin.Name, "Money to Buy")
        self.Icon_TakeMoney.DisableIcon(self.Place_CastleBedRoom.Closet)
        if "Task06" in self.Status_TaskCompletion:
            self.Icon_BlueKey.EnableIcon(self.Char_Lilly_S.Name)
        self.Status_TaskCompletion += " Task07 --> "

        self.V.Set.EnableInput()
        return
    # -------------------------- Bob - Talk - Ask Key - Lilly --------------------------
    def SC_Task08_Bob_Lilly_ChestKey(self):
        self.V.Set.DisableInput()
        self.V.Set.Position(self.Item_BlueKey.Name, self.Char_Lilly_S.Name)
        self.Char_Lilly_S.Give(self.Item_BlueKey.Name, self.Char_Bob.Name)
        #self.Char_Lilly_S_Inventory.Remove(self.Item_BlueKey.Name)
        #self.SEffect_Pocket.Play()
        self.Char_Bob.Pocket(self.Item_BlueKey.Name)
        self.Char_Bob_Inventory.Add(self.Item_BlueKey.Name)

        self.Icon_BlueKey.DisableIcon(self.Char_Lilly_S.Name)
        self.Icon_Chest.EnableIcon(self.Item_BlueKey.Name)
        self.Icon_Unlock.EnableIcon(self.Place_CastleBedRoom.Chest)

        self.Status_TaskCompletion += " Task08 --> "
        self.V.Set.EnableInput()
        return

    # -------------------------- Bob - Key - Chest - Open --------------------------
    def SC_Task09_Bob_Chest_Open(self):
        self.V.Set.DisableInput()
        self.Char_Bob.WalkTo(self.Place_CastleBedRoom.Chest)
        self.Char_Bob.Unpocket(self.Item_BlueKey.Name)
        self.Char_Bob_Inventory.Remove(self.Item_BlueKey.Name)
        self.Char_Bob.PutDown(self.Item_BlueKey.Name)
        self.Char_Bob.OpenFurniture(self.Place_CastleBedRoom.Chest)
        self.CBR_Item_Chest_Inventory.Show()
        self.Status_TaskCompletion += " Task09 --> "
        self.V.Set.EnableInput()
        return
    # -------------------------- Bob - Key - Chest - Take Compass --------------------------
    def SC_Task10_Bob_Chest_Compass(self):
        self.V.Set.DisableInput()
        self.CBR_Item_Chest_Inventory.Remove(self.Item_Compass.Name)
        self.V.Set.Position(self.Item_Compass.Name, self.Char_Bob.Name)
        self.Char_Bob.Pocket(self.Item_Compass.Name)
        self.Char_Bob_Inventory.Add(self.Item_Compass.Name)
        self.Icon_Take.DisableIcon(self.Item_Compass.Name)

        if "Task11" in self.Status_TaskCompletion:
            self.Icon_City.EnableIcon(self.Place_CastleBedRoom.Door)
            self.CBR_Item_Chest_Inventory.Hide()
        self.Status_TaskCompletion += " Task10 --> "
        self.V.Set.EnableInput()
        return
    # -------------------------- Bob - Key - Chest - Take Hammer --------------------------
    def SC_Task11_Bob_Chest_Hammer(self):
        self.V.Set.DisableInput()
        self.CBR_Item_Chest_Inventory.Remove(self.Item_Hammer.Name)
        self.V.Set.Position(self.Item_Hammer.Name, self.Char_Bob.Name)
        self.Char_Bob.Pocket(self.Item_Hammer.Name)
        self.Char_Bob_Inventory.Add(self.Item_Hammer.Name)
        self.Icon_Take.DisableIcon(self.Item_Hammer.Name)
        if "Task10" in self.Status_TaskCompletion:
            self.Icon_City.EnableIcon(self.Place_CastleBedRoom.Door)
            self.CBR_Item_Chest_Inventory.Hide()
        self.Status_TaskCompletion += " Task11 --> "
        self.V.Set.EnableInput()
        return
    # -------------------------- Bob - Door - Exit - City --------------------------
    def SC_Task12_Bob_Door_Exit(self):
        self.V.Set.DisableInput()
        self.Char_Bob.Exit(self.Place_CastleBedRoom.Door)
        self.V.Display.FadeOut()
        self.Icon_City.DisableIcon(self.Place_CastleBedRoom.Door)
        self.Status_TaskCompletion += " Task12 --> "
        self.V.Set.EnableInput()
        return
    def CBR_Hints(self):
        self.V.Set.DisableInput()
        if self.Status_TaskCompletion == "":
            Message = f"HINT : Unlock the Door"
            _ = Message_([Message], self.V.Action).ShowNarration()
        elif "Task11" in self.Status_TaskCompletion:
            Message = f"HINT : Exit from Door to City"
            _ = Message_([Message], self.V.Action).ShowNarration()
        elif ("Task08" in self.Status_TaskCompletion) or ("Task09" in self.Status_TaskCompletion) or ("Task10" in self.Status_TaskCompletion):
            Message = f"HINT : Collect Items from Chest"
            _ = Message_([Message], self.V.Action).ShowNarration()
        elif "Task07" in self.Status_TaskCompletion:
            Message = f"HINT : Get Key from {self.Char_Lilly_S.Name}"
            _ = Message_([Message], self.V.Action).ShowNarration()
        elif ("Task05" in self.Status_TaskCompletion) or ("Task06" in self.Status_TaskCompletion):
            Message = f"HINT : Get Clothes and Money from Closet"
            _ = Message_([Message], self.V.Action).ShowNarration()
        elif "Task04" in self.Status_TaskCompletion:
            Message = f"HINT : Put fire on at Fireplace"
            _ = Message_([Message], self.V.Action).ShowNarration()
        elif "Task03" in self.Status_TaskCompletion:
            Message = f"HINT : Get Torch from Lilly"
            _ = Message_([Message], self.V.Action).ShowNarration()
        elif "Task02" in self.Status_TaskCompletion:
            Message = f"HINT : Talk to {self.Char_Lilly_S.Name}"
            _ = Message_([Message], self.V.Action).ShowNarration()
        elif "Task01" in self.Status_TaskCompletion:
            Message = f"HINT : Talk to {self.Char_Candy.Name}"
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
            elif ("Icon Chest" in self.camelotMessage) and (self.Item_BlueKey.Name in self.camelotMessage):
                self.V.Char_Bob_Inventory.Hide()
                self.SC_Task09_Bob_Chest_Open()
                self.V.Set.EnableInput()
                break
            elif "Game Instructions" in self.camelotMessage:
                self.V.Char_Bob_Inventory.Hide()
                self.V.D_GameInstructions.ShowDialogs(self.Char_Bob.Name)
                self.V.Set.EnableInput()
                self.V.Char_Bob_Inventory.Show()

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    '''
    def SC_Task03_Bob_Lilly_Talk111(self):
        self.V.Set.DisableInput()

        self.Status_TaskCompletion += " Task03 --> "
        self.V.Set.EnableInput()
        return
    # -------------------------- Bob - Talk - Candy --------------------------
    # -------------------------- Bob - Clap - Lilly --------------------------
    # -------------------------- Bob - Talk - Lilly --------------------------
    # -------------------------- Bob - LiTourch - Lilly --------------------------
    # -------------------------- Bob - LiTourch - FirePlace --------------------------
    # -------------------------- Bob - Closet - Dress --------------------------
    # -------------------------- Bob - Closet - Coin --------------------------
    # -------------------------- Bob - Talk - Ask Key - Lilly --------------------------
    # -------------------------- Bob - Key - Chest - Take Compass --------------------------
    # -------------------------- Bob - Door - Exit - City --------------------------

    def UC_Select_Task1(self):
        TF = self.V.Set.EnableInput()
        TF = self.V.SEffect_Ominous.Play()
        while True:
            camelotMessage = input()
            # -------------------------- Bob - Candy - Talk --------------------------
            if ("Icon" in camelotMessage) and ("Talk" in camelotMessage) and (self.Char_Candy.Name in camelotMessage):
                if self.Task_Bob_Candy_Talk_Limit > 0:
                    TF = self.V.SEffect_Ominous.Stop()
                    self.Status_CBR += self.SC_Task01_Bob_Candy_Talk()
                    self.Task_Bob_Candy_Talk_Limit -= 1
                else:
                    TF = self.SEffect_Error.Play()
                    _ = Message_([f"Candy is sleeping"], self.V.Action).ShowNarration()

            # -------------------------- Bob - Lilly - Talk --------------------------
            if ("Icon" in camelotMessage) and ("Talk" in camelotMessage) and (self.Char_Lilly_S.Name in camelotMessage):
                if self.Task_Bob_Lilly_Talk_Limit > 0:
                    TF = self.V.SEffect_Ominous.Stop()
                    self.Status_CBR += self.SC_Task02_CBR_Bob_Lilly_Talk()
                    self.Task_Bob_Candy_Talk_Limit -= 1
                else:
                    TF = self.SEffect_Error.Play()
                    #_ = Message_([f"Lilly is Busy in work"], self.V.Action).ShowNarration()

            # -------------------------- Bob - Lilly - FirePlace --------------------------
            if ("Icon" in camelotMessage) or ("FirePlace" in camelotMessage):
                if self.Task_Bob_Lilly_Talk_Limit==0:
                    TF = self.V.SEffect_Ominous.Stop()
                    self.Status_CBR += self.SC_Task03_CBR_Bob_Lilly_FirePlace()
                else:
                    TF = self.SEffect_Error.Play()
                    #_ = Message_([f"First talk with Lilly"], self.V.Action).ShowNarration()

            # -------------------------- Bob - Closet - Dress --------------------------
            elif ("Icon" in camelotMessage) and ("Dress" in camelotMessage) and (self.Task_Bob_Candy_Talk_Limit < 2):
                if self.Task_Bob_Closet_Dress_Limit > 0:
                    TF = self.V.SEffect_Ominous.Stop()
                    self.Status_CBR += self.SC_Task04_CBR_Bob_Closet_Dress()
                else:
                    TF = self.SEffect_Error.Play()
                    #_ = Message_(["Dress already Changed"], self.V.Action).ShowNarration()

            # -------------------------- Bob - Closet - Money --------------------------
            if ("Icon" in camelotMessage) and ("Money" in camelotMessage) and (self.Task_Bob_Lilly_Talk_Limit==0):
                if self.Task_Bob_Closet_Money_Limit > 0:
                    TF = self.V.SEffect_Ominous.Stop()
                    self.Status_CBR += self.SC_Task05_CBR_Bob_Closet_Money()
                else:
                    TF = self.SEffect_Error.Play()
                    #_ = Message_(["Task Completed"], self.V.Action).ShowNarration()

            # -------------------------- Bob - Door - City --------------------------
            if ("Icon City" in camelotMessage) or ("City" in camelotMessage) and (self.Task_Bob_Candy_Talk_Limit < 2):
                TF = self.V.SEffect_Ominous.Stop()
                self.Status_CBR += self.SC_Task06_CBR_Bob_Door_Exit_City()
                return self.Status_CBR

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # ===============================================  SYSTEM CONTROL  =============================================
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # =============================================  Bob - Candy - Talk  ===========================================
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    def SC_Task01_Bob_Candy_Talk(self):
        TF = self.V.Set.DisableInput()
        TF = self.V.SEffect_Serenade.Play()
        TF = self.Char_Bob.WalkTo(self.Char_Candy.Name)

        D_CBR01_Bob_Candy = self.V.D_CBR01_Bob_Candy_Talk_1_English
        camelotMessage = D_CBR01_Bob_Candy.ShowDialogs(self.Char_Bob.Name, self.Char_Candy.Name)

        self.Status_TaskCompletion = "Task01 --> "

        status = ""
        if self.Task_Bob_Candy_Talk_Limit == 2:
            D_CBR01_Bob_Candy = self.V.D_CBR01_Bob_Candy_Talk_1_English
            TF = D_CBR01_Bob_Candy.ShowDialogs(self.Char_Bob.Name, self.Char_Candy.Name)
            TF = self.Char_Bob.Face(self.Place_CastleBedroom.Door)
            TF = self.Char_Bob.Clap()
            TF = self.V.Set.CameraFocus(self.Place_CastleBedroom.Door)
            TF = self.Char_Lilly_S.Enter(self.Place_CastleBedroom.Door)
            TF = self.Char_Lilly_S.WalkTo(self.Char_Bob.Name)
            self.Task_Bob_Candy_Talk_Limit -= 1
            status = " --> Completed Candy Talk1 "
        elif (self.Task_Bob_Candy_Talk_Limit == 1) & (self.Task_Bob_Lilly_Talk_Limit == 0):
            D_CBR03_Bob_Candy_Talk_2 = self.V.D_CBR02_Bob_Candy_Talk_2_English
            TF = D_CBR03_Bob_Candy_Talk_2.ShowDialogs(self.Char_Bob.Name, self.Char_Candy.Name)
            status = " --> Completed Candy Talk2 "
        TF = self.V.SEffect_Serenade.Stop()
        TF = self.V.Set.EnableInput()
        return status

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # =============================================  Bob - Lilly - Talk  ===========================================
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    def SC_Task02_CBR_Bob_Lilly_Talk(self):
        TF = self.V.Set.DisableInput()
        TF = self.V.SEffect_Serenade.Play()
        D_CBR02_Bob_LillyS_Talk = self.V.D_CBR03_Bob_LillyS_Talk_English
        camelotMessage = D_CBR02_Bob_LillyS_Talk.ShowDialogs(self.Char_Bob.Name, self.Char_Lilly_S.Name)
        status = " --> Completed Lilly Talk "
        TF = self.V.SEffect_Serenade.Stop()
        TF = self.V.Set.EnableInput()
        return status

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # ==========================================  Bob - Lilly - FirePlace  =========================================
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    def SC_Task03_CBR_Bob_Lilly_FirePlace(self):
        TF = self.V.Set.DisableInput()
        TF = self.V.SEffect_Serenade.Play()
        TF = self.V.Set.CameraFocus(self.Char_Lilly_S.Name)
        TF = self.V.Set.CameraMode('track')

        TF = self.Char_Lilly_S.WalkTo(self.Place_CastleBedroom.Fireplace)
        TF = self.Char_Lilly_S.Kneel()

        if self.Task_Bob_Lilly_FirePlace_Limit == 1:
            TF = self.SEffect_Fireball.Play()
            TF = self.VEffect_Campfire.EnableEffect()
            TF = self.SEffect_Fireplace.Play()
            self.Task_Bob_Lilly_FirePlace_Limit -= 1
            status = "--> Enabled Fire at FirePlace"
        else:
            TF = self.VEffect_Campfire.DisableEffect()
            self.Task_Bob_Lilly_FirePlace_Limit += 1
            status = "--> Disabled Fire at FirePlace "

        TF = self.Char_Lilly_S.WalkTo(self.Place_CastleBedroom.SmallTable)
        TF = self.Char_Lilly_S.Kneel(True)

        TF = self.V.SEffect_Serenade.Stop()
        TF = self.V.Set.EnableInput()
        return status

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # ==========================================  Bob - Closet - Dress  =========================================
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    def SC_Task04_CBR_Bob_Closet_Dress(self):
        TF = self.V.Set.DisableInput()
        TF = self.V.SEffect_Serenade.Play()

        TF = self.Char_Bob.WalkTo(self.Place_CastleBedroom.Closet)
        TF = self.Char_Bob.SetClothing("Noble")
        TF = self.SEffect_Pocket.Play()
        TF = self.V.Icon_Dress.DisableIcon()

        TF = self.V.SEffect_Serenade.Stop()
        TF = self.V.Set.EnableInput()
        self.Task_Bob_Closet_Dress_Limit -= 1
        return " --> Dress Changed "

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # ==========================================  Bob - Closet - Money  =========================================
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    def SC_Task05_CBR_Bob_Closet_Money(self):
        TF = self.V.Set.DisableInput()
        TF = self.V.SEffect_Serenade.Play()

        TF = self.Char_Bob.WalkTo(self.Place_CastleBedroom.Closet)
        TF = self.Char_Bob.SetClothing("Noble")
        TF = self.SEffect_Pocket.Play()

        TF = self.V.SEffect_Serenade.Stop()

        self.Task_Bob_Closet_Money_Limit -= 1
        TF = self.V.Set.EnableInput()
        return " --> Money Taken "

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # =========================================  Bob - Door - Exit - CIty  =========================================
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    def SC_Task06_CBR_Bob_Door_Exit_City(self):
        TF = self.V.Set.DisableInput()
        TF = self.V.Set.CameraMode('track')
        TF = self.V.Set.CameraFocus(self.Char_Bob.Name)
        TF = self.Char_Bob.Exit(self.Place_CastleBedroom.Door)
        TF = self.V.Display.FadeOut()
        TF = self.V.Set.EnableInput()
        return " --> Exit to City "
    '''
'''
from GlobalVariables import Variables
V = Variables()
ABFC = Activities_CastleBedRoom_(V)
ABFC.SC_Start()
ABFC.UC_Select_Task()
'''