
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# ======================================================== ForestPath  ================================================
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
class ForestPath_:
    # Defining Characteristics of Place ====================================
    def __init__(self, place, action):
        self.Action = action

        self.Name = place["Name"]
        self.Type = place["Type"]

        self.EastEnd = f"{self.Name}.EastEnd"
        self.Well = f"{self.Name}.Well"
        self.Plant = f"{self.Name}.Plant"
        self.DirtPile = F"{self.Name}.DirtPile"
        self.PathBlock = f"{self.Name}.PathBlock"
        self.WestEnd = f"{self.Name}.WestEnd"

    # Creating a Place ======================================================
    def CreatePlace(self):
        TF = self.Action.Execute_Command('CreatePlace' + '(' + self.Name + ', ' + self.Type + ')', True)
        return TF

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# ========================================================= Bridge  ===================================================
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
class Bridge_:
    # Defining Characteristics of Place ====================================
    def __init__(self, place, action):
        self.Action = action

        self.Name = place["Name"]
        self.Type = place["Type"]

        self.NorthEnd = f"{self.Name}.NorthEnd"
        self.WestEnd = f"{self.Name}.WestEnd"
        self.Flowers = f"{self.Name}.Flowers"
        self.SouthEnd = f"{self.Name}.SouthEnd"
        self.Woods = f"{self.Name}.Woods"
        self.SouthSign = f"{self.Name}.SouthSign"
        self.WestSign = f"{self.Name}.WestSign"
        self.NorthSign = f"{self.Name}.NorthSign"

    # Creating a Place =====================================================
    def CreatePlace(self):
        TF = self.Action.Execute_Command('CreatePlace' + '(' + self.Name + ', ' + self.Type + ')', True)
        return TF
    
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# ====================================================== CastleBedroom  ==============================================
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
class CastleBedroom_:
    # Defining Characteristics of Place ====================================
    def __init__(self, place, action):
        self.Action = action

        self.Name = place["Name"] # BobHouse
        self.Type = place["Type"]
        self.Door = f"{self.Name}.Door" # BobHouse.Door
        self.Chest = f"{self.Name}.Chest"
        self.Couch = f"{self.Name}.Couch"
        self.Couch_Left = f"{self.Name}.Couch.Left"
        self.Couch_Right = f"{self.Name}.Couch.Right"
        self.Couch_Middle = f"{self.Name}.Couch.Seat"
        self.Fireplace = f"{self.Name}.Fireplace"
        self.Table = f"{self.Name}.Table"
        self.Table_Left = f"{self.Name}.Table.Left"
        self.Table_Right = f"{self.Name}.Table.Right"
        self.Table_FrontLeft = f"{self.Name}.Table.FrontLeft"
        self.Table_FrontRight = f"{self.Name}.Table.FrontRight"
        self.Table_BackLeft = f"{self.Name}.Table.BackLeft"
        self.Table_BackRight = f"{self.Name}.Table.BackRight"
        self.Chair_Right = f"{self.Name}.RightChair"
        self.Chair_Left = f"{self.Name}.LeftChair"
        self.SmallTable = f"{self.Name}.SmallTable"
        self.Bed = f"{self.Name}.Bed"
        self.Bed_Left = f"{self.Name}.Bed.Left"
        self.Bed_Middle = f"{self.Name}.Bed"
        self.Bed_Right = f"{self.Name}.Bed.Right"
        self.Closet = f"{self.Name}.Closet"


    # Creating a Place ====================================================
    def CreatePlace(self):
        TF = self.Action.Execute_Command('CreatePlace' + '(' + self.Name + ', ' + self.Type + ')', True)
        return TF


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# ========================================================== City  ====================================================
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
class City_:
    # Defining Characteristics of Place ====================================
    def __init__(self, place, action):
        self.Action = action

        self.Name = place["Name"] # BobHouse
        self.Type = place["Type"]

        self.NorthEnd = f"{self.Name}.NorthEnd"
        self.GreenHouseDoor = f"{self.Name}.GreenHouseDoor"
        self.Bench = f"{self.Name}.Bench"
        self.Bench_Left = f"{self.Name}.Bench.Left"
        self.Bench_Right = F"{self.Name}.Bench.Right"
        self.Fountain = f"{self.Name}.Fountain"
        self.EastEnd = f"{self.Name}.EastEnd"
        self.BrownHouseDoor = f"{self.Name}.BrownHouseDoor"
        self.RedHouseDoor = f"{self.Name}.RedHouseDoor"
        self.BlueHouseDoor = f"{self.Name}.BlueHouseDoor"
        self.Barrel = f"{self.Name}.Barrel"
        self.Horse = f"{self.Name}.Horse"
        self.WestEnd = f"{self.Name}.WestEnd"
        self.Plant = f"{self.Name}.Plant"
        self.Alley = f"{self.Name}.Alley"
        self.Alley2 = f"{self.Name}.Alley2"

    # Creating a Place ====================================================
    def CreatePlace(self):
        TF = self.Action.Execute_Command('CreatePlace' + '(' + self.Name + ', ' + self.Type + ')', True)
        return TF

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# ========================================================== Dungeon  ====================================================
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
class Dungeon_:
    # Defining Characteristics of Place ====================================
    def __init__(self, place, action):
        self.Action = action

        self.Name = place["Name"]
        self.Type = place["Type"]

        self.Door = f"{self.Name}.Door"
        self.Chest = f"{self.Name}.Chest"
        self.Table = f"{self.Name}.Table"
        self.Table_Left = f"{self.Name}.Table.Left"
        self.Table_Right = F"{self.Name}.Table.Right"

        self.Table_FrontLeft = F"{self.Name}.Table.FrontLeft"
        self.Table_BackLeft = F"{self.Name}.Table.BackLeft"
        self.Table_FrontRight = F"{self.Name}.Table.FrontRight"
        self.Table_BackRight = F"{self.Name}.Table.BackRight"

        self.Chair = f"{self.Name}.Chair"
        self.Bookshelf_Left = f"{self.Name}.Bookshelf.Left"
        self.Bookshelf_Right = f"{self.Name}.Bookshelf.Right"
        self.CellDoor = f"{self.Name}.CellDoor"
        self.CellDoor_Inside = f"{self.Name}.CellDoor.Inside"
        self.RoundTable = f"{self.Name}.RoundTable"
        self.BlueHouseDoor = f"{self.Name}.BlueHouseDoor"
        self.DirtPile = f"{self.Name}.DirtPile"
        self.Bed = f"{self.Name}.Bed"

    # Creating a Place ====================================================
    def CreatePlace(self):
        TF = self.Action.Execute_Command('CreatePlace' + '(' + self.Name + ', ' + self.Type + ')', True)
        return TF

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# ================================================  CastleCrossRoads  =================================================
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
class CastleCrossroads_:
    # Defining Characteristics of Place ====================================
    def __init__(self, place, action):
        self.Action = action

        self.Name = place["Name"]
        self.Type = place["Type"]
        self.Gate = f"{self.Name}.Gate"
        self.WestEnd = f"{self.Name}.WestEnd"
        self.Right = f"{self.Name}.Right"
        self.Left = f"{self.Name}.Left"
        self.EastEnd = f"{self.Name}.EastEnd"
        self.Gate = f"{self.Name}.Gate"
        self.WestSign = f"{self.Name}.WestSign"
        self.EastSign = f"{self.Name}.EastSign"

    # Creating a Place ====================================================
    def CreatePlace(self):
        TF = self.Action.Execute_Command('CreatePlace' + '(' + self.Name + ', ' + self.Type + ')', True)
        return TF


