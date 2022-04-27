
class CbrtoCity:
    def __init__(self,V):
        self.V=V
        self.V.Display.FadeOut()
        self.V.Set.CameraFocus(self.V.Place_Bridge.NorthEnd)
        self.V.Set.CameraMode('track')
        self.V.Set.CameraBlend(2)

    def start(self):
        self.V.Display.FadeIn()
        self.V.Char_Bob.Enter(self.V.Place_Bridge.NorthEnd)
        self.V.Set.CameraFocus(self.V.Char_Bob.Name)
        self.V.Char_Bob.Exit(self.V.Place_Bridge.SouthEnd)
        self.V.Display.FadeOut()

'''from GlobalVariables import Variables
V=Variables()
'''







