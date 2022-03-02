from Functions.Actions import Actions
from Functions.GlobalVariables import Variables
from Functions.Characters import Character
from Functions.Places import Place
from Functions.Items import Item
from Functions.Display import Display
from Functions.Camera import Camera
from Functions.Sounds import Sound
from Functions.Time import Time

action = Actions()
var = Variables()
display = Display()
camera = Camera()
sound = Sound()
time = Time()

# CREATING PLACES
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
BobsHouse = Place(var.places["BobsHouse"])
ForestPath = Place(var.places["ForestPath"])

# CREATING CHARACTERS
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Bob_charstics = var.characters['Bob']
# Bob = Character(Bob_charstics)
Bob = Character(var.characters['Bob'])
Angel = Character(var.characters['Angel'])

# CREATING ITEMS
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
BluePotion = Item(var.items["BluePotion"])
RedPotion = Item(var.items["RedPotion"])

# ===============================================================================================
# ===============================================================================================
# ===============================================================================================

action.run_command('EnableIcon("Open_Door", Open, BobsHouse.Door, "Leave the house", true)')
action.run_command('ShowMenu()')
# Respond to input.
while (True):
    i = input()
    if (i == 'input Selected Start'):
        camera.Set("BobsHouse.Door", "focus", "1") # Parameters: (Object, TimeDuration,
        action.run_command('HideMenu()')
        Bob.Enter("BobsHouse.Door", "true")
        camera.Set(Bob.Name, "follow", "1")  # Parameters: (Object, TimeDuration,
        action.run_command('EnableInput()', True)

    elif (i == 'input Open_Door BobsHouse.Door'):
        # time.Wait(1)
        action.run_command('DisableInput()', True)
        Bob.Exit('BobsHouse.Door', 'true')
        Bob.Enter('ForestPath.EastEnd', 'true')
        Bob.Face('ForestPath.Well')
        # Camera.Set(Bob.Name, 'track', '1')
        Bob.WalkTo("ForestPath.Well")
        Bob.Face('ForestPath.EastEnd')
        narrationMessage = "Oh what a wonderful place it is!"
        display.ShowNarration(narrationMessage)
        action.run_command('EnableInput()', True)

    elif (i == 'input Close Narration'):
        # sound.Stop("Peaceful", "ForestPath.EastEnd")
        display.HideNarration()
        action.run_command('DisableInput()', True)
        action.run_command(f"SetCameraMode(track)")
        action.run_command(f"SetCameraFocus(ForestPath.WestEnd)")
        Angel.Enter('ForestPath.WestEnd', 'true')
        action.run_command(f"SetCameraFocus({Angel.Name})")
        action.run_command(f"SetCameraMode(follow)")
        action.run_command(f"SetCameraFocus({Angel.Name})")
        # Camera.Set(Angel.Name, 'focus', '1')
        Angel.Clap()
        Bob.Face(Angel.Name)
        Bob.Wave()
        Bob.WalkTo(Angel.Name)

        # action.run_command("ClearList()", True)
    elif(input() == " input arrived Angel position Bob"):
        dialogs = {1: f"{Angel.Name} : Hey kid, what are you looking for?",
                   2: f"{Bob.Name} : Hi, I am seeking for someone who makes me strong enough. Can you guide me?",
                   3: f"{Angel.Name} : Sure kid. This is a magical forest, anything is possible. Only the luckiest can come here.",
                   4: f"{Bob.Name} : Oh Wowwww, That's Great",
                   5: f"{Angel.Name} : I have a task for you. Select one from the below potions.",
                   6: f"[Red|Red] <||> [Blue|Blue] <||> [Reject|Reject]"    # Red is for Poison, Blue is for Wealth
                   }
        display.ShowDialog(dialogs)
        action.run_command('EnableInput()', True)

    elif (i == 'input Selected Blue'):
        display.HideDialog()
        action.run_command('DisableInput()', True)
        sound.Play("DarkMagic")
        Angel.Give(BluePotion.Name, Bob.Name)
        Bob.Drink()

        dialogs = {1: f"{Angel.Name} : Wise choice kid. You have gained full of required knowledge for entire your life and you live forever. Go home and sleep well."}
        display.ShowDialog(dialogs)
        Time.Wait(5)
        display.HideDialog()

        Bob.Dance()
        sound.Play("Flute1", Angel.Name)
        Time.Wait(5)
        Bob.Exit('ForestPath.EastEnd', 'true')
        dialogs = {1: f"THE END"}
        display.ShowDialog(dialogs)
        action.run_command('EnableInput()', True)

    elif (i == 'input Selected Red'):
        display.HideDialog()
        action.run_command('DisableInput()', True)
        sound.Play("DarkMagic")
        Angel.Give(RedPotion.Name, Bob.Name)
        Bob.Drink()

        dialogs = {
            1: f"{Angel.Name} : Poor choice kid. You have lost your life."}
        display.ShowDialog(dialogs)
        Time.Wait(5)
        display.HideDialog()

        # sound.Play("Death2", Angel.Name)
        Bob.Die()
        # sound.Play("EvilLaugh1", Angel.Name)
        ############## Camera.Set(Angel.Name, 'track', '1')
        Angel.Exit('ForestPath.WestEnd', 'true')

        dialogs = {1: f"THE END"}
        display.ShowDialog(dialogs)
        action.run_command('EnableInput()', True)

    elif (i == 'input Selected Reject'):
        display.HideDialog()
        action.run_command('DisableInput()', True)
        dialogs = {
            1: f"{Angel.Name} : You don’t have courage. You run home."}
        display.ShowDialog(dialogs)
        Time.Wait(5)
        display.HideDialog()
        Bob.Exit('ForestPath.EastEnd', 'true')
        dialogs = {1: f"THE END"}
        display.ShowDialog(dialogs)
        action.run_command('EnableInput()', True)


