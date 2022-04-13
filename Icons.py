
class Icon_:
    def __init__(self, icon, action):
        self.Action = action

        self.ActionName = icon["ActionName"]            # Name of the Action for Output when we select icon
        self.DisplayIcon = icon["DisplayIcon"]          # Icon Type to Display
        self.EnableObject = ""                          # Icon is enabled on this Object
        self.DisplayName = icon["DisplayName"]          # Name to Display
        self.Description = icon["Description"]          # Purpose of the icon
        self.Default = False

    def EnableIcon(self, EnableObject, Default=False):
        self.EnableObject = EnableObject
        self.Default = Default
        command = f"EnableIcon('{self.ActionName}', {self.DisplayIcon}, {self.EnableObject}, '{self.DisplayName}', {self.Description}, {self.Default})"
        TF = self.Action.Execute_Command(command, True)
        return True
    def DisableIcon(self):
        TF = self.Action.Execute_Command(f"DisableIcon('{self.ActionName}', {self.EnableObject})", True)
        return True
