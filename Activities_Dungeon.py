from Messages import Message_
class Activity_Dungeon:
    def __init__(self,V):
        self.V = V
        #create a place
        self.V.Place_Dungeon.CreatePlace()
        #create characters
        self.V.Set.Position(self.V.Char_AngelOfDeath.Name, self.V.Place_Dungeon.Bed)
        #self.V.Char_Bob.Enter(self.V.Place_Dungeon.Door)

        #create item
        self.V.Item_ChestKey.CreateItem()

        # enable icon
        self.V.Icon_GreenKey.EnableIcon(self.V.Place_Dungeon.Chest)
        self.V.Icon_Door.EnableIcon(self.V.Place_Dungeon.Door)
        #self.V.Icon_Door.EnableIcon(self.V.Place_Dungeon.CellDoor)
        #self.V.Icon_Talk.EnableIcon(self.V.Char_AngelOfDeath.Name)


    def start(self):
        self.V.Set.CameraFocus(self.V.Place_Dungeon.Door)
        self.V.Set.CameraMode('track')
        self.V.Set.CameraBlend(2)

        self.V.Display.FadeIn()
        self.V.Char_Bob.Enter(self.V.Place_Dungeon.Door)
        self.V.Set.CameraFocus(self.V.Char_Bob.Name)
        self.V.Set.CameraMode('follow')


    def UC_Select_Task(self):
        self.V.Set.EnableInput()
        while True:
            Camelot_Message = input()
            if ('Icon' in Camelot_Message) and ('GreenKey' in Camelot_Message):
                self.SC_Task01_Chest()

            elif ('Icon' in Camelot_Message) and ('CellDoor' in Camelot_Message):
                self.SC_Task02_CellDoor()

            elif ('Icon' in Camelot_Message) and ('Talk' in Camelot_Message) and (self.V.Char_AngelOfDeath.Name):
                self.SC_Task03_Bob_AngelTalk()
                return 'done'


    def SC_Task01_Chest(self):
        self.V.Set.DisableInput()
        self.V.Char_Bob.OpenFurniture(self.V.Place_Dungeon.Chest)
        self.V.Set.Position(self.V.Item_ChestKey.Name, self.V.Char_Bob.Name)
        self.V.Icon_Door.EnableIcon(self.V.Place_Dungeon.CellDoor)
        self.V.Set.EnableInput()

    def SC_Task02_CellDoor(self):
        self.V.Set.DisableInput()
        self.V.Char_Bob.Enter(self.V.Place_Dungeon.CellDoor)
        self.V.Set.EnableInput()

    def SC_Task03_Bob_AngelTalk(self):
        self.V.Set.DisableInput()
        AngelTalk = Message_(["Angel: Thanks for saving me",
                              "How can I help you?",
                              "Bob: Actually i came here to meet you,Please help me to save my wife... she is sick"
                              ], self.V.Action)
        AngelTalk.ShowDialogs(self.V.Char_Bob.Name, self.V.Char_AngelOfDeath.Name)
        self.V.Char_Bob.Exit(self.V.Place_Dungeon.Door, False)
        self.V.Char_AngelOfDeath.Exit(self.V.Place_Dungeon.Door)
        self.V.Display.FadeOut()
        self.V.Set.EnableInput()























