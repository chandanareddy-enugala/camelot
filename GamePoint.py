from GlobalVariables import Variables
from Activities_ForestPath import Activities_ForestPath_
from Activities_BridgePath import Activities_Bridge_FP_TO_CBR_
from Activities_CastleBedRoom import Activities_CastleBedRoom_

# Creating GlobalVariables Class object which connect to all other classes
# (like Places, Characters, Items, Icons, SoundEffects, Visual Effects, Set, Displays)
V = Variables()

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% LEVEL 01 - ForestPath
AFP = Activities_ForestPath_(V)
V.Status_EntireGame += AFP.SC_AFP_Start()
V.Status_EntireGame += AFP.UC_Task00_Select_Task()

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% LEVEL 02 - Bridge
ABFC = Activities_Bridge_FP_TO_CBR_(V)
V.Status_EntireGame += ABFC.SC_Start()

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% LEVEL 03 - Bridge

ACBR = Activities_CastleBedRoom_(V)
V.Status_EntireGame += ACBR.SC_ACBR_Start()
V.Status_EntireGame += ACBR.UC_Task00_Select_Task()

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% LEVEL 04 - City
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% LEVEL 05 - CastleCrossRoad
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% LEVEL 06 - Ruins
'''V.Display.Menu_Title_Set("To be Continued...")
V.Display.Menu_Show()
V.Display.Wait(5)
V.Display.Menu_Quit()
# print(V.Status_EntireGame)
'''


'''
# Commands:
input Selected Start
input Close Narration
Talk or ---------------- Attack
Key or input Key Pause
RedPotion or ----------- BluePotion
Key
Key
Key
Dress | Money | FirePlace | City
'''

''':cvar
Sounds used in this Game: Make sure these will be used at every same situation.
# ----------------------------------------------------------------------------
SEffect_Danger2 - Used for Man Die
SEffect_DarkMagic - Attack 
SEffect_Ominous - When Player in User Control -|- When Player talks with other
SEffect_Spooky - When Player in System Control
SEffect_Potion - Get Potion in Hand
SEffect_Spell2 - Get Secret Spell, Secret Scroll
SEffect_Error - When Unspecified happened -|- When Restricted to use

'''