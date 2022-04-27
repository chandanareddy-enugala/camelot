from Activities_Dungeon import Activity_Dungeon
class City:
    def __init__(self,V):
        self.V=V
        #create a place
        self.V.Place_City.CreatePlace()
        #create characters
        self.V.Char_Tom_S.CreateCharacter()
        self.V.Char_Jack_S.CreateCharacter()
        self.V.Char_AngelOfDeath.CreateCharacter()

        self.V.Set.Position(self.V.Char_Jack_S.Name, self.V.Place_City.Plant)
        self.V.Set.Position(self.V.Char_Tom_S.Name, self.V.Place_City.BlueHouseDoor)
        self.V.Set.Position(self.V.Char_Lilly_S.Name, self.V.Place_City.RedHouseDoor)
        #self.V.Set.Position(self.V.Char_AngelOfDeath.Name, self.V.Place_City.Fountain)

        #create a item
        self.V.Item_EvilBook.CreateItem()
        self.V.Item_BobSword.CreateItem()
        #create icons
        #self.V.Icon_Door.EnableIcon(self.V.Place_City.BlueHouseDoor)

        self.V.Icon_Talk.EnableIcon(self.V.Char_Tom_S.Name)
        self.V.Icon_Attack.EnableIcon(self.V.Char_Tom_S.Name)
        self.V.Icon_Talk.EnableIcon(self.V.Char_Lilly_S.Name)
        self.V.Icon_Attack.EnableIcon(self.V.Char_Lilly_S.Name)
        self.V.Icon_Talk.EnableIcon(self.V.Char_Jack_S.Name)
        self.V.Icon_Attack.EnableIcon(self.V.Char_Jack_S.Name)
        self.V.Icon_Sword.EnableIcon(self.V.Place_City.Fountain)
        self.V.Icon_SnowFlake.EnableIcon(self.V.Place_City.Fountain)
        self.V.Icon_EvilBook.EnableIcon(self.V.Place_City.Fountain)
        self.V.Icon_Hint.EnableIcon(self.V.Place_City.Fountain)


    def start(self):
        # camera settings
        self.V.Display.FadeOut()
        self.V.Set.CameraFocus(self.V.Place_City.NorthEnd)
        self.V.Set.CameraMode('track')
        self.V.Set.CameraBlend(2)

        self.V.Display.FadeIn()

        self.V.Char_Bob.Enter(self.V.Place_City.NorthEnd)
        self.V.Set.CameraFocus(self.V.Char_Bob.Name)

        self.V.Set.CameraMode('follow')


    def UC_Select_Task(self):
        self.V.Set.EnableInput()
        while True:
            Camelot_Message=input()  #input 'Select Icon Talk' Jim
            if ('Icon' in Camelot_Message) and ('Talk' in Camelot_Message) and (self.V.Char_Lilly_S.Name in Camelot_Message):
                self.SC_Task01_Bob_Lilly_Talk()
            elif ('Icon' in Camelot_Message) and ('Talk' in Camelot_Message) and (self.V.Char_Jack_S.Name in Camelot_Message):
                self.SC_Task02_Bob_Jack_Talk()
            elif ('Icon' in Camelot_Message) and ('Talk' in Camelot_Message) and (self.V.Char_Tom_S.Name in Camelot_Message):
                self.SC_Task03_Bob_Tom_Talk()
                self.V.Icon_Door.EnableIcon(self.V.Place_City.BlueHouseDoor)

            elif ('Icon' in Camelot_Message) and ('Attack' in Camelot_Message) and (self.V.Char_Lilly_S.Name in Camelot_Message):
                self.SC_Task05_Bob_Lilly_Fight()
            elif ('Icon' in Camelot_Message) and ('Attack' in Camelot_Message) and (self.V.Char_Jack_S.Name in Camelot_Message):
                self.SC_Task06_Bob_Jack_Fight()
            elif ('Icon' in Camelot_Message) and ('Attack' in Camelot_Message) and (self.V.Char_Tom_S.Name in Camelot_Message):
                self.SC_Task07_Bob_Tom_Fight()
                self.V.Icon_Door.EnableIcon(self.V.Place_City.BlueHouseDoor)

            elif ('Icon' in Camelot_Message) and ('BlueHouseDoor' in Camelot_Message):
                self.SC_Task10_Exit_BlueHouse()
                return 'completed'




    def SC_Task01_Bob_Lilly_Talk(self):
        self.V.Set.DisableInput()
        _ = self.V.D05_Bob_LillyS.ShowDialogs(self.V.Char_Bob.Name, self.V.Char_Lilly_S.Name)
        self.V.Set.EnableInput()

    def SC_Task02_Bob_Jack_Talk(self):
        self.V.Set.DisableInput()
        _ = self.V.D06_Bob_JackS.ShowDialogs(self.V.Char_Bob.Name, self.V.Char_Jack_S.Name)
        self.V.Set.EnableInput()

    def SC_Task03_Bob_Tom_Talk(self):
        self.V.Set.DisableInput()
        _ = self.V.D07_Bob_TomS.ShowDialogs(self.V.Char_Bob.Name, self.V.Char_Tom_S.Name)
        self.V.Char_Tom_S.Attack(self.V.Char_Bob.Name)
        self.V.Char_Bob.Attack(self.V.Char_Tom_S.Name)
        self.V.Char_Tom_S.Die()
        self.V.Set.EnableInput()

