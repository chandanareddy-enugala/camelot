# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# ==================================================  INVENTORY  =================================================
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
class Inventory_:
    def __init__(self, Entity, action):
        self.Action = action
        self.Entity = Entity
        self.List = {}
    def Add(self, Object, Description=""):
        self.List[Object] = {"Name": Object, "Description": Description}
        return True
    def Remove(self, Object):
        self.List.pop(Object)
        self.Action.Execute_Command(f"RemoveFromList({Object})", True)
        return True
    def Show(self):
        if len(self.List.keys())>0:
            for key in self.List.keys():
                self.Action.Execute_Command(f"AddToList({self.List[key]['Name']}, {self.List[key]['Description']})", True)
        self.Action.Execute_Command(f"ShowList({self.Entity})", True)
        return True
    def Hide(self):
        self.Action.Execute_Command(f"HideList()", True)
        self.Clear()
        return True
    def Clear(self):
        self.Action.Execute_Command(f"ClearList()", True)