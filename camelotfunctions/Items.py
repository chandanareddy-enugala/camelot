# Importing user defined functions
# ----------------------------------
from Functions.Actions import Actions

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# ====================================================== ITEMS CREATION ============================================================
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
class Item:
    # Defining Characteristics of Item
    # =================================================================================================================================
    def __init__(self, item):
        # item = {"Name", "Type", "Position"}
        self.Name       = item["Name"]
        self.Type       = item["Type"]
        self.Position   = item["Position"]

        self.action = Actions()

        self.Create_Item(item)

    # Creating an Item
    # =================================================================================================================================
    def Create_Item(self, item):
        self.action.run_command('CreateItem' + '(' + item["Name"] + ', ' + item["Type"] + ')', True)
        self.Set_Position()

    # Position of a Character ---------------------------------------------------------------------------------------------------
    def Set_Position(self, Position="None"):
        Name = self.Name
        if Position == "None":
            Position = self.Position

        self.action.run_command('SetPosition(' + Name + ', ' + Position + ')')