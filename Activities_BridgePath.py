from Messages import Message_

class Activities_Bridge_FP_TO_CBR_:
    def __init__(self, V):
        self.V = V
        self.Status_Bridge = ""

        # -------------------------------------------------- Creating Place
        self.Place_Bridge = self.V.Place_Bridge
        TF = self.Place_Bridge.CreatePlace()
        if TF!=True:
            self.V.Display.Menu_Quit()

        # -------------------------------------------------- Characters
        self.Char_Bob = self.V.Char_Bob

        # -------------------------------------------------- Sounds
        self.SEffect_Danger1 = self.V.SEffect_Danger1

        # -------------------------------------------------- Camera Settings
        TF = self.V.Display.FadeOut()
        TF = self.V.Set.CameraFocus(self.Place_Bridge.SouthEnd)
        TF = self.V.Set.CameraMode('track')
        TF = self.V.Set.CameraBlend(4)
        self.Status_Bridge = " --> Bridge_Setup "

    def SC_Start(self):
        TF = self.V.Set.DisableInput()
        TF = self.V.Display.FadeIn()
        TF = self.SEffect_Danger1.Play()
        TF = self.Char_Bob.Enter(self.Place_Bridge.SouthEnd)
        TF = self.V.Set.CameraFocus(self.Char_Bob.Name)
        TF = self.Char_Bob.Face(self.Place_Bridge.NorthSign)

        TF = self.Char_Bob.WalkTo(self.Place_Bridge.WestEnd)
        TF = self.Char_Bob.WalkTo(self.Place_Bridge.Flowers)
        _ = Message_(["Wow such a beautiful Flower. I will take it for my Love. She will be Happy. "], self.V.Action).ShowNarration()

        TF = self.Char_Bob.WalkTo(self.Place_Bridge.NorthEnd)
        TF = self.V.Display.FadeOut()
        TF = self.SEffect_Danger1.Stop()
        TF = self.V.Set.EnableInput()
        self.Status_Bride = self.Status_Bridge + " --> Bridge Crossed "
        return self.Status_Bride



'''
# This code is used for testing the commands in this file
# --------------------------------------------------------
from GlobalVariables import Variables
V = Variables()
ABFC = Activities_Bridge_FP_TO_CBR_(V)
S = ABFC.SC_Task01_Start()
print(S)'''
