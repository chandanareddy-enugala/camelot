from GlobalVariables import Variables
from Activities01_ForestPath import Activities_ForestPath_
from Activities02_Bridge_FP_TO_CBR import Activities_Bridge_FP_to_CBR_
from Activities03_CastleBedRoom import Activities_CastleBedRoom_
from Activities05_City import Activities_City_
# from Activities02_Bridge_FP_TO_CBR import Activities_Bridge_CBR_TO_City
from Activities06_Ruins import Activities_Ruins
# from Activities_CastleCrossRoad_ import Activities_CastleCrossRoad_

# Creating GlobalVariables Class object which connect to all other classes
# (like Places, Characters, Items, Icons, SoundEffects, Visual Effects, Set, Displays)

V = Variables()

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% LEVEL 01 - ForestPath
AFP = Activities_ForestPath_(V)
AFP.SC_Start()
AFP.UC_Select_Task()

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%inp%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% LEVEL 02 - Bridge_FP_to_CBR
ABFC = Activities_Bridge_FP_to_CBR_(V)
ABFC.SC_Start()
ABFC.UC_Select_Task()

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% LEVEL 03 - CBR
ACBR = Activities_CastleBedRoom_(V)
ACBR.SC_Start()
ACBR.UC_Select_Task()

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% LEVEL 04 - Bridge_CBR_to_CIty
# Bridge from CBR to City

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% LEVEL 05 - City
CBR = Activities_City_(V)
CBR.SC_Start()
CBR.UC_Select_Task()

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% LEVEL 06 - Ruins
AR = Activities_Ruins(V)
AR.SC_Start()
AR.UC_Select_Task()


'''from Game_Initialize import Setup
setup = Setup(V)
setup.Create()
V.Display.Menu_Show()'''