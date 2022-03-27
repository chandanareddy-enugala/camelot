def WaitFor(msg):
        while(True):
                received = input()
                if recevied == msg:
                        break


def action(command):
        print('start ' + command)
        while(True):
                i = input()
                if(i == 'succeeded ' + command):
                        return True
                elif(i == 'failed ' + command):
                        return False
                elif(i.startswith('error')):
                        return False
# Set up a small house with a door.
action('CreatePlace(BobsHouse, Cottage)')
action('CreateCharacter(Bob, B)')
action('SetClothing(Bob, Peasant)')
action('SetPosition(Bob, BobsHouse.Door)')

###added new character
action('CreateCharacter(Tom, A)')

action("CreatePlace(ForestPath, ForestPath)")
action('CreateCharacter(Angel, F)')
action('SetClothing(Angel, Warlock)')
action('SetPosition(Angel, ForestPath.WestEnd)')
action('PlaySound(LivelyMusic)')

action('CreateItem(BluePotion, BluePotion)')
action('SetPosition(BluePotion, Angel)')
action('Pocket(Angel, BluePotion)')

action('CreateItem(RedPotion, RedPotion)')
action('SetPosition(RedPotion, Angel)')
action('Draw(Angel, BluePotion)')

action('EnableIcon("Open_Door", Open, BobsHouse.Door, "Leave the house", true)')
action('ShowMenu()')
# Respond to input.
while(True):
        i = input()
        if(i == 'input Selected Start'):
                action('SetCameraFocus(Bob)')
                action('HideMenu()')
                action('EnableInput()')
        elif(i == 'input Open_Door BobsHouse.Door'):
                action('Exit(Bob, BobsHouse.Door, true)')
                action("Enter(Bob, ForestPath.EastEnd, true)")
                action('SetNarration("Oh what place is this! There is someone standing there. Lets ask them.")')
                action('ShowNarration()')
                #action('"WalkTo(Bob, Angel)"')
        elif(i == 'input Close Narration'):
                action('HideNarration()')
                action('WalkTo(Bob, Angel)')
                action("ClearList()")
                action('SetDialog("Bob : hey what place is it?")')
                action('SetDialog("Angel : hello bob this is a magical forest. Only the luckiest can come here.")')
                action('SetDialog("Bob : oh wow")')
                action('SetDialog("Angel : i have a task for you bob. Select one from the potions. [Red|Red] is wealth. [Blue|Blue] is knowledge.")')
                action('ShowDialog()')
        elif(i == 'input Selected Blue'):
                action('HideDialog()')
                action('Give(Angel, BluePotion, Bob)')
                action('Drink(Bob)')
                action('Die(Bob)')
                action('SetNarration("Bob drank the wrong potion and died. THE END")')
                action('ShowNarration()')
        elif(i == 'input Selected Red'):
                action('HideDialog()')
                action('Give(Angel, RedPotion, Bob)')
                action('Drink(Bob)')
                action('Dance(Bob)')
                action('SetNarration("Bob drank the right potion. Now he lives forever. THE END")')
                action('ShowNarration()')
