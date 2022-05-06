
class Setup:
    def __init__(self, V):
        self.V = V
    def Create(self):
        # ============================================= PLACES : CREATING
        for place in self.V.places.keys():
            TF = eval(f"self.V.Place_{place}.CreatePlace()")
            if TF == True: continue
        # ============================================= CHARACTERS : CREATING
        for char in self.V.characters.keys():
            TF = eval(f"self.V.Char_{char}.CreateCharacter()")
            if TF == True: continue
        # ============================================= ITEMS : CREATING
        for item in self.V.items.keys():
            TF = eval(f"self.V.Item_{item}.CreateItem()")
            if TF == True: continue

        '''V.Place_ForestPath

        V.Char_Bob
        V.Char_Angel
        
        self.Item_BluePotion = V.Item_BluePotion
        self.Item_RedPotion = V.Item_RedPotion
        self.Item_CloseScroll = V.Item_CloseScroll
        self.Item_PurpleBook = V.Item_PurpleBook
        '''
        # ============================================= SHOW MENU
        self.V.Display.FadeOut()
        self.V.Set.CameraFocus(self.V.Place_ForestPath.EastEnd)
        self.V.Set.CameraMode('track')  # track, focus, follow
        self.V.Set.CameraBlend(4)

        self.V.Display.Menu_Title_Set(self.V.Menu_Title)
        self.V.Display.Menu_Show()
        self.V.D_GameInstructions.ShowDialogs()
        camelotMessage = self.V.D_Music_On_Off.ShowDialogs()
        self.V.Set.EnableInput()
        if "CloseOn" in camelotMessage:
            self.V.Music_On_Off = "ON"
        elif "CloseOff" in camelotMessage:
            self.V.Music_On_Off = "OFF"



'''from GlobalVariables import Variables
V = Variables()
S = Setup(V)
S.Create()'''