
class Set_:
    def __init__(self, action):
        self.Action = action

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Camera Setting
    def CameraFocus(self, object):
        TF = self.Action.Execute_Command(f"SetCameraFocus({object})", True)
        return TF
    def CameraMode(self, mode):
        TF = self.Action.Execute_Command(f"SetCameraMode({mode})", True)
        return TF
    def CameraBlend(self, n):
        TF = self.Action.Execute_Command(f"SetCameraBlend({n})", True)
        return TF

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Enable | Disable Input
    def EnableInput(self):
        TF = self.Action.Execute_Command(f"EnableInput()", True)
        return TF
    def DisableInput(self):
        TF = self.Action.Execute_Command(f"DisableInput()", True)
        return TF

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Wait | Poistion
    def Wait(self, n):
        TF = self.Action.Execute_Command(f'Wait({n})', True)
        return True
    def Position(self, Object, Place):
        TF = self.Action.Execute_Command(f"SetPosition({Object}, {Place})", True)
        return TF
