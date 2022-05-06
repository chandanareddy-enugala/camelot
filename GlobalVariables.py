from Actions import Actions
from Places import ForestPath_, Bridge_, CastleBedroom_, City_, CastleCrossroads_, Dungeon_, Ruins_, Farm_
from Characters import Character_
from Items import Item_
from Icons import Icon_
from VisualEffects import VisualEffect_
from Messages import Message_
from Set import Set_
from Displays import Display
from SoundEffects import SoundEffect_
from Inventory import Inventory_

class Variables:
    def __init__(self):
        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # ==========================================  Status check variables  ==========================================
        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                # Activities status which tells where player has reached and where to go
        self.Menu_Title = "|- SAVING LIFE -|"
        self.EscapeCount = 0
        self.Language = "English"
        self.Status_EntireGame = ""
        self.Status_AFP = ""            # Place: ForestPath
        self.Bob_Drink_Potion = ""
        self.Status_Bridge = ""         # Place : Bridge
        self.Status_CBR = ""            # Place: CastleBedRoom
        self.Status_City = ""           # Place: City
        self.Status_CCR = ""            # Place: CastleCrossRoad
        self.Status_Ruins = ""          # Place: Ruins
        self.SecretSpell_Angel = ""     # SecretSpell: OmBhimBhush
        self.Char_Bob_Life = 100
        self.Char_Devil_Life = 200
        self.Char_Bob_List = []
        self.Music_On_Off = "ON"

        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # ===========================================  ACTIONS, SET, DISPLAY  ==========================================
        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        self.Action = Actions()
        self.Set = Set_(self.Action)
        self.Display = Display(self.Action)

        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # ===================================================  PLACES  =================================================
        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # ------------------------------------ DICTIONARIES -----------------------------------------
        # Places Parameter : [<Name>, <Type>]
        self.places = {
            "ForestPath": {"Name": "ForestPath", "Type": "ForestPath"},
            "Bridge": {"Name": "Bridge", "Type": "Bridge"},
            "CastleBedRoom": {"Name": "CastleBedRoom", "Type": "CastleBedroom"},
            "City": {"Name": "City", "Type": "City"},
            "Dungeon": {"Name": "Dungeon", "Type": "Dungeon"},
            "CastleCrossroads": {"Name": "CrossRoad", "Type": "CastleCrossroads"},
            "Ruins": {"Name": "Ruins", "Type": "Ruins"},
            "Farm"  : {"Name": "Farm", "Type": "Farm"}
        }
        # ------------------------------------ CLASS OBJECTS -----------------------------------------
        self.Place_ForestPath       = ForestPath_(self.places["ForestPath"],                self.Action)
        self.Place_Bridge           = Bridge_(self.places['Bridge'],                        self.Action)
        self.Place_CastleBedRoom    = CastleBedroom_(self.places["CastleBedRoom"],          self.Action)
        self.Place_City             = City_(self.places["City"],                            self.Action)
        self.Place_Dungeon          = Dungeon_(self.places["Dungeon"],                      self.Action)
        self.Place_CastleCrossroads = CastleCrossroads_(self.places["CastleCrossroads"],    self.Action)
        self.Place_Ruins            = Ruins_(self.places["Ruins"],                          self.Action)
        self.Place_Farm             = Farm_(self.places["Farm"],                            self.Action)

        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # =================================================  CHARACTERS  ===============================================
        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # ------------------------------------ DICTIONARIES -----------------------------------------
        # Character Parameters : [<Name>, <BodyType>, <HairStyle>, <HairColor>, <EyeColor>, <Outfits>, <Role>]
        self.characters = {
            "Bob"         : {"Name": "Bob",          "BodyType": "B",    "SkinColor": "5",   "HairStyle": "Long",    "HairColor": "black",   "EyeColor": "black",    "Outfits": "Peasant",       "Role": "Player"},
            "Candy"       : {"Name": "Candy",        "BodyType": "A",    "SkinColor": "5",   "HairStyle": "Long",    "HairColor": "black",   "EyeColor": "black",    "Outfits": "Peasant",       "Role": "BobWife, Sick"},
            "Lilly_S"     : {"Name": "Lilly",        "BodyType": "G",    "SkinColor": "5",   "HairStyle": "Straight","HairColor": "black",   "EyeColor": "black",    "Outfits": "Merchant",      "Role": "Support character - used anywhere and Worker at BobsHouse"},
            "Amelia_S"    : {"Name": "Amelia",       "BodyType": "A",    "SkinColor": "5",   "HairStyle": "Ponytail","HairColor": "black",   "EyeColor": "black",    "Outfits": "Noble",        "Role": "Support character - Selling Flowers at Bridge"},
            "Angel"       : {"Name": "Angel",        "BodyType": "C",    "SkinColor": "5",   "HairStyle": "Long",    "HairColor": "black",   "EyeColor": "red",      "Outfits": "Witch",         "Role": "Guide persons to get power who come forest"},
            "AngelOfDeath": {"Name": "AngelOfDeath", "BodyType": "E",    "SkinColor": "5",   "HairStyle": "Long",    "HairColor": "black",   "EyeColor": "red",      "Outfits": "Priest",        "Role": "Guide persons to get power who come City"},
            "Devil"       : {"Name": "Devil",        "BodyType": "D",    "SkinColor": "5",   "HairStyle": "Musketeer_Full",    "HairColor": "black",   "EyeColor": "black",    "Outfits": "Warlock",   "Role": "Secure the Cure at Ruins"},
            "Tom_S"       : {"Name": "Tom",          "BodyType": "F",    "SkinColor": "5",   "HairStyle": "Short_Beard",    "HairColor": "black",   "EyeColor": "black",    "Outfits": "Peasant",   "Role": "Support character - used anywhere"},
            "Jim_S"       : {"Name": "Jim",          "BodyType": "D",    "SkinColor": "5",   "HairStyle": "Spiky",   "HairColor": "black",   "EyeColor": "black",    "Outfits": "HeavyArmour",   "Role": "Support character - used anywhere"},
            "Jack_S"      : {"Name": "Jack",         "BodyType": "H",    "SkinColor": "5",   "HairStyle": "Mage",    "HairColor": "black",   "EyeColor": "black",    "Outfits": "HeavyArmour",   "Role": "Support character - used anywhere"},
            "Begger_S"    : {"Name": "Begger",       "BodyType": "H",    "SkinColor": "5",   "HairStyle": "Spiky",  "HairColor": "black", "EyeColor": "black",      "Outfits": "Beggar",        "Role": "Begging"},
            "Emily_S"     : {"Name": "Emily",        "BodyType": "G",    "SkinColor": "5",   "HairStyle": "Straight","HairColor": "black", "EyeColor": "black",     "Outfits": "Merchant",      "Role": "Support character - used anywhere and Worker at BobsHouse"},
            "Priest"      : {"Name": "Priest",       "BodyType": "H",    "SkinColor": "5",   "HairStyle": "Spiky",   "HairColor": "black", "EyeColor": "black",      "Outfits": "Priest",        "Role": "Help people"}


        }
        # ------------------------------------ CLASS OBJECTS -----------------------------------------
        self.Char_Bob       = Character_(self.characters["Bob"],        self.Action)
        self.Char_Candy     = Character_(self.characters["Candy"],      self.Action)
        self.Char_Lilly_S   = Character_(self.characters["Lilly_S"],    self.Action)
        self.Char_Amelia_S  = Character_(self.characters["Amelia_S"],   self.Action)
        self.Char_Angel     = Character_(self.characters["Angel"],      self.Action)
        self.Char_AngelOfDeath = Character_(self.characters["AngelOfDeath"], self.Action)
        self.Char_Devil     = Character_(self.characters["Devil"],      self.Action)
        self.Char_Tom_S     = Character_(self.characters["Tom_S"],      self.Action)
        self.Char_Jim_S     = Character_(self.characters["Jim_S"],      self.Action)
        self.Char_Jack_S    = Character_(self.characters["Jack_S"],     self.Action)
        self.Char_Begger_S  = Character_(self.characters["Begger_S"],   self.Action)
        self.Char_Emily_S   = Character_(self.characters["Emily_S"],   self.Action)
        self.Char_Devil     = Character_(self.characters["Devil"],      self.Action)
        self.Char_Priest    = Character_(self.characters["Priest"],     self.Action)



        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # =================================================  ITEMS  ===============================================
        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # ------------------------------------ DICTIONARIES -----------------------------------------
        # Item Parameters : [<Name>, <Type>]
        self.items = {
            "BlueBook"      : {"Name": "BlueBook",      "Type": "BlueBook",     "Role": "To Distract Player"},
            "RedBook"       : {"Name": "RedBook",       "Type": "RedBook",      "Role": "To Distract Player"},
            "GreenBook"     : {"Name": "GreenBook",     "Type": "GreenBook",    "Role": "To Distract Player"},
            "PurpleBook"    : {"Name": "PurpleBook",    "Type": "PurpleBook",   "Role": "Used for Game Instructions"},
            "EvilBook"      : {"Name": "EvilBook",      "Type": "EvilBook",     "Role": "Choose right word of it"},
            "SpellBook"     : {"Name": "SpellBook",     "Type": "SpellBook",    "Role": ""},

            "BluePotion"    : {"Name": "BluePotion",    "Type": "BluePotion",   "Role": "Angel"},
            "RedPotion"     : {"Name": "RedPotion",     "Type": "RedPotion",    "Role": "Angel"},
            "GreenPotion"   : {"Name": "GreenPotion",     "Type": "GreenPotion",  "Role": "Angel"},
            "PurplePotion"  : {"Name": "PurplePotion",  "Type": "PurplePotion", "Role": "Angel"},

            "BlueKey"       : {"Name": "BlueKey",       "Type": "BlueKey",      "Role": ""},
            "RedKey"        : {"Name": "RedKey",        "Type": "RedKey",       "Role": ""},
            "GreenKey"      : {"Name": "GreenKey",      "Type": "GreenKey",     "Role": ""},
            "PurpleKey"     : {"Name": "PurpleKey",     "Type": "PurpleKey",    "Role": ""},
            "JewelKey"      : {"Name": "JewelKey",      "Type": "JewelKey",     "Role": ""},
            "ChestKey"      : {"Name": "ChestKey",      "Type": "BlueKey",      "Role": "SmallTable"},

            "CloseScroll"   : {"Name": "CloseScroll",   "Type": "Scroll",       "Role": "Closet"},
            "OpenScroll"    : {"Name": "OpenScroll",    "Type": "OpenScroll",   "Role": "Table"},

            "UnLitTorch"    : {"Name": "UnLitTorch",    "Type": "Torch",        "Role": "Used in Night"},
            "LitTorch"      : {"Name": "LitTorch",      "Type": "LitTorch",     "Role": "Used in Night"},

            "BobSword"      : {"Name": "BobSword",      "Type": "Sword",        "Role": "Angel"},
            "DevilSword"    : {"Name": "DevilSword",    "Type": "Sword",        "Role": "Devil"},

            "BlueCloth"     : {"Name": "BlueCloth",     "Type": "BlueCloth",    "Role": ""},
            "RedCloth"      : {"Name": "RedCloth",      "Type": "RedCloth",     "Role": ""},
            "PurpleCloth"   : {"Name": "PurpleCloth",   "Type": "PurpleCloth",  "Role": ""},
            "Rags"          : {"Name": "Rags",          "Type": "Rags",         "Role": ""},

            "Bottle"        : {"Name": "Bottle",        "Type": "Bottle",       "Role": "Drink or Blast"},
            "Coin"          : {"Name": "Coin",          "Type": "Coin",         "Role": "Used for Money"},
            "Hammer"        : {"Name": "Hammer",        "Type": "Hammer",       "Role": "Used for Break things"},
            "Compass"       : {"Name": "Compass",       "Type": "Compass",      "Role": "Used for Directions"},
            "Help"          : {"Name": "Help",          "Type": "InkandQuill",  "Role": "Used for Help"}
        }
        # ------------------------------------ CLASS OBJECTS -----------------------------------------
        self.Item_BlueBook = Item_(self.items["BlueBook"], self.Action)
        self.Item_RedBook = Item_(self.items["RedBook"], self.Action)
        self.Item_GreenBook = Item_(self.items["GreenBook"], self.Action)
        self.Item_PurpleBook = Item_(self.items["PurpleBook"], self.Action)
        self.Item_EvilBook = Item_(self.items["EvilBook"], self.Action)
        self.Item_SpellBook = Item_(self.items["SpellBook"], self.Action)

        self.Item_BluePotion = Item_(self.items["BluePotion"], self.Action)
        self.Item_RedPotion = Item_(self.items["RedPotion"], self.Action)
        self.Item_GreenPotion = Item_(self.items["GreenPotion"], self.Action)
        self.Item_PurplePotion = Item_(self.items["PurplePotion"], self.Action)

        self.Item_BlueKey = Item_(self.items["BlueKey"], self.Action)
        self.Item_RedKey = Item_(self.items["RedKey"], self.Action)
        self.Item_GreenKey = Item_(self.items["GreenKey"], self.Action)
        self.Item_PurpleKey = Item_(self.items["PurpleKey"], self.Action)
        self.Item_JewelKey = Item_(self.items["JewelKey"], self.Action)
        self.Item_ChestKey      = Item_(self.items["ChestKey"],     self.Action)

        self.Item_CloseScroll = Item_(self.items["CloseScroll"], self.Action)
        self.Item_OpenScroll = Item_(self.items["OpenScroll"], self.Action)

        self.Item_UnLitTorch = Item_(self.items["UnLitTorch"], self.Action)
        self.Item_LitTorch = Item_(self.items["LitTorch"], self.Action)

        self.Item_BobSword      = Item_(self.items["BobSword"],     self.Action)
        self.Item_DevilSword    = Item_(self.items["DevilSword"],   self.Action)

        self.Item_BlueCloth    = Item_(self.items["BlueCloth"],   self.Action)
        self.Item_RedCloth = Item_(self.items["RedCloth"], self.Action)
        self.Item_PurpleCloth = Item_(self.items["PurpleCloth"], self.Action)
        self.Item_Rags = Item_(self.items["Rags"], self.Action)

        self.Item_Hammer = Item_(self.items["Hammer"], self.Action)
        self.Item_Bottle = Item_(self.items["Bottle"], self.Action)


        self.Item_Coin          = Item_(self.items["Coin"],         self.Action)
        self.Item_Compass       = Item_(self.items["Compass"],      self.Action)
        self.Item_Help          = Item_(self.items["Help"],         self.Action)

        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # ====================================================  ICONS  =================================================
        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # ------------------------------------ DICTIONARIES -----------------------------------------
        self.icons = {
            "Give": {"ActionName": "Select Icon Give", "DisplayIcon": "hand", "DisplayName": "Give", "Description": "Used to Give Entity"},
            "Take"     : {"ActionName": "Select Icon Take", "DisplayIcon": "hand", "DisplayName": "Take", "Description": "Used to Take Entity"},
            "Drink"     : {"ActionName": "Select Icon Drink", "DisplayIcon": "drink", "DisplayName": "Drink", "Description": "Drink liquid in hand"},
            "Attack"    : {"ActionName": "Select Icon Attack", "DisplayIcon": "first", "DisplayName": "Attack", "Description": "Attack"},
            "Talk"      : {"ActionName": "Select Icon Talk", "DisplayIcon": "talk", "DisplayName": "Talk", "Description": "Talk"},
            "Dress"     : {"ActionName": "Select Icon Dress", "DisplayIcon": "dress", "DisplayName": "Dress", "Description": "Changing Dress"},
            "Money"     : {"ActionName": "Select Icon Money", "DisplayIcon": "coins", "DisplayName": "Money", "Description": "Take Money"},
            "GiveMoney": {"ActionName": "Select Icon GiveMoney", "DisplayIcon": "coins", "DisplayName": "GiveMoney", "Description": "Take Money"},
            "TakeMoney": {"ActionName": "Select Icon TakeMoney", "DisplayIcon": "coins", "DisplayName": "TakeMoney", "Description": "Take Money"},
            "Pick": {"ActionName": "Select Icon PickObject", "DisplayIcon": "hand", "DisplayName": "Pick", "Description": "Pick Object"},
            "CloseScroll": {"ActionName": "Select Icon  CloseScroll", "DisplayIcon": "scroll", "DisplayName": "CloseScroll", "Description": "Closed Scroll used for directions"},
            "OpenScroll": {"ActionName": "Select Icon  OpenScroll", "DisplayIcon": "openscroll", "DisplayName": "OpenScroll", "Description": "Closed Scroll to read matter"},
            "Woods": {"ActionName": "Select Icon Woods", "DisplayIcon": "woodpile", "DisplayName": "Woods", "Description": "Select Icon ing Woods"},
            "Health": {"ActionName": "Select Icon HealingPotion", "DisplayIcon": "healingpotion", "DisplayName": "Health", "Description": "Used for Increase Health"},
            "Apple": {"ActionName": "Select Icon  Apple", "DisplayIcon": "apple", "DisplayName": "Apple", "Description": "Select Icon ing Apple"},
            "Book": {"ActionName": "Select Icon  Book", "DisplayIcon": "book", "DisplayName": "Book", "Description": "Select Icon  Book"},
            "EvilBook": {"ActionName": "Select Icon EvilBook", "DisplayIcon": "evilbook", "DisplayName": "EvilBook", "Description": "Select Icon ed for Danger"},
            "BlueBook": {"ActionName": "Select Icon BlueBook", "DisplayIcon": "book", "DisplayName": "BlueBook", "Description": "Select Icon  BlueBook"},
            "RedBook": {"ActionName": "Select Icon RedBook", "DisplayIcon": "book", "DisplayName": "RedBook", "Description": "Select Icon  RedBook"},
            "GreenBook": {"ActionName": "Select Icon GreenBook", "DisplayIcon": "book", "DisplayName": "GreenBook", "Description": "Select Icon  GreenBook"},
            "PurpleBook": {"ActionName": "Select Icon PurpleBook", "DisplayIcon": "book", "DisplayName": "PurpleBook", "Description": "Select Icon  PurpleBook"},
            "SpellBook": {"ActionName": "Select Icon SpellBook", "DisplayIcon": "book", "DisplayName": "SpellBook", "Description": "Select Icon  SpellBook"},

            "Key": {"ActionName": "Select Icon  Key", "DisplayIcon": "key", "DisplayName": "Key", "Description": "Select Icon  BlueKey"},
            "BlueKey": {"ActionName": "Select Icon BlueKey", "DisplayIcon": "key", "DisplayName": "BlueKey", "Description": "Select Icon  BlueKey"},
            "RedKey": {"ActionName": "Select Icon Key", "DisplayIcon": "key", "DisplayName": "RedKey", "Description": "Select Icon  RedKey"},
            "GreenKey": {"ActionName": "Select Icon Key", "DisplayIcon": "key", "DisplayName": "GreenKey", "Description": "Select Icon  GreenKey"},
            "PurpleKey": {"ActionName": "Select Icon Key", "DisplayIcon": "key", "DisplayName": "PurpleKey", "Description": "Select Icon  PurpleKey"},
            "JewelKey": {"ActionName": "Select Icon JewelKey", "DisplayIcon": "key", "DisplayName": "JewelKey", "Description": "Select Icon  JewelKey"},

            "LovePotion": {"ActionName": "Select Icon Love", "DisplayIcon": "lovepotion", "DisplayName": "Love", "Description": "Expressing Love"},
            "Poison": {"ActionName": "Select Icon Poison", "DisplayIcon": "poison", "DisplayName": "Poison", "Description": "Select Icon ed for Danger"},

            "Potion": {"ActionName": "Select Icon Potion", "DisplayIcon": "potion", "DisplayName": "Potion", "Description": "Select Icon  Potion"},
            "BluePotion": {"ActionName": "Select Icon BluePotion", "DisplayIcon": "potion", "DisplayName": "BluePotion", "Description": "Select Icon  BluePotion"},
            "RedPotion": {"ActionName": "Select Icon RedPotion", "DisplayIcon": "potion", "DisplayName": "RedPotion", "Description": "Select Icon  RedPotion"},
            "GreenPotion": {"ActionName": "Select Icon Potion", "DisplayIcon": "potion", "DisplayName": "GreenPotion", "Description": "Select Icon  GreenPotion"},
            "PurplePotion": {"ActionName": "Select Icon Potion", "DisplayIcon": "potion", "DisplayName": "PurplePotion", "Description": "Select Icon  PurplePotion"},

            "HealthPotion": {"ActionName": "Select Icon HealthPotion", "DisplayIcon": "healingpotion", "DisplayName": "HealthPotion", "Description": "Select Icon  BlueHealthPotion"},
            "BlueHealthPotion": {"ActionName": "Select Icon BlueHealthPotion", "DisplayIcon": "healingpotion", "DisplayName": "BlueHealthPotion", "Description": "Select Icon  BlueHealthPotion"},
            "RedHealthPotion": {"ActionName": "Select Icon HealthPotion", "DisplayIcon": "healingpotion", "DisplayName": "RedHealthPotion", "Description": "Select Icon  RedHealthPotion"},
            "GreenHealthPotion": {"ActionName": "Select Icon HealthPotion", "DisplayIcon": "healingpotion", "DisplayName": "GreenHealthPotion", "Description": "Select Icon  GreenHealthPotion"},
            "PurpleHealthPotion": {"ActionName": "Select Icon HealthPotion", "DisplayIcon": "healingpotion", "DisplayName": "PurpleHealthPotion", "Description": "Select Icon  PurpleHealthPotion"},

            "Gift": {"ActionName": "Select Icon Gift ", "DisplayIcon": "present", "DisplayName": "Gift", "Description": "Gift to present"},
            "Ring": {"ActionName": "Select Icon Ring", "DisplayIcon": "ring", "DisplayName": "Ring", "Description": "Ring for Gift"},
            "Sword": {"ActionName": "Select Icon Sword", "DisplayIcon": "sword", "DisplayName": "Sword", "Description": "Sword for Fight"},

            "Sleep": {"ActionName": "Select Icon Sleep", "DisplayIcon": "sleep", "DisplayName": "Sleep", "Description": "Sleep on Bed"},
            "Meal": {"ActionName": "Select Icon Meal", "DisplayIcon": "meal", "DisplayName": "Meal", "Description": "Having Meal"},
            "Music": {"ActionName": "Select Icon Music", "DisplayIcon": "music", "DisplayName": "Play Music", "Description": "Listening Songs"},  # Need to add musics for different songs available in Camelot
            "Accept": {"ActionName": "Select Icon Accept", "DisplayIcon": "checkmark", "DisplayName": "Accept", "Description": "Accept for Mission"},
            "Reject": {"ActionName": "Select Icon Reject", "DisplayIcon": "cancel", "DisplayName": "Reject", "Description": "Abort Mission"},
            "Return": {"ActionName": "Select Icon Return", "DisplayIcon": "return", "DisplayName": "Return", "Description": "Going back"},
            # Effects
            "FireSpell": {"ActionName": "Select Icon FireSpell", "DisplayIcon": "firespell", "DisplayName": "FireSpell", "Description": "FireSpell"},
            "BrokenHeart": {"ActionName": "Select Icon BrokenHeart", "DisplayIcon": "brokenheart", "DisplayName": "BrokenHeart", "Description": "DisplayName"},
            "LoveCharm": {"ActionName": "Select Icon LoveCharm", "DisplayIcon": "charm", "DisplayName": "LoveCharm", "Description": "LoveCharm"},
            "Hurt": {"ActionName": "Select Icon Hurt", "DisplayIcon": "hurt", "DisplayName": "Hurt", "Description": "Hurt"},
            "Skull": {"ActionName": "Select Icon Skull", "DisplayIcon": "skull", "DisplayName": "Skull", "Description": "Skull"},
            "SnowFlake": {"ActionName": "Select Icon SnowFlake", "DisplayIcon": "snowflake", "DisplayName": "SnowFlake", "Description": "SnowFlake"},
            "Star": {"ActionName": "Select Icon Star", "DisplayIcon": "star", "DisplayName": "Star", "Description": "Star"},

            "Campfire": {"ActionName": "Select Icon Campfire", "DisplayIcon": "campfire", "DisplayName": "Campfire", "Description": "Campfire"},
            "Bridge": {"ActionName": "Select Icon Bridge", "DisplayIcon": "bridge", "DisplayName": "Bridge", "Description": "Bridge"},
            "StonePath": {"ActionName": "Select Icon StonePath", "DisplayIcon": "stonepath", "DisplayName": "StonePath", "Description": "StonePath"},
            "Castle": {"ActionName": "Select Icon Castle", "DisplayIcon": "castle", "DisplayName": "Castle", "Description": "Castle"},
            "Farm": {"ActionName": "Select Icon Farm", "DisplayIcon": "tree", "DisplayName": "Farm", "Description": "Farm"},
            "City": {"ActionName": "Select Icon City", "DisplayIcon": "city", "DisplayName": "City", "Description": "City"},
            "Cottage": {"ActionName": "Select Icon Cottage", "DisplayIcon": "cottage", "DisplayName": "Cottage", "Description": "Cottage"},
            "Forest": {"ActionName": "Select Icon Forest", "DisplayIcon": "forest", "DisplayName": "Forest", "Description": "Forest"},
            "Dungeon": {"ActionName": "Select Icon Dungeon", "DisplayIcon": "dungeon", "DisplayName": "Dungeon", "Description": ""},
            "ExitDoor": {"ActionName": "Select Icon ExitDoor", "DisplayIcon": "exit", "DisplayName": "Exit", "Description": "Exit from the Door"},
            "ExitPlace": {"ActionName": "Select Icon ExitPlace", "DisplayIcon": "exit", "DisplayName": "ExitPlace", "Description": "Exit from present Place"},
            "ExitGate": {"ActionName": "Select Icon ExitGate", "DisplayIcon": "exit", "DisplayName": "Exit", "Description": "Exit from the Gate"},
            "LockedDoor": {"ActionName": "Select Icon LockedDoor", "DisplayIcon": "lockeddoor", "DisplayName": "LockedDoor", "Description": ""},
            "LockedChest": {"ActionName": "Select Icon LockedChest", "DisplayIcon": "lockedchest", "DisplayName": "LockedChest", "Description": ""},
            "FirePlace": {"ActionName": "Select Icon FirePlace", "DisplayIcon": "fireplace", "DisplayName": "FirePlace", "Description": ""},
            "Door": {"ActionName": "Select Icon Door", "DisplayIcon": "door", "DisplayName": "Door", "Description": ""},
            "WoodenDoor": {"ActionName": "Select Icon WoodenDoor", "DisplayIcon": "woodendoor", "DisplayName": "WoodenDoor", "Description": "WoddenDoor"},
            "Target": {"ActionName": "Select Icon Target", "DisplayIcon": "target", "DisplayName": "Target", "Description": "Target"},
            "Well": {"ActionName": "Select Icon Well", "DisplayIcon": "well", "DisplayName": "Go to Well", "Description": "Well"},
            "Throne": {"ActionName": "Select Icon Throne", "DisplayIcon": "throne", "DisplayName": "Throne", "Description": "Throne"},
            "Chest": {"ActionName": "Select Icon Chest", "DisplayIcon": "chest", "DisplayName": "Chest", "Description": "Chest"},
            "Chair": {"ActionName": "Select Icon Cchair", "DisplayIcon": "chair", "DisplayName": "Chair", "Description": "Chair"},
            "Bed": {"ActionName": "Select Icon Bed", "DisplayIcon": "bed", "DisplayName": "Bed", "Description": "Bed"},
            "Cauldron": {"ActionName": "Select Icon Cauldron", "DisplayIcon": "cauldron", "DisplayName": "Cauldron", "Description": "Cauldron"},
            "Shoping": {"ActionName": "Select Icon Shoping", "DisplayIcon": "shopsign", "DisplayName": "Shoping", "Description": "Shoping"},
            "Ship": {"ActionName": "Select Icon Ship", "DisplayIcon": "ship", "DisplayName": "Ship", "Description": "Ship"},
            "Anvil": {"ActionName": "Select Icon Anvil", "DisplayIcon": "anvil", "DisplayName": "Anvil", "Description": "Anvil"},
            "Mug": {"ActionName": "Select Icon Mug", "DisplayIcon": "mug", "DisplayName": "Mug", "Description": "Mug"},

            "SunRise": {"ActionName": "Select Icon SunRise", "DisplayIcon": "sunrise", "DisplayName": "SunRise", "Description": "SunRice"},
            "SunSet": {"ActionName": "Select Icon SunSet", "DisplayIcon": "sunrise", "DisplayName": "SunSet", "Description": "SunSet"},
            "Time": {"ActionName": "Select Icon Time", "DisplayIcon": "time", "DisplayName": "Time", "Description": "Time"},
            "Tree": {"ActionName": "Select Icon Tree", "DisplayIcon": "tree", "DisplayName": "Tree", "Description": "Tree"},
            "Unlock": {"ActionName": "Select Icon Unlock", "DisplayIcon": "unlock", "DisplayName": "Unlock", "Description": "Unlock Door or Cell"},
            "Torch": {"ActionName": "Select Icon Torch", "DisplayIcon": "torch", "DisplayName": "Torch", "Description": "Put Fire on"},
            "TimeHourGlass": {"ActionName": "Select Icon  TimeHourGlass", "DisplayIcon": "hourglass", "DisplayName": "TimeHourGlass", "Description": "TimeHourGlass"}
        }
        # -------------------------------------------------------------------------------------------------------------

        self.Icon_Give = Icon_(self.icons["Give"], self.Action)
        self.Icon_Take = Icon_(self.icons["Take"], self.Action)
        self.Icon_Torch = Icon_(self.icons["Torch"], self.Action)
        self.Icon_Attack = Icon_(self.icons["Attack"], self.Action)
        self.Icon_Talk = Icon_(self.icons["Talk"], self.Action)
        self.Icon_Accept = Icon_(self.icons["Accept"], self.Action)
        self.Icon_Anvil = Icon_(self.icons["Anvil"], self.Action)
        self.Icon_Apple = Icon_(self.icons["Apple"], self.Action)
        self.Icon_Bed = Icon_(self.icons["Bed"], self.Action)
        self.Icon_BlueBook  = Icon_(self.icons["BlueBook"], self.Action)
        self.Icon_BlueKey   = Icon_(self.icons["BlueKey"], self.Action)
        self.Icon_BluePotion = Icon_(self.icons["BluePotion"], self.Action)
        self.Icon_Book  = Icon_(self.icons["Book"], self.Action)
        self.Icon_Bridge = Icon_(self.icons["Bridge"], self.Action)
        self.Icon_BrokenHeart = Icon_(self.icons["BrokenHeart"], self.Action)
        self.Icon_Campfire = Icon_(self.icons["Campfire"], self.Action)
        self.Icon_Castle = Icon_(self.icons["Castle"], self.Action)
        self.Icon_Cauldron = Icon_(self.icons["Cauldron"], self.Action)
        self.Icon_Chair = Icon_(self.icons["Chair"], self.Action)
        self.Icon_Chest = Icon_(self.icons["Chest"], self.Action)
        self.Icon_Farm = Icon_(self.icons["Farm"], self.Action)
        self.Icon_City = Icon_(self.icons["City"], self.Action)
        self.Icon_CloseScroll = Icon_(self.icons["CloseScroll"], self.Action)
        self.Icon_Cottage = Icon_(self.icons["Cottage"], self.Action)
        self.Icon_Door = Icon_(self.icons["Door"], self.Action)
        self.Icon_Dress = Icon_(self.icons["Dress"], self.Action)
        self.Icon_Dungeon = Icon_(self.icons["Dungeon"], self.Action)
        self.Icon_Drink = Icon_(self.icons["Drink"], self.Action)
        self.Icon_EvilBook = Icon_(self.icons["EvilBook"], self.Action)
        self.Icon_ExitDoor = Icon_(self.icons["ExitDoor"], self.Action)
        self.Icon_ExitPlace = Icon_(self.icons["ExitPlace"], self.Action)
        self.Icon_ExitGate = Icon_(self.icons["ExitGate"], self.Action)
        self.Icon_FirePlace = Icon_(self.icons["FirePlace"], self.Action)
        self.Icon_FireSpell = Icon_(self.icons["FireSpell"], self.Action)
        self.Icon_Forest = Icon_(self.icons["Forest"], self.Action)
        self.Icon_Gift = Icon_(self.icons["Gift"], self.Action)
        self.Icon_GreenBook = Icon_(self.icons["GreenBook"], self.Action)
        self.Icon_GreenKey = Icon_(self.icons["GreenKey"], self.Action)
        self.Icon_GreenPotion = Icon_(self.icons["GreenPotion"], self.Action)
        self.Icon_Health = Icon_(self.icons["Health"], self.Action)
        self.Icon_HealthPotion = Icon_(self.icons["HealthPotion"], self.Action)
        self.Icon_Hurt = Icon_(self.icons["Hurt"], self.Action)
        self.Icon_JewelKey = Icon_(self.icons["JewelKey"], self.Action)
        self.Icon_Key = Icon_(self.icons["Key"], self.Action)
        self.Icon_LockedChest = Icon_(self.icons["LockedChest"], self.Action)
        self.Icon_LockedDoor = Icon_(self.icons["LockedDoor"], self.Action)
        self.Icon_LoveCharm = Icon_(self.icons["LoveCharm"], self.Action)
        self.Icon_LovePotion = Icon_(self.icons["LovePotion"], self.Action)
        self.Icon_Meal = Icon_(self.icons["Meal"], self.Action)
        self.Icon_Money = Icon_(self.icons["Money"], self.Action)
        self.Icon_GiveMoney = Icon_(self.icons["GiveMoney"], self.Action)
        self.Icon_TakeMoney = Icon_(self.icons["TakeMoney"], self.Action)
        self.Icon_Mug = Icon_(self.icons["Mug"], self.Action)
        self.Icon_Music = Icon_(self.icons["Music"], self.Action)
        self.Icon_OpenScroll = Icon_(self.icons["OpenScroll"], self.Action)
        self.Icon_Pick = Icon_(self.icons["Pick"], self.Action)
        self.Icon_Poison = Icon_(self.icons["Poison"], self.Action)
        self.Icon_Potion = Icon_(self.icons["Potion"], self.Action)
        self.Icon_PurpleBook = Icon_(self.icons["PurpleBook"], self.Action)
        self.Icon_PurpleKey = Icon_(self.icons["PurpleKey"], self.Action)
        self.Icon_PurplePotion = Icon_(self.icons["PurplePotion"], self.Action)
        self.Icon_RedBook = Icon_(self.icons["RedBook"], self.Action)
        self.Icon_RedKey = Icon_(self.icons["RedKey"], self.Action)
        self.Icon_RedPotion = Icon_(self.icons["RedPotion"], self.Action)
        self.Icon_Reject = Icon_(self.icons["Reject"], self.Action)
        self.Icon_Return = Icon_(self.icons["Return"], self.Action)
        self.Icon_Ring = Icon_(self.icons["Ring"], self.Action)
        self.Icon_Ship = Icon_(self.icons["Ship"], self.Action)
        self.Icon_Shoping = Icon_(self.icons["Shoping"], self.Action)
        self.Icon_Skull = Icon_(self.icons["Skull"], self.Action)
        self.Icon_Sleep = Icon_(self.icons["Sleep"], self.Action)
        self.Icon_SnowFlake = Icon_(self.icons["SnowFlake"], self.Action)
        self.Icon_SpellBook = Icon_(self.icons["SpellBook"], self.Action)
        self.Icon_Star = Icon_(self.icons["Star"], self.Action)
        self.Icon_StonePath = Icon_(self.icons["StonePath"], self.Action)
        self.Icon_SunRise = Icon_(self.icons["SunRise"], self.Action)
        self.Icon_SunSet = Icon_(self.icons["SunSet"], self.Action)
        self.Icon_Sword = Icon_(self.icons["Sword"], self.Action)
        self.Icon_Target = Icon_(self.icons["Target"], self.Action)
        self.Icon_Throne = Icon_(self.icons["Throne"], self.Action)
        self.Icon_Time = Icon_(self.icons["Time"], self.Action)
        self.Icon_TimeHourGlass = Icon_(self.icons["TimeHourGlass"], self.Action)
        self.Icon_Tree = Icon_(self.icons["Tree"], self.Action)
        self.Icon_Well = Icon_(self.icons["Well"], self.Action)
        self.Icon_WoodenDoor = Icon_(self.icons["WoodenDoor"], self.Action)
        self.Icon_Woods = Icon_(self.icons["Woods"], self.Action)
        self.Icon_Unlock = Icon_(self.icons["Unlock"], self.Action)


        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # ================================================  SOUND EFFECTS  =============================================
        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # ------------------------------------ DICTIONARIES -----------------------------------------
        self.SoundEffects = {
            "Flute2"        : {"Name": "Flute2",    "Type": "Flute2"},
            "Flute1"        : {"Name": "Flute1",    "Type": "Flute1"},
            "Button"        : {"Name": "Button",    "Type": "Button"},
            "Menu"          : {"Name": "Menu",      "Type": "Menu"},
            "Spooky"        : {"Name": "Spooky",    "Type": "Spooky"},
            "Error"         : {"Name": "Error",     "Type": "Error"},
            "Spell2"        : {"Name": "Spell2",    "Type": "Spell2"},
            "Potion"        : {"Name": "Potion",    "Type": "Potion"},
            "Fireplace"     : {"Name": "Fireplace", "Type": "Fireplace"},
            "DarkMagic"     : {"Name": "DarkMagic", "Type": "DarkMagic"},
            "Fireball"      : {"Name": "Fireball",  "Type": "Fireball"},
            "Clap"          : {"Name": "Clap",      "Type": "Clap"},
            "Danger1"       : {"Name": "Danger1",   "Type": "Danger1"},
            "Danger2"       : {"Name": "Danger2",   "Type": "Danger2"},
            "Danger3"       : {"Name": "Danger3",   "Type": "Danger3"},
            "Dramatic"      : {"Name": "Dramatic",  "Type": "Dramatic"},
            "Draw"          : {"Name": "Draw",      "Type": "Draw"},
            "Eat"           : {"Name": "Eat",       "Type": "Eat"},
            "Explorer"      : {"Name": "Explorer",  "Type": "Explorer"},
            "Grief"         : {"Name": "Grief",     "Type": "Grief"},
            "Hammer"        : {"Name": "Hammer",    "Type": "Hammer"},
            "Kingdom"       : {"Name": "Kingdom",   "Type": "Kingdom"},
            "LivelyMusic"   : {"Name": "LivelyMusic", "Type": "LivelyMusic"},
            "Lock"          : {"Name": "Hammer",    "Type": "Hammer"},
            "Ominous"       : {"Name": "Ominous",   "Type": "Ominous"},
            "Peaceful"      : {"Name": "Peaceful",  "Type": "Peaceful"},
            "Pocket"        : {"Name": "Pocket",    "Type": "Pocket"},
            "Serenade"      : {"Name": "Serenade",  "Type": "Serenade"},
            "Serenity"      : {"Name": "Serenity",  "Type": "Serenity"},
            "Sheathe"       : {"Name": "Sheathe",   "Type": "Sheathe"},
            "Tavern"        : {"Name": "Tavern",    "Type": "Tavern"},
            "Unlock"        : {"Name": "Unlock",    "Type": "Unlock"},
            "Unpocket"      : {"Name": "Unpocket",  "Type": "Unpocket"},
            "Write"         : {"Name": "Write",     "Type": "Write"}
        }

        # ------------------------------------ CLASS OBJECTS -----------------------------------------
        self.SEffect_Flute2 = SoundEffect_(self.SoundEffects["Flute2"], self.Music_On_Off, self.Action)
        self.SEffect_Flute1 = SoundEffect_(self.SoundEffects["Flute1"], self.Music_On_Off, self.Action)
        self.SEffect_Button = SoundEffect_(self.SoundEffects["Button"], self.Music_On_Off, self.Action)
        self.SEffect_Menu = SoundEffect_(self.SoundEffects["Menu"], self.Music_On_Off, self.Action)
        self.SEffect_Spooky = SoundEffect_(self.SoundEffects["Spooky"], self.Music_On_Off, self.Action)
        self.SEffect_Error = SoundEffect_(self.SoundEffects["Error"], self.Music_On_Off, self.Action)
        self.SEffect_Spell2 = SoundEffect_(self.SoundEffects["Spell2"], self.Music_On_Off, self.Action)
        self.SEffect_Potion = SoundEffect_(self.SoundEffects["Potion"], self.Music_On_Off, self.Action)
        self.SEffect_Ominous = SoundEffect_(self.SoundEffects["Ominous"], self.Music_On_Off, self.Action)
        self.SEffect_Fireplace = SoundEffect_(self.SoundEffects["Fireplace"], self.Music_On_Off, self.Action)
        self.SEffect_DarkMagic = SoundEffect_(self.SoundEffects["DarkMagic"], self.Music_On_Off, self.Action)
        self.SEffect_Fireball = SoundEffect_(self.SoundEffects["Fireball"], self.Music_On_Off, self.Action)
        self.SEffect_Clap = SoundEffect_(self.SoundEffects["Clap"], self.Music_On_Off, self.Action)
        self.SEffect_Draw = SoundEffect_(self.SoundEffects["Draw"], self.Music_On_Off, self.Action)
        self.SEffect_Eat = SoundEffect_(self.SoundEffects["Eat"], self.Music_On_Off, self.Action)
        self.SEffect_Hammer = SoundEffect_(self.SoundEffects["Hammer"], self.Music_On_Off, self.Action)
        self.SEffect_Lock = SoundEffect_(self.SoundEffects["Lock"], self.Music_On_Off, self.Action)
        self.SEffect_Pocket = SoundEffect_(self.SoundEffects["Pocket"], self.Music_On_Off, self.Action)
        self.SEffect_Sheathe = SoundEffect_(self.SoundEffects["Sheathe"], self.Music_On_Off, self.Action)
        self.SEffect_Unlock = SoundEffect_(self.SoundEffects["Unlock"], self.Music_On_Off, self.Action)
        self.SEffect_Unpocket = SoundEffect_(self.SoundEffects["Unpocket"], self.Music_On_Off, self.Action)
        self.SEffect_Write = SoundEffect_(self.SoundEffects["Write"], self.Music_On_Off, self.Action)
        # --------------------------------- Musical Sounds ---------------------------------
        self.SEffect_Danger1 = SoundEffect_(self.SoundEffects["Danger1"], self.Music_On_Off, self.Action)
        self.SEffect_Danger2 = SoundEffect_(self.SoundEffects["Danger2"], self.Music_On_Off, self.Action)
        self.SEffect_Danger3 = SoundEffect_(self.SoundEffects["Danger3"], self.Music_On_Off, self.Action)
        self.SEffect_Dramatic = SoundEffect_(self.SoundEffects["Dramatic"], self.Music_On_Off, self.Action)
        self.SEffect_Explorer = SoundEffect_(self.SoundEffects["Explorer"], self.Music_On_Off, self.Action)
        self.SEffect_Grief = SoundEffect_(self.SoundEffects["Grief"], self.Music_On_Off, self.Action)
        self.SEffect_Kingdom = SoundEffect_(self.SoundEffects["Kingdom"], self.Music_On_Off, self.Action)
        self.SEffect_LivelyMusic = SoundEffect_(self.SoundEffects["LivelyMusic"], self.Music_On_Off, self.Action)
        self.SEffect_Ominous = SoundEffect_(self.SoundEffects["Ominous"], self.Music_On_Off, self.Action)
        self.SEffect_Peaceful = SoundEffect_(self.SoundEffects["Peaceful"], self.Music_On_Off, self.Action)
        self.SEffect_Serenade = SoundEffect_(self.SoundEffects["Serenade"], self.Music_On_Off, self.Action)
        self.SEffect_Serenity = SoundEffect_(self.SoundEffects["Serenity"], self.Music_On_Off, self.Action)

        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # ===============================================  VISUAL EFFECTS  =============================================
        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # ------------------------------------ DICTIONARIES -----------------------------------------
        self.VisualEffects = {
            "Diamond"       : {"Name": "Diamond",       "Type": "Diamond"},
            "Force"         : {"Name": "Force",         "Type": "Force"},
            "Campfire"      : {"Name": "Campfire",      "Type": "Campfire"},
            "Death"         : {"Name": "Death",         "Type": "Death"},
            "Explosion"     : {"Name": "Explosion",     "Type": "Explosion"},
            "Heart"         : {"Name": "Heart",         "Type": "Heart"},
            "Heartbroken"   : {"Name": "Heartbroken",   "Type": "Heartbroken"},
            "Aura"          : {  "Name": "Aura",        "Type": "Aura"},
            "Blood"         : {"Name": "Blood",         "Type": "Blood"},
            "Brew"          : {"Name": "Brew",          "Type": "Brew"},
            "Blackflame"    : {"Name": "Blackflame",    "Type": "Blackflame"},
            "Poof"          : {"Name": "Poof",          "Type": "Poof"},
            "Skulls"        : {"Name": "Skulls",        "Type": "Skulls"},
            "Spiralflame"   : {"Name": "Spiralflame",   "Type": "Spiralflame"},
            "Poison"        : {"Name": "Poison",        "Type": "Poison"},
            "Wildfire"      : {"Name": "Poison",        "Type": "Wildfire"},
            "Resurrection"  : {"Name": "Resurrection",  "Type": "Resurrection"},
            "Magic"         : {"Name": "Magic",         "Type": "Magic"}
        }

        # ------------------------------------ CLASS OBJECTS -----------------------------------------
        self.VEffect_Aura           = VisualEffect_(self.VisualEffects["Aura"],         self.Action)
        self.VEffect_Blood          = VisualEffect_(self.VisualEffects["Blood"],        self.Action)
        self.VEffect_Brew           = VisualEffect_(self.VisualEffects["Brew"],         self.Action)
        self.VEffect_Blackflame     = VisualEffect_(self.VisualEffects["Blackflame"],   self.Action)
        self.VEffect_Campfire       = VisualEffect_(self.VisualEffects["Campfire"],     self.Action)
        self.VEffect_Death          = VisualEffect_(self.VisualEffects["Death"],        self.Action)
        self.VEffect_Diamond        = VisualEffect_(self.VisualEffects["Diamond"],      self.Action)
        self.VEffect_Force          = VisualEffect_(self.VisualEffects["Force"],        self.Action)
        self.VEffect_Explosion      = VisualEffect_(self.VisualEffects["Explosion"],    self.Action)
        self.VEffect_Heart          = VisualEffect_(self.VisualEffects["Heart"],        self.Action)
        self.VEffect_Heartbroken    = VisualEffect_(self.VisualEffects["Heartbroken"],  self.Action)
        self.VEffect_Magic          = VisualEffect_(self.VisualEffects["Magic"],        self.Action)
        self.VEffect_Poof           = VisualEffect_(self.VisualEffects["Poof"],         self.Action)
        self.VEffect_Poison         = VisualEffect_(self.VisualEffects["Poison"],       self.Action)
        self.VEffect_Resurrection   = VisualEffect_(self.VisualEffects["Resurrection"], self.Action)
        self.VEffect_Skulls         = VisualEffect_(self.VisualEffects["Skulls"],       self.Action)
        self.VEffect_Spiralflame    = VisualEffect_(self.VisualEffects["Spiralflame"],  self.Action)
        self.VEffect_Wildfire       = VisualEffect_(self.VisualEffects["Wildfire"],     self.Action)

        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # ================================================  NARRATIONS  ================================================
        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        N_FP01 = ["Wow! This place is sooo Beautiful !!!", "There is someone standing there. I will ask them."]
        self.N_FP01_Bob = Message_(N_FP01, self.Action)

        N_FP02 = ["Select one of Blue or Red Potions Carefully"]
        self.N_FP02_Bob_Well_Help = Message_(N_FP02, self.Action)

        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # ==================================================  DIALOGS  =================================================
        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        self.D_Music_On_Off =  Message_(["Music : [CloseOn|ON] , [CloseOff|OFF]"], self.Action)
        self.D_GameInstructions = Message_(["%%%%%%%%%%% INSTRUCTIONS %%%%%%%%%%%",
                                            "--------- Keyboard ---------",
                                            "W | UP  : Player Moves Front",
                                            "S | Down  : Player Moves Back",
                                            "A | Left  : Player Moves Left",
                                            "D | Right  : Player Moves Right",
                                            "E : Player Hints",
                                            "I : Player Inventory",
                                            "--------- Mouse ---------",
                                            "Left Click : PLayer Moves to Mouse Left Click Location or if Mouse Left click on Icon is enabled object, Default Icon will be activated",
                                            "Right Click : Select enabled Icon on Entity or Object"
                                            ], self.Action)
        # ------------------------------------ @ FOREST PATH @ -----------------------------------------
        self.D_FP00_Bob_Die_English = Message_(["Wrong Step....",
                                        "____Choose____",
                                        "[RESTART|RESTART] :::: [QUIT|QUIT]"], self.Action)
        # self.D_FP00_Bob_Die_Expressions = ["sad", "sad","sad"]

        self.D_FP01_Bob_Angel_English = Message_(["BOB : Hello, I am Bob. What place is it?",
                                  "ANGEL : Hello Bob this is a magical forest. Only the luckiest can come here.",
                                  "BOB : oh wow. I am here to get some powers.",
                                  "ANGEL : Oh then you have to finish the task to get that.",
                                  "If you ready, got to well and Select one from the potions (RED | BLUE). Remember, only one gives you Power."
                                                  ], self.Action)
        self.D_FP01_Bob_Angel_Telugu = Message_(["BOB : Hello, Nenu Bob. Ee pradesham Emiti?",
                                                  "ANGEL : Hello Bob, idi maya prapamchapu adavi. Adhrushtavanthulu matrame ikkadiki ragalaru.",
                                                  "BOB : Aha Adhbutam. Nenu konni shakthulanu pondataniki ikkadiki vachanu.",
                                                  "ANGEL : Oh, Ayithe vatini pondadaniki meeru oka panini poorthi cheyali.",
                                                  "Meeru siddamga unte, ikkada daggarlo unna bhavi vaddaku velli oka danni enchukondi (Erupu, Neelam) Gurthunchukondi, okati matrame neeku kavalasina shakthini isthundi."
                                                  ], self.Action)

        self.D_FP02_Bob_Angel_English = Message_(["BOB: I have selected a potion. What do I have to do with potion?",
                                          "ANGEL: Drink it",
                                          "BOB: Okay"
                                                  ], self.Action)

        self.D_FP03_Bob_Angel_BluePotion = Message_(["BOB: What happened now? I did not feel anything.",
                                                     "ANGEL: Unluckily, you got no Power.",
                                                     "ANGEL: But, do not worry, I can give one SecretSpell use this at right time.",
                                                     "ANGEL: [CLOSE | OmBhimBhush]",
                                                     "ANGEL: Remember, Do not forget this SecretSpell"],
                                                    self.Action
                                                    )
        self.D_FP03_Bob_Angel_RedPotion_English = Message_(["BOB: Oh my Goddess, I feel so Strong now. What is next Goddess?",
                                                    "ANGEL: Lucky, You got enough strength & power.",
                                                    "ANGEL: And take this SecretScroll also and Go to the City.",
                                                    "ANGEL: You will be guided by someone there.",
                                                    "ANGEL: Remember, Choose the steps carefully, it is a dangerous place."],
                                                           self.Action
                                                           )
        # ------------------------------------ @ BRIDGE from FP to CBR @ -----------------------------------------
        self.D_Bridge_Bob_Amelia_Talk_English = Message_(["Bob : Wow! These flowers are very beautiful. what are these?",
                                                          "Amelia : These are called as Meconopsis which are genus of flowering plants in the poppy family Papaveraceae.",
                                                          "Bob : I want to take one flower for my love but I do not have money now, I will come back here and give money while returning.",
                                                          "Amelia: Okay take it."
                                                          ], self.Action)

        # ------------------------------------ @ CASTLE BED ROOM @ -----------------------------------------
        self.D_CBR01_Bob_Candy_Talk_1_English = Message_(["BOB: My dear! How are you feeling now?",
                                                   "CANDY: No, I am sick.",
                                                   "BOB: Do not worry dear, Be strong, I am there with you.",
                                                   "CANDY: Okay dear!!!"
                                                          ], self.Action)
        self.D_CBR02_Bob_Candy_Talk_2_English = Message_(["BOB: No worries, I will go, find, and bring the Cure. Lilly will take care of you till then",
                                                  "CANDY: No dear, you stay with me in the last minute of me diying.",
                                                  "BOB: Do not say that, I can save you. Please let me save you.",
                                                  "CANDY: Okay dear! Take care."
                                                          ], self.Action)
        self.D_CBR03_Bob_LillyS_Talk_English = Message_(["BOB: Lilly, Candy is sick now. Can you take care of her?",
                                                 "BOB: In sometime, I will go to bring the cure for your sister.",
                                                 "LILLY: Okay, I will look after her. You take care.",
                                                 "BOB: Tell me if you need anything.",
                                                 "LILLY: Okay!"
                                                         ], self.Action)


        # ------------------------------------ @ CITY @ -----------------------------------------
        self.D05_City_Bob_JimS_English = Message_(["BOB: Hello, I am new here.",
                                                    "Can you tell me how I can meet AngelOfDeath?",
                                                    "JIM: Oh Sorry, I do not. I am also new for this place."
                                                   ], self.Action)
        self.D06_City_Bob_JackS_English = Message_(["BOB: Hello, I am new here.",
                                                    "Can you tell me how I can meet AngelOfDeath?",
                                                     "JACK: Oh yes, I knew her. She comes rarely. Wait at Fountain to meet her.",
                                                    ], self.Action)
        self.D07_City_Bob_TomS_English = Message_(["Bob: Hello, I am new here.",
                                                   "Can you tell me how I can meet AngelOfDeath?",
                                                    "Tom: You are not belonging here, Get out."
                                                    ], self.Action)
        self.D08_City_Bob_AngelOfDeath1_English = Message_(["BOB: Hello, I am new here.",
                                                             "Can you tell me how I can meet AngelOfDeath?",
                                                            "SUSU: Go to Fountain and complete the test and pass them to meet her.",
                                                            "BOB: Okay, Thank you"
                                                            ], self.Action)

        self.D08_City_Bob_AngelOfDeath_English = Message_(["AOD: Hello young man, what is the matter.",
                                     "BOB: My wife is sick. I am looking for Angel here who can help me.",
                                     "AOD: Where are you coming from? and Who sent you here?",
                                     "BOB: Angel sent me from Forest. Please help me to find her.",
                                     "AOD: Nearby there is a fountain with Eagle Statue which has some tasks. You have to complete to meet her."
                                                           ], self.Action)

        self.D_City_Bob_Emily_Talk = Message_(["BOB: Hello, I am new here.",
                                               "Can you tell me how I can meet Priest?",
                                               "Emily: Oh Sorry, I do not. I am also new for this place."
                                               ], self.Action)
        self.D_City_Bob_Fountain_Sword = Message_(["As You have selected Sword You need to complete the task at RedHouseDoor to meet the Priest who is Prisoned by Evil"], self.Action)
        self.D_City_Bob_Tom_Talk = Message_(["BOB: Please help me to meet priest",
                                             "TOM: No I will not let you in"
                                             ], self.Action)
        self.D_City_SwordTask_Bob_Priest_Talk = Message_(["PRIEST: Thank you so much man, make a wish ill make that true.",
                                                   "BOB: My wife is sick please give medicine to save her life,",
                                                   "PRIEST: Do not worry poor boy, Ill definitely help you but for that you need to win in the battle with a dangerous evil, go to ruins to fight with him"
                                                          ], self.Action)
        self.D_City_Bob_Fountain_EvilBook = Message_(["Wow you got magical power, you can meet famous priest who can help you get the medicine, to meet him go to farm"], self.Action)
        self.D_City_EvilBookTask_Bob_Priest_Talk = Message_(["BOB: Please save my wife she is sick iam worried about her life.",
                                                   "PRIEST: Do not worry poor boy Ill definitely help you but for that you need to win in the battle with a dangerous evil go to ruins to fight with him."
                                                             ], self.Action)

        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # =============================================  INVENTORY OBJECTS  ============================================
        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

        self.Char_Bob_Inventory = Inventory_(self.Char_Bob.Name, self.Action)
        self.Char_Lilly_S_Inventory = Inventory_(self.Char_Lilly_S.Name, self.Action)
        self.FP_Item_Well_Inventory = Inventory_(self.Place_ForestPath.Well, self.Action)
        self.CBR_Item_Chest_Inventory = Inventory_(self.Place_CastleBedRoom.Chest, self.Action)
        self.City_Item_Fountain_Inventory = Inventory_(self.Place_City.Fountain, self.Action)
        self.Dungeon_Item_Chest_Inventory = Inventory_(self.Place_Dungeon.Chest, self.Action)


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% ROUGH COPY %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
'''self.D_FP02_Bob_Angel = Message_(["BOB: I have to save my wife. Can you please help me which one to select?",
                                            "Angel: Sorry young man, I am prohibited to tell that and you have to choose wisely.",
                                            "Angel: As you are here for saving life, all I can help you is 'Go Opposite Direction'."
                                          ], self.Action)'''