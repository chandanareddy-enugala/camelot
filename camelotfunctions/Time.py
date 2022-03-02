# Importing user defined functions
# ----------------------------------
from Functions.Actions import Actions


class Time:
    def __init__(self):
        self.action = Actions()
    def Wait(self, duration):
        command = f"Wait({duration})"
        self.action.run_command(command, True)
