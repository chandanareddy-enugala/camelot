
from GlobalVariables import Variables

# (((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((
# --------------------------------------------------------------------------------------------------- LEVEL 1
# )))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
class Level_1:
    def __init__(self):
        self.V = Variables()
        self.Action = self.V.Action
        self.Set = self.V.Set
        self.Display = self.V.Display
        self.Sound = self.V.Sound
        self.Level_1_Status = self.V.Level_1_Status
        self.Task1_Status = ""
        self.Task2_Status = ""
        self.Task3_Status = ""

        # ================================================================== ITEMS
        self.MedicineBook = self.V.MedicineBook
        self.BobHouseKey = self.V.BobHouseKey
        self.Money = self.V.Money

        # ================================================================== Loading Entities
        self.BobHouse = self.V.BobHouse
        self.Bob = self.V.Bob
        self.BobWife = self.V.BobWife
        self.BobHouseWorker = self.V.BobHouseWorker

    def StartGame(self):
        # ================================================================== Creating Entities
        self.TF = self.BobHouse.Create_Place()
        self.TF = self.Bob.Create_Character()
        self.TF = self.BobWife.Create_Character()
        self.TF = self.BobHouseWorker.Create_Character()

        # ================================================================== Positions of the Characters at BobHouse
        self.Bob.Set_Position(self.BobHouse.Door)
        self.Bob.Face(self.BobHouse.Door)
        self.BobWife.Set_Position(self.BobHouse.Closet)
        self.BobWife.Face((self.BobHouse.Fireplace))

        # ================================================================== Camera Settings at BobHouse
        TF = self.Set.cameraFocus(self.BobHouse.Door)
        TF = self.Set.cameraMode('track')
        TF = self.Set.cameraBlend(3)
        TF = self.Display.FadeOut()

        # ================================================================== Show Menu
        self.ShowMenu()



    def Home(self):

        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # ------------------------------------------------------------------------------------------------------  NARRATION 1
        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # Narration to be added ------------------------------------------
        TF = self.Display.ShowNarration("Once there lived Bob and his wife goldie... goldie falls sick, poor Bob wants to revive his wife life,inorder to get the medicine he has to pass some levels in the game....Finally after lot of hurdles he finds the medicne!", True)

        TF = self.Set.cameraFocus(self.BobHouse.Bed)
        TF = self.Display.FadeIn()

        TF = self.BobWife.Sleep(self.BobHouse.Bed_Right, True)
        TF = self.Bob.WalkTo(self.BobHouse.SmallTable, True)
        TF = self.Bob.Face(self.BobWife.Name)
        self.Sound.Play(self.Sound.Grief)
        TF = self.Bob.Kneel()

        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # ------------------------------------------------------------------------------------------------------  NARRATION 2
        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        TF = self.Display.ShowNarration("Goldie how are you doing now, dont worry i will get the medicine", True)

        TF = self.Set.cameraFocus(self.Bob.Name)
        TF = self.Bob.WalkTo(self.BobHouse.Door, True)
        TF = self.Bob.WalkTo(self.BobHouse.Table_Left, True)
        TF = self.Bob.WalkTo(self.BobHouse.Bed_Middle, True)
        TF = self.Bob.Face(self.BobHouse.Door)
        TF = self.Bob.Clap(True)
        TF = self.Set.cameraMode('follow')
        self.BobHouseWorker.Enter(self.BobHouse.Door, True)
        self.BobHouseWorker.WalkTo(self.Bob.Name, True)
        self.Set.cameraMode('track')
        self.Set.cameraFocus(self.Bob.Name)

        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # ------------------------------------------------------------------------------------------------------  NARRATION 3
        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        TF = self.Display.ShowNarration("Bob calls his worker to look after his wife since he is going to get the medicine", True)

        TF = self.Bob.WalkTo(self.BobHouse.Table)
        self.BobHouseWorker.WalkTo(self.BobHouse.SmallTable)
        TF = self.BobHouseWorker.Face(self.BobWife.Name)
        TF = self.BobHouseWorker.Kneel()
        TF = self.Bob.WalkTo(self.BobHouse.Bed_Left, True)
        TF = self.Bob.Face(self.BobHouseWorker.Name)
        TF = self.Set.Wait(2)
        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # ------------------------------------------------------------------------------------------------------  NARRATION 4
        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        TF = self.Bob.Face(self.BobHouse.Door)
        TF = self.Set.cameraFocus(self.Bob.Name)
        self.Set.cameraMode('follow')
        self.Sound.Stop(self.Sound.Grief)
        # Enable Icons
        self.Action.Execute_Command(f'EnableIcon("Open_Door", Open, {self.BobHouse.Door}, "Leave the house", true)')

        # ----------------------------------------------------------------------------------------------------- Player Task 1
        self.Set.Wait(2)
        self.Display.ShowNarration("Before going out Bob changes his attire and takes money", True)
        Task1_Status = self.Task1_Closet()

        self.Set.Wait(2)
        self.Display.ShowNarration("Find a KEY !!!", True)
        Task2_Status = self.Task2_Chest()

        return self.Level_1_Status
        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # ------------------------------------------------------------------------------------------------------  ADD SOME TASKS AT HOME, SO THAT PLAYER WILL COMPLETE TASKS
        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # After completed some tasks we take player in our control