class Ruins_:
    # Defining Characteristics of Place ====================================
    def __init__(self, place, action):
        self.Action = action

        self.Name = place["Name"]
        self.Type = place["Type"]
        self.Exit = f"{self.Name}.Exit"
        self.DirtPile = f"{self.Name}.DirtPile"
        self.Plant = f"{self.Name}.Plant"
        self.Altar = f"{self.Name}.Altar"
        self.Throne = f"{self.Name}.Throne"
        self.Chest = f"{self.Name}.Chest"
        self.Altar_Behind = f"{self.Name}.Altar.Behind"

    # Creating a Place ====================================================
    def CreatePlace(self):
        TF = self.Action.Execute_Command('CreatePlace' + '(' + self.Name + ', ' + self.Type + ')', True)
        if TF == False:
            self.Action.Execute_Command("Quit()")
        return TF
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# ================================================  FARM  =================================================
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
class Farm_:
    # Defining Characteristics of Place ====================================
    def __init__(self, place, action):
        self.Action = action

        self.Name = place["Name"]
        self.Type = place["Type"]
        self.Exit = f"{self.Name}.Exit"
        self.Horse = f"{self.Name}.Horse"
        self.Anvil = f"{self.Name}.Anvil"
        self.Door = f"{self.Name}.Door"
        self.Well = f"{self.Name}.Well"

    # Creating a Place ====================================================
    def CreatePlace(self):
        TF = self.Action.Execute_Command('CreatePlace' + '(' + self.Name + ', ' + self.Type + ')', True)
        return TF

