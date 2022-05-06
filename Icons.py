
class Icon_:
    def __init__(self, icon, action):
        self.Action = action

        self.ActionName = icon["ActionName"]            # Name of the Action for Output when we select icon
        self.DisplayIcon = icon["DisplayIcon"]          # Icon Type to Display
        self.DisplayName = icon["DisplayName"]          # Name to Display
        self.Description = icon["Description"]          # Purpose of the icon
        self.Default = False

    def EnableIcon(self, Object, Default=False):
        self.Default = Default
        command = f"EnableIcon('{self.ActionName}', {self.DisplayIcon}, {Object}, '{self.DisplayName}', {self.Description}, {self.Default})"
        TF = self.Action.Execute_Command(command, True)
        return True
    def DisableIcon(self, Object):
        TF = self.Action.Execute_Command(f"DisableIcon('{self.ActionName}', {Object})", True)
        return True