# Additional Functions which will be used in the above tasks.
# ----------------------------------------------------------------------------------------------------
    def Task1_Closet(self):
        self.Set.EnableIcon("Clothes", 'dress', self.BobHouse.Closet, "Clothes")
        self.Set.EnableIcon("Money", 'coins', self.BobHouse.Closet, "Money")
        self.Set.Poistion(self.Money, self.BobHouse.Closet)
        self.Set.EnableInput()

        count=0
        while count<2:
            receivedMessage = input()
            if "Clothes" in receivedMessage:
                self.Set.DisableInput()
                self.Bob.OpenFurniture(self.BobHouse.Closet)
                self.Bob.SetClothing("Noble")
                self.Set.EnableInput()
                self.Task1_Status += " Clothes "
                count+=1
            elif "Money" in receivedMessage:
                self.Set.DisableInput()
                self.Bob.OpenFurniture(self.BobHouse.Closet)
                # self.Bob.Take(self.Money.Name, self.BobHouse.Closet)
                self.Sound.Play("Pocket")
                self.Set.EnableInput()
                self.Task2_Status += " Money "
                count += 1
            elif receivedMessage == f'input Open_Door {self.BobHouse.Door}':
                TF = self.Display.ShowNarration("Door is Locked!", True)
                self.Set.Wait(3)
                self.Display.HideNarration()
                if (("Clothes" in self.Task1_Status) & ("Money" not in self.Task1_Status)):
                    TF = self.Display.ShowNarration("You need to take Money", True)
                    self.Set.Wait(3)
                    self.Display.HideNarration()
                if (("Clothes" not in self.Task1_Status) & ("Money" in self.Task1_Status)):
                    TF = self.Display.ShowNarration("You need to Change Clothes", True)
                    self.Set.Wait(3)
                    self.Display.HideNarration()
                if (("Clothes" in self.Task1_Status) & ("Money" in self.Task1_Status)):
                    TF = self.Display.ShowNarration("Find Main Door Key", True)
                    self.Set.Wait(3)
                    self.Display.HideNarration()

        if count==3:
            self.Set.DisableInput()
            self.Bob.WalkTo(self.BobHouse.Bed)
            self.Bob.Face(self.BobHouse.Chest)
            self.Level_1_Status = "_Task1_Closet_"
            return self.Level_1_Status

    def Task2_Chest(self):
        self.Set.Poistion(self.MedicineBook, self.BobHouse.Chest)
        self.Set.Poistion(self.BobHouseKey, self.BobHouse.Chest)
        self.Set.EnableIcon("Key", 'usekey', self.BobHouse.Chest, "Key")
        self.Set.EnableIcon("Medicine_Book", 'book', self.BobHouse.Chest, "Medicine Book")
        self.Set.EnableIcon("Sit", 'chair', self.BobHouse.Chair_Left, "Sit")
        self.Set.EnableInput()

        count = 0
        while count < 2:
            receivedMessage = input()
            if "Medicine_Book" in receivedMessage:
                self.Set.DisableInput()
                self.Bob.OpenFurniture(self.BobHouse.Chest)
                # self.Bob.Take(self.Bob.Name, self.MedicineBook, self.BobHouse.Chest)
                self.Sound.Play("Pocket")
                self.Set.EnableInput()
                self.Task2_Status += " Medicine_Book "
                count += 1
            elif "Key" in receivedMessage:
                self.Set.DisableInput()
                self.Bob.OpenFurniture(self.BobHouse.Chest)
                # self.Bob.Take(self.BobHouseKey.Name, self.BobHouse.Chest)
                # self.Bob.Pocket(self.BobHouseKey)
                self.Sound.Play("Pocket")
                self.Set.EnableInput()
                self.Task2_Status += " Key "
                count += 1
            elif receivedMessage == f'input Open_Door {self.BobHouse.Door}':
                TF = self.Display.ShowNarration("Door is Locked!", True)
                self.Set.Wait(3)
                self.Display.HideNarration()
                if (("Medicine_Book" in self.Task2_Status) & ("Key" not in self.Task2_Status)):
                    TF = self.Display.ShowNarration("Find the Door Key", True)
                    self.Set.Wait(3)
                    self.Display.HideNarration()
                if (("Medicine_Book" not in self.Task2_Status) & ("Key" in self.Task2_Status)):
                    TF = self.Display.ShowNarration("Take Medicine Book !!!", True)
                    self.Set.Wait(3)
                    self.Display.HideNarration()
                if (("Medicine_Book" in self.Task2_Status) & ("Key" in self.Task2_Status)):
                    TF = self.Display.ShowNarration("Find Main Door Key", True)
                    self.Set.Wait(3)
                    self.Display.HideNarration()

        if count==3:
            self.Set.DisableInput()
            self.Bob.WalkTo(self.BobHouse.Bed)
            self.Bob.Face(self.BobHouse.Door)
            self.Level_1_Status = "_Task2_Chest_"
            return self.Level_1_Status

    def Task3_Door(self):
        self.Set.EnableIcon("Exit_Door", 'unlock', self.BobHouse.Door, "Exit Door")
        self.Set.EnableIcon("Unlock_with_Key", 'usekey', self.BobHouse.Door, "Unlock")
        if self.Level_1_Status != "_Task2_Chest_":
            TF = self.Display.ShowNarration("You can Exit Home!!!!!!", True)
            self.Set.Wait(3)
            self.Display.HideNarration()
        self.Set.EnableInput()

        count = 0
        while count < 2:
            receivedMessage = input()

            if ("Exit_Door" in receivedMessage) or ("Unlock_with_Key" in receivedMessage):
                self.Set.DisableInput()
                self.Bob.Face(self.BobWife.Name)
                self.Bob.Wave()
                self.Bob.Face(self.BobHouse.Dooor)
                self.Bob.Exit(self.BobHouse.Door, False)
                self.Set.Wait(2)
                self.Display.FadeOut()
                self.Level_1_Status += "Completed Home"
                count += 1
    # ------------------------------------------------------------------------------------------------- Function: Show Menu
    def ShowMenu(self):
        TF = self.Display.SetMenuTitle("Game Area")
        TF = self.Display.ShowMenu()

        while True:
            inputMessage = input()
            if inputMessage == "input Selected Start":
                TF = self.Display.HideMenu()
                self.Home()
                break
            elif inputMessage == "input Selected Credits":
                TF = self.Display.ShowCredits()
                while True:
                    inputMessage = input()
                    if inputMessage == "input Close Credits":
                        TF = self.Display.HideCredits()
                        self.ShowMenu()
                        break
            elif inputMessage == "input Selected Quit":
                TF = self.Display.Quit()
                break
    # ------------------------------------------------------------------------------------------------- Function: 2 Task

