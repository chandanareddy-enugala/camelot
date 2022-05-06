
class VisualEffect_:
    def __init__(self, effect, action):
        self.Action = action
        self.Name = effect["Name"]
        self.Type = effect["Type"]
        self.TargetObjectName = ""

    def CreateEffect(self, TargetObjectName):
        self.TargetObjectName = TargetObjectName
        self.Action.Execute_Command(f"CreateEffect({TargetObjectName}, {self.Name})")
        return True

    def EnableEffect(self):
        self.Action.Execute_Command(f"EnableEffect({self.TargetObjectName}, {self.Name})")
        return True

    def DisableEffect(self):
        self.Action.Execute_Command(f"DisableEffect({self.TargetObjectName}, {self.Name})")
        return True

