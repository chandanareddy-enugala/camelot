class Setup:
    def __init__(self, V):
        self.V = V
    def Create(self):
        # ============================================= PLACES : CREATING
        self.V.Place_ForestPath.CreatePlace()
        self.V.Place_Bridge.CreatePlace()
        self.V.Place_CastleBedRoom.CreatePlace()
        self.V.Place_City.CreatePlace()
        self.V.Place_Dungeon.CreatePlace()
        self.V.Place_CastleCrossroads.CreatePlace()
        self.V.Place_Ruins.CreatePlace()
        self.V.Place_Farm.CreatePlace()
        # ============================================= CHARACTERS : CREATING
        self.V.Char_Bob.CreateCharacter()
        self.V.Char_Candy.CreateCharacter()
        self.V.Char_Lilly_S.CreateCharacter()
        self.V.Char_Amelia_S.CreateCharacter()
        self.V.Char_Angel.CreateCharacter()
        self.V.Char_AngelOfDeath.CreateCharacter()
        self.V.Char_Devil.CreateCharacter()
        self.V.Char_Tom_S.CreateCharacter()
        self.V.Char_Jim_S.CreateCharacter()
        self.V.Char_Jack_S.CreateCharacter()
        self.V.Char_Begger_S.CreateCharacter()
        self.V.Char_Devil.CreateCharacter()
        self.V.Char_Priest.CreateCharacter()

        # ============================================= ITEMS : CREATING
        self.V.Item_BlueBook.CreateItem()
        self.V.Item_RedBook.CreateItem()
        self.V.Item_GreenBook.CreateItem()
        self.V.Item_PurpleBook.CreateItem()
        self.V.Item_EvilBook.CreateItem()
        self.V.Item_SpellBook.CreateItem()
        self.V.Item_BluePotion.CreateItem()
        self.V.Item_RedPotion.CreateItem()
        self.V.Item_GreenPotion.CreateItem()
        self.V.Item_PurplePotion.CreateItem()
        self.V.Item_BlueKey.CreateItem()
        self.V.Item_RedKey.CreateItem()
        self.V.Item_GreenKey.CreateItem()
        self.V.Item_PurpleKey.CreateItem()
        self.V.Item_JewelKey.CreateItem()
        self.V.Item_ChestKey.CreateItem()

        # ============================================= SHOW MENU
        self.V.Display.FadeOut()
        self.V.Set.CameraFocus(self.V.Place_ForestPath.EastEnd)
        self.V.Set.CameraMode('track')  # track, focus, follow
        self.V.Set.CameraBlend(4)

        self.V.Display.Menu_Title_Set(self.V.Menu_Title)
        self.V.Display.Menu_Show()
        self.V.D_GameInstructions.ShowDialogs()
        camelotMessage = self.V.D_Music_On_Off.ShowDialogs()
        if "ON" in camelotMessage:
            self.V.Music_On_Off = "ON"
        elif "OFF" in camelotMessage:
            self.V.Music_On_Off = "OFF"



'''from GlobalVariables import Variables
V = Variables()
S = Setup(V)
S.Create()'''