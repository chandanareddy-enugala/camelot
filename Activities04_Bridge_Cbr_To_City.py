from Messages import Message_

class Activities_Bridge_Cbr_To_City_:
    def __init__(self, V):
        self.V = V
        self.Status_Bridge = ""

        # -------------------------------------------------- Creating Place
        self.Place_Bridge = self.V.Place_Bridge
        # -------------------------------------------------- Characters
        self.Char_Bob = self.V.Char_Bob
        # -------------------------------------------------- Sounds
        self.SEffect_Danger1 = self.V.SEffect_Danger1
        # -------------------------------------------------- Camera Settings
        TF = self.V.Display.FadeOut()
        TF = self.V.Set.CameraFocus(self.Place_Bridge.NorthEnd)
        TF = self.V.Set.CameraMode('track')
        TF = self.V.Set.CameraBlend(4)
        self.Status_Bridge = " --> Bridge_Setup "

    def SC_Start(self):
        TF = self.V.Set.DisableInput()
        TF = self.V.Display.FadeIn()
        TF = self.SEffect_Danger1.Play()
        TF = self.Char_Bob.Enter(self.Place_Bridge.NorthEnd)
        TF = self.V.Set.CameraFocus(self.Char_Bob.Name)
        TF = self.Char_Bob.Exit(self.Place_Bridge.SouthEnd)
        TF = self.V.Display.FadeOut()
        TF = self.SEffect_Danger1.Stop()
        TF = self.V.Set.EnableInput()
        self.Status_Bride = self.Status_Bridge + " --> Castle Cross Road Crossed "
        return self.Status_Bride



'''# This code is used for testing the commands in this file
# --------------------------------------------------------
from GlobalVariables import Variables
V = Variables()
ABFC = Activities_Bridge_Cbr_To_City_(V)
S = ABFC.SC_Start()
print(S)
'''