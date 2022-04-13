from Messages import Message_

class Activities_CastleBedRoom_:
    def __init__(self, V):
        self.V = V
        self.Status_CBR = ""
        self.Task_Bob_Candy_Talk_Limit = 2
        self.Task_Bob_Lilly_Talk_Limit = 1
        self.Task_Bob_Lilly_FirePlace_Limit = 1
        self.Task_Bob_Closet_Dress_Limit = 1
        self.Task_Bob_Closet_Money_Limit = 2
        self.Task_Bob_Door_Exit_City_Limit = 5         # Going City from Home is infinite but I kept temporarily 5 since, no one can go those many times.

        # --------------------------- PLACES ---------------------------
        self.Place_BobHouse = self.V.Place_BobHouse
        TF = self.Place_BobHouse.CreatePlace()
        if TF!=True:
            self.V.Display.Menu_Quit()
        # --------------------------- CHARACTERS ---------------------------
        self.Char_Bob = V.Char_Bob

        self.Char_Candy = self.V.Char_Candy
        TF = self.Char_Candy.CreateCharacter()
        if TF != True:
            self.V.Display.Menu_Quit()

        self.Char_Lilly_S = self.V.Char_Lilly_S
        TF = self.Char_Lilly_S.CreateCharacter()
        if TF != True:
            self.V.Display.Menu_Quit()

        # --------------------------- SET POSITION ---------------------------
        self.V.Set.Position(self.Char_Candy.Name, self.Place_BobHouse.Closet)
        self.Char_Candy.Sleep(self.Place_BobHouse.Bed)

        # # --------------------------- ITEMS ---------------------------
        # Clothes, Money, Key

        # # --------------------------- LISTS ---------------------------

        # --------------------------- VISUAL EFFECT ---------------------------
        self.VEffect_Campfire = self.V.VEffect_Campfire
        self.VEffect_Campfire.CreateEffect(self.Place_BobHouse.Fireplace)

        # # --------------------------- SOUND EFFECTS ---------------------------
        self.SEffect_Fireball = self.V.SEffect_Fireball
        self.SEffect_Pocket = self.V.SEffect_Pocket
        self.SEffect_Fireplace = self.V.SEffect_Fireplace
        self.SEffect_Dramatic = self.V.SEffect_Dramatic
        self.SEffect_DarkMagic = self.V.SEffect_DarkMagic
        self.SEffect_Ominous = self.V.SEffect_Ominous
        self.SEffect_Potion = self.V.SEffect_Potion
        self.SEffect_Spell2 = self.V.SEffect_Spell2
        self.SEffect_Error = self.V.SEffect_Error
        self.SEffect_Spooky = self.V.SEffect_Spooky

        # # --------------------------- ICONS ---------------------------
        self.Icon_Talk = self.V.Icon_Talk
        self.Icon_Dress = self.V.Icon_Dress
        self.Icon_Money = self.V.Icon_Money
        self.Icon_FirePlace = self.V.Icon_FirePlace
        self.Icon_City = self.V.Icon_City
        # --------------------------- ENABLE ICONS ---------------------------
        TF = self.Icon_Talk.EnableIcon(self.Char_Candy.Name, False)
        TF = self.Icon_Talk.EnableIcon(self.Char_Lilly_S.Name, False)
        TF = self.Icon_FirePlace.EnableIcon(self.Char_Lilly_S.Name, True)
        TF = self.Icon_Dress.EnableIcon(self.Place_BobHouse.Closet, True)
        TF = self.Icon_Money.EnableIcon(self.Place_BobHouse.Closet)
        TF = self.Icon_City.EnableIcon(self.Place_BobHouse.Door, True)

        # --------------------------- CAMERA ---------------------------
        TF = self.V.Set.Wait(1)
        TF = self.V.Display.FadeOut()
        TF = self.V.Set.CameraFocus(self.Place_BobHouse.Bed)
        TF = self.V.Set.CameraMode('track')
        TF = self.V.Set.CameraBlend(4)
        self.Status_CBR = "CastleBedRoom Setup "

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # ===================================================  START  ==================================================
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    def SC_ACBR_Start(self):
        TF = self.V.Set.DisableInput()
        TF = self.V.Display.FadeIn()
        TF = self.V.Set.CameraFocus(self.Place_BobHouse.Door)
        TF = self.Char_Bob.Enter(self.Place_BobHouse.Door)
        TF = self.V.Set.CameraFocus(self.Char_Bob.Name)
        TF = self.V.Set.CameraMode('focus')
        TF = self.Char_Bob.SetExpression('scared')
        TF = self.SEffect_Dramatic.Play()
        TF = self.V.Set.CameraMode('follow')
        TF = self.Char_Bob.WalkTo(self.Place_BobHouse.SmallTable)
        TF = self.Char_Bob.Face(self.Char_Candy.Name)
        TF = self.Char_Bob.Kneel(False)
        TF = self.V.Set.Wait(1)
        #TF = self.Char_Bob.WalkTo(self.Place_BobHouse.Door)
        TF = self.Char_Bob.WalkTo(self.Place_BobHouse.Table)
        #TF = self.Char_Bob.WalkTo(self.Place_BobHouse.Bed)
        TF = self.Char_Bob.Face(self.Char_Candy.Name)
        # --------------------------- CAMERA SETTINGS ---------------------------
        self.V.Set.CameraFocus(self.Char_Bob.Name)
        self.V.Set.CameraMode('follow')
        self.Status_CBR += " --> Reached Home "
        TF = self.SEffect_Dramatic.Stop()
        TF = self.V.Set.EnableInput()
        return self.Status_CBR

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # ================================================  USER CONTROL  ==============================================
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    def UC_Task00_Select_Task(self):
        TF = self.V.Set.EnableInput()
        TF = self.V.SEffect_Ominous.Play()
        while True:
            camelotMessage = input()
            # -------------------------- Bob - Candy - Talk --------------------------
            if ("Icon" in camelotMessage) and ("Talk" in camelotMessage) and (self.Char_Candy.Name in camelotMessage):
                if self.Task_Bob_Candy_Talk_Limit > 0:
                    TF = self.V.SEffect_Ominous.Stop()
                    self.Status_CBR += self.SC_Task01_CBR_Bob_Candy_Talk()
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
    def SC_Task01_CBR_Bob_Candy_Talk(self):
        TF = self.V.Set.DisableInput()
        TF = self.V.SEffect_Serenade.Play()
        TF = self.Char_Bob.WalkTo(self.Char_Candy.Name)
        TF = self.Char_Bob.Face(self.Char_Candy.Name)

        status = ""
        if self.Task_Bob_Candy_Talk_Limit == 2:
            D_CBR01_Bob_Candy = self.V.D_CBR01_Bob_Candy_Talk_1
            TF = D_CBR01_Bob_Candy.ShowDialogs(self.Char_Bob.Name, self.Char_Candy.Name)
            TF = self.Char_Bob.Face(self.Place_BobHouse.Door)
            TF = self.Char_Bob.Clap()
            TF = self.V.Set.CameraFocus(self.Place_BobHouse.Door)
            TF = self.Char_Lilly_S.Enter(self.Place_BobHouse.Door)
            TF = self.Char_Lilly_S.WalkTo(self.Char_Bob.Name)
            self.Task_Bob_Candy_Talk_Limit -= 1
            status = " --> Completed Candy Talk1 "
        elif (self.Task_Bob_Candy_Talk_Limit == 1) & (self.Task_Bob_Lilly_Talk_Limit == 0):
            D_CBR03_Bob_Candy_Talk_2 = self.V.D_CBR03_Bob_Candy_Talk_2
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
        D_CBR02_Bob_LillyS_Talk = self.V.D_CBR02_Bob_LillyS_Talk
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

        TF = self.Char_Lilly_S.WalkTo(self.Place_BobHouse.Fireplace)
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

        TF = self.Char_Lilly_S.WalkTo(self.Place_BobHouse.SmallTable)
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

        TF = self.Char_Bob.WalkTo(self.Place_BobHouse.Closet)
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

        TF = self.Char_Bob.WalkTo(self.Place_BobHouse.Closet)
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
        TF = self.Char_Bob.Exit(self.Place_BobHouse.Door)
        TF = self.V.Display.FadeOut()
        TF = self.V.Set.EnableInput()
        return " --> Exit to City "


'''from GlobalVariables import Variables
V = Variables()
S = ""
ABFC = Activities_CastleBedRoom_(V)
S += ABFC.SC_ACBR_Start()
S += ABFC.UC_Task00_Select_Task()

print(S)'''