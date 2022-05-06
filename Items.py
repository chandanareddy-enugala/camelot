
class Item_:
    # Defining Characteristics of Item
    # ============================================================================
    def __init__(self, item, action):
        self.Action = action

        # item = {"Name", "Type", "Position"}
        self.Name   = item["Name"]
        self.Type   = item["Type"]
        self.Role   = item["Role"]

    # Creating an Item
    # ============================================================================
    def CreateItem(self):
        TF = self.Action.Execute_Command(f'CreateItem({self.Name}, {self.Type})', True)
        if TF == False:
            self.Action.Execute_Command("Quit()")
        return True

