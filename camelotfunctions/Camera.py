
from Functions.Actions import Actions

class Camera:
    def __init__(self):
        self.action = Actions()

    def Blend(self, time):
        command = f"SetCameraBlend({time})"
        self.action.run_command(command, True)

    def Mode(self, mode):
        command = f"SetCameraMode({mode})"
        self.action.run_command(command, True)
    def Focus(self, object):
        command = f'SetCameraFocus({object})'
        self.action.run_command(command, False)

    def Set(self, Object, Position="follow", TrasitTime='0'):
        # Object = ObjectName <Any Character, Item, Position of Place>
        # TrasitTime = Blend Number <Any Positive real number>
        # Position = Mode (follow, focus, track)
        self.Blend(TrasitTime)
        self.Focus(Object)
        self.Mode(Position)