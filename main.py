
# from Stories.Level_One import Level_1
from Level_One import Level_1
from Level_Two import Level_2
#from Base_Structures1 import Entities_ClassObjects
from GlobalVariables import Variables

V = Variables()

# Start Level 1 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
L1 = Level_1()
Level_1_Status = L1.StartGame()


'''if Level_One_Status != "":
    L2 = Level_Two(action)
    Level_Two_Status = L2.Start()
else:
    display.Quit()'''

print("|-----------------* THE END *-----------------|")

# Home Functionalities
# ==================================
# Create a place "BobsHouse"
# Create two Characters "Bob" and "BobWife"
# Set up Home (If any objects whats to be placed in this home)
# Set BobWife on bed - Sleeping
# Set Bob standing near bed at Home
# Set Camera Position - tacking mode
# Bob Kneels and cries
# Set Camera Focus to Bob
# Set Dialogues
# Exit from Home through Door