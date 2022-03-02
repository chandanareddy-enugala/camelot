# Importing user defined functions
# ----------------------------------
from Functions.Actions import Actions

class Display:
    def __init__(self):
        self.action = Actions()
        pass
    def ShowNarration(self, narration):
        self.action.run_command(f'SetNarration({narration})', True)
        self.action.run_command('ShowNarration()')
    def ShowDialog(self, dialogs):
        self.action.run_command('ShowDialog()')
        for key in dialogs.keys():
            self.action.run_command(f"SetDialog({dialogs[key]})", True)
    def HideNarration(self):
        self.action.run_command('HideNarration()')
    def HideDialog(self):
        self.action.run_command('HideDialog()')
