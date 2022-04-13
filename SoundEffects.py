
class SoundEffect_:
    def __init__(self, sound, action):
        self.Action = action
        self.Name = sound["Name"]
        self.Type = sound["Type"]

    def Play(self):
        self.Action.Execute_Command(f"PlaySound({self.Name})")

    def Stop(self):
        self.Action.Execute_Command(f"StopSound({self.Name})")


