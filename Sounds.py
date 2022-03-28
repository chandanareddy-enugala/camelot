# Importing user defined functions
# ----------------------------------
from Functions.Actions import Actions

class Sound:
    def __init__(self):
        self.action = Actions()

    def Play(self, soundEffect, onObject, loop=False):
        command = f"PlaySound({soundEffect}, {onObject}, {loop})"
        self.action.run_command(command, True)
    def Stop(self, soundEffect, onObject):
        command = f"StopSound({soundEffect}, {onObject})"
        self.action.run_command(command, True)
