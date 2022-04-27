class CrossRoads:
    def __init__(self,V):
        self.V = V
        # create a place Castlecrossroads
        self.V.Place_CastleCrossroads.CreatePlace()
        #self.Char_AngelOfDeath = V.Char_AngelOfDeath
        #setposition of angelofdeath
        self.V.Char_Jim_S.CreateCharacter()
        self.V.Set.Position(self.V.Char_Jim_S.Name, self.V.Place_CastleCrossroads.Gate)

    def start(self):
        self.V.Set.CameraFocus(self.V.Place_CastleCrossroads.WestEnd)
        self.V.Set.CameraMode('track')  # ask diff of mode and placement in init and in this
        self.V.Set.CameraBlend(2)
        self.V.Display.FadeIn()

        # Bob enters castelcrossroads
        self.V.Char_Bob.Enter(self.V.Place_CastleCrossroads.WestEnd, False)
        self.V.Char_AngelOfDeath.Enter(self.V.Place_CastleCrossroads.WestEnd)
        self.V.Set.CameraFocus(self.V.Char_Bob.Name)
        self.V.Set.CameraFocus(self.V.Char_AngelOfDeath.Name)
        self.V.Char_Bob.WalkTo(self.V.Place_CastleCrossroads.Gate,False)
        self.V.Char_AngelOfDeath.WalkTo(self.V.Place_CastleCrossroads.Gate)
        self.V.Char_AngelOfDeath.Cast(self.V.Char_Jim_S.Name)
        self.V.Char_Jim_S.Die()
        self.V.Set.CameraMode('follow')

'''from GlobalVariables import Variables
V=Variables()
cr=CrossRoads(V)
cr.start()'''