############ attack

    def SC_Task05_Bob_Lilly_Fight(self):
        # Bob walkto jim
        #self.V.Char_Bob.WalkTo(self.V.Char_Jim_S.Name, True)
        self.V.Set.DisableInput()
        self.V.Char_Bob.Attack(self.V.Char_Lilly_S.Name)    # Bob attcks jim
        self.V.Char_Lilly_S.Exit(self.V.Place_City.EastEnd)  # jim runsaway
        self.V.Set.EnableInput()


    def SC_Task06_Bob_Jack_Fight(self):
        self.V.Set.DisableInput()
        self.V.Char_Bob.Attack(self.V.Char_Jack_S.Name)  # Bob attcks jack
        self.V.Char_Jack_S.Exit(self.V.Place_City.EastEnd)  # jack runsaway
        self.V.Set.EnableInput()

    def SC_Task07_Bob_Tom_Fight(self):
        self.V.Set.DisableInput()
        self.V.Char_Bob.Attack(self.V.Char_Tom_S.Name)  # Bob attcks tom
        self.V.Char_Tom_S.Attack(self.V.Char_Bob.Name)
        self.V.Char_Bob.Attack(self.V.Char_Tom_S.Name)
        self.V.Char_Tom_S.Die()  # tom die
        self.V.Set.EnableInput()


    def SC_Task09_Bob_Exit_City(self):
        self.V.Set.DisableInput()
        self.V.Set.CameraMode('track')
        self.V.Set.CameraFocus(self.V.Char_Bob.Name)
        self.V.Char_Bob.Exit(self.V.Place_City.EastEnd, False)
        self.V.Char_AngelOfDeath.Exit(self.V.Place_City.EastEnd)
        self.V.Display.FadeOut()
        self.V.Set.EnableInput()

    def SC_Task10_Exit_BlueHouse(self):
        self.V.Set.DisableInput()
        self.V.Char_Bob.Exit(self.V.Place_City.BlueHouseDoor, False)
        self.V.Display.FadeOut()
        Dun = Activity_Dungeon(self.V)
        Dun.start()
        status = Dun.UC_Select_Task()
        self.V.Set.CameraFocus(self.V.Place_City.BlueHouseDoor)

        self.V.Display.FadeIn()
        self.V.Char_Bob.Enter(self.V.Place_City.BlueHouseDoor, False)
        self.V.Char_AngelOfDeath.Enter(self.V.Place_City.BlueHouseDoor)

        self.V.Set.CameraMode('track')
        self.V.Set.CameraFocus(self.V.Char_Bob.Name)
        self.V.Char_Bob.Exit(self.V.Place_City.EastEnd, False)
        self.V.Char_AngelOfDeath.Exit(self.V.Place_City.EastEnd)
        self.V.Display.FadeOut()
        self.V.Set.EnableInput()
        return "done"






'''from GlobalVariables import Variables
V=Variables()
c= City(V)
c.start()
c.UC_Select_Task()
'''

















##create place city
#create characters angel of death,self.Char_Tom_S,self.Char_Jim_S,self.Char_Jack
#  self.Char_Bob = V.Char_Bob
#icons: talk, fight(enable these on three characters), spellbook, knowledge , courage and hint(enable on fountain)
