
class SoundEffect_:
    def __init__(self, sound, music, action):
        self.Action = action
        self.Name = sound["Name"]
        self.Type = sound["Type"]
        self.Music_On_Off = music

    def Play(self):
        if self.Music_On_Off == "ON":
            self.Action.Execute_Command(f"PlaySound({self.Name})")

    def Stop(self):
        if self.Music_On_Off == "ON":
            self.Action.Execute_Command(f"StopSound({self.Name})")


