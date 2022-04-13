from Actions import Actions
from Places import ForestPath_, Bridge_, CastleBedroom_, City_, CastleCrossroads_    # Ruins
from Characters import Character_
from Items import Item_
from Icons import Icon_
from VisualEffects import VisualEffect_
from Messages import Message_
from Set import Set_
from Displays import Display
from SoundEffects import SoundEffect_

class Variables:
    def __init__(self):
        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # ==========================================  Status check variables  ==========================================
        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                # Activities status which tells where player has reached and where to go
        self.Menu_Title = "|- SAVING LIFE -|"
        self.EscapeCount = 0
        self.Status_EntireGame = ""
        self.Status_AFP = ""            # Place: ForestPath
        self.Status_Bridge = ""         # Place : Bridge
        self.Status_CBR = ""            # Place: CastleBedRoom
        self.Status_City = ""           # Place: City
        self.Status_CCR = ""            # Place: CastleCrossRoad
        self.Status_Ruins = ""          # Place: Ruins
        self.SecretSpell_Angel = ""     # SecretSpell: OmBhimBhush

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
            "BobHouse": {"Name": "BobHouse", "Type": "CastleBedroom"},
            "City": {"Name": "City", "Type": "City"},
            "CastleCrossroads": {"Name": "CrossRoad", "Type": "CastleCrossroads"},
            "Ruins": {"Name": "Ruins", "Type": "Ruins"}
        }
        # ------------------------------------ CLASS OBJECTS -----------------------------------------
        self.Place_ForestPath = ForestPath_(self.places["ForestPath"], self.Action)
        self.Place_Bridge = Bridge_(self.places['Bridge'], self.Action)
        self.Place_BobHouse = CastleBedroom_(self.places["BobHouse"], self.Action)
        self.Place_City = City_(self.places["City"], self.Action)
        self.Place_CastleCrossroads = CastleCrossroads_(self.places["CastleCrossroads"], self.Action)
        # self.Place_Ruins = Ruins_(self.places["Ruins"], self.Action)

        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # =================================================  CHARACTERS  ===============================================
        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # ------------------------------------ DICTIONARIES -----------------------------------------
        # Character Parameters : [<Name>, <BodyType>, <HairStyle>, <HairColor>, <EyeColor>, <Outfits>, <Role>]
        self.characters = {
            "Bob"         : {"Name": "Bob",          "BodyType": "B",    "SkinColor": "5",   "HairStyle": "Long",    "HairColor": "black",   "EyeColor": "black",    "Outfits": "Peasant",       "Role": "Player"},
            "Candy"       : {"Name": "Candy",        "BodyType": "A",    "SkinColor": "5",   "HairStyle": "Long",    "HairColor": "black",   "EyeColor": "black",    "Outfits": "Peasant",       "Role": "BobWife, Sick"},
            "Lilly_S"     : {"Name": "Lilly_S",      "BodyType": "G",    "SkinColor": "5",   "HairStyle": "Straight","HairColor": "Short",   "EyeColor": "black",    "Outfits": "Merchant",      "Role": "Support character - used anywhere and Worker at BobsHouse"},
            "Angel"       : {"Name": "Angel",        "BodyType": "C",    "SkinColor": "5",   "HairStyle": "Long",    "HairColor": "black",   "EyeColor": "red",      "Outfits": "Witch",         "Role": "Guide persons to get power who come forest"},
            "AngelOfDeath": {"Name": "AngelOfDeath", "BodyType": "E",    "SkinColor": "5",   "HairStyle": "Long",    "HairColor": "black",   "EyeColor": "red",      "Outfits": "Priest",        "Role": "Guide persons to get power who come City"},
            "Devil"       : {"Name": "Devil",        "BodyType": "H",    "SkinColor": "5",   "HairStyle": "Long",    "HairColor": "black",   "EyeColor": "black",    "Outfits": "HeavyArmour",   "Role": "Secure the Cure at Ruins"},
            "Tom_S"       : {"Name": "Tom",          "BodyType": "H",    "SkinColor": "5",   "HairStyle": "Long",    "HairColor": "black",   "EyeColor": "black",    "Outfits": "HeavyArmour",   "Role": "Support character - used anywhere"},
            "Jim_S"       : {"Name": "Jim",          "BodyType": "H",    "SkinColor": "5",   "HairStyle": "Long",    "HairColor": "black",   "EyeColor": "black",    "Outfits": "HeavyArmour",   "Role": "Support character - used anywhere"},
            "Jack_S"      : {"Name": "Jack",         "BodyType": "H",    "SkinColor": "5",   "HairStyle": "Long",    "HairColor": "black",   "EyeColor": "black",    "Outfits": "HeavyArmour",   "Role": "Support character - used anywhere"}
        }
        # ------------------------------------ CLASS OBJECTS -----------------------------------------
        self.Char_Bob = Character_(self.characters["Bob"], self.Action)
        self.Char_Candy = Character_(self.characters["Candy"], self.Action)
        self.Char_Lilly_S = Character_(self.characters["Lilly_S"], self.Action)
        self.Char_Angel = Character_(self.characters["Angel"], self.Action)
        self.Char_AngelOfDeath = Character_(self.characters["AngelOfDeath"], self.Action)
        self.Char_Devil = Character_(self.characters["Devil"], self.Action)
        self.Char_Tom_S = Character_(self.characters["Tom_S"], self.Action)
        self.Char_Jim_S = Character_(self.characters["Jim_S"], self.Action)
        self.Char_Jack_S = Character_(self.characters["Jack_S"], self.Action)


        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # =================================================  ITEMS  ===============================================
        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # ------------------------------------ DICTIONARIES -----------------------------------------
        # Item Parameters : [<Name>, <Type>]
        self.items = {
            "BluePotion"    : {"Name": "BluePotion",    "Type": "BluePotion",   "Role": "Angel"},
            "RedPotion"     : {"Name": "RedPotion",     "Type": "RedPotion",    "Role": "Angel"},
            "CloseScroll"   : {"Name": "CloseScroll",   "Type": "Scroll",       "Role": "Closet"},
            "Money"         : {"Name": "Money",         "Type": "Coin",         "Role": "Closet"},
            "Torch"         : {"Name": "Torch",         "Type": "Torch",        "Role": "Used in Night"},
            "LitTorch"      : {"Name": "LitTorch",      "Type": "LitTorch",     "Role": "Used in Night"},
            "EvilBook"      : {"Name": "EvilBook",      "Type": "EvilBook",     "Role": "Choose right word of it"},
            "BlueBook"      : {"Name": "BlueBook",      "Type": "BlueBook",     "Role": "To Distract Player"},
            "RedBook"       : {"Name": "RedBook",       "Type": "RedBook",      "Role": "To Distract Player"},
            "BobSword"      : {"Name": "BobSword",      "Type": "Sword",        "Role": "Angel"},
            "DevilSword"    : {"Name": "DevilSword",    "Type": "Sword",        "Role": "Devil"},
            "ChestKey"      : {"Name": "ChestKey",      "Type": "BlueKey",      "Role": "SmallTable"},
            "GreenPotion"   : {"Name": "RedPotion",     "Type": "GreenPotion",  "Role": "Angel"},
            "PurplePotion"  : {"Name": "PurplePotion",  "Type": "PurplePotion", "Role": "Angel"},
            "SpellBook"     : {"Name": "SpellBook",     "Type": "SpellBook",    "Role": ""},
            "MedicineBook"  : {"Name": "MedicineBook",  "Type": "BlueBook",     "Role": "Chest"},
            "OpenScroll"    : {"Name": "OpenScroll",    "Type": "OpenScroll",   "Role": "Table"},
            "BlueCloth"     : {"Name": "BlueCloth",     "Type": "BlueCloth",    "Role": "Change Dress"},
            "Help"          : {"Name": "Help",          "Type": "InkandQuill",  "Role": "Used for Help"},
        }
        # ------------------------------------ CLASS OBJECTS -----------------------------------------
        self.Item_ChestKey      = Item_(self.items["ChestKey"],     self.Action)
        self.Item_BluePotion    = Item_(self.items["BluePotion"],   self.Action)
        self.Item_RedPotion     = Item_(self.items["RedPotion"],    self.Action)
        self.Item_GreenPotion   = Item_(self.items["GreenPotion"],  self.Action)
        self.Item_PurplePotion  = Item_(self.items["PurplePotion"], self.Action)
        self.Item_BobSword      = Item_(self.items["BobSword"],     self.Action)
        self.Item_DevilSword    = Item_(self.items["DevilSword"],   self.Action)
        self.Item_BlueBook      = Item_(self.items["BlueBook"],     self.Action)
        self.Item_RedBook       = Item_(self.items["RedBook"],      self.Action)
        self.Item_EvilBook      = Item_(self.items["EvilBook"],     self.Action)
        self.Item_MedicineBook  = Item_(self.items["MedicineBook"], self.Action)
        self.Item_SpellBook     = Item_(self.items["SpellBook"],    self.Action)
        self.Item_Money         = Item_(self.items["Money"],        self.Action)
        self.Item_CloseScroll   = Item_(self.items["CloseScroll"],  self.Action)
        self.Item_OpenScroll    = Item_(self.items["OpenScroll"],   self.Action)
        self.Item_BlueCloth     = Item_(self.items["BlueCloth"],    self.Action)
        self.Item_Help          = Item_(self.items["Help"],         self.Action)


        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # ====================================================  ICONS  =================================================
        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # ------------------------------------ DICTIONARIES -----------------------------------------
        self.icons = {
            "Attack"    : {"ActionName": "Select Icon Attack", "DisplayIcon": "first", "DisplayName": "Attack", "Description": "Attack"},
            "Talk"      : {"ActionName": "Select Icon Talk", "DisplayIcon": "talk", "DisplayName": "Talk", "Description": "Talk"},
            "Dress"     : {"ActionName": "Select Icon Dress", "DisplayIcon": "dress", "DisplayName": "Dress", "Description": "Changing Dress"},
            "Money"     : {"ActionName": "Select Icon Money", "DisplayIcon": "coins", "DisplayName": "Money", "Description": "Take Money"},
            "Pick": {"ActionName": "Select Icon PickObject", "DisplayIcon": "hand", "DisplayName": "Pick", "Description": "Pick Object"},
            "CloseScroll": {"ActionName": "Select Icon  CloseScroll", "DisplayIcon": "scroll", "DisplayName": "CloseScroll", "Description": "Closed Scroll used for directions"},
            "OpenScroll": {"ActionName": "Select Icon  OpenScroll", "DisplayIcon": "openscroll", "DisplayName": "OpenScroll", "Description": "Closed Scroll to read matter"},
            "Woods": {"ActionName": "Select Icon Woods", "DisplayIcon": "woodpile", "DisplayName": "Woods", "Description": "Select Icon ing Woods"},
            "Health": {"ActionName": "Select Icon HealingPotion", "DisplayIcon": "healingpotion", "DisplayName": "Health", "Description": "Used for Increase Health"},
            "Apple": {"ActionName": "Select Icon  Apple", "DisplayIcon": "apple", "DisplayName": "Apple", "Description": "Select Icon ing Apple"},
            "Book": {"ActionName": "Select Icon  Book", "DisplayIcon": "book", "DisplayName": "Book", "Description": "Select Icon  Book"},
            "EvilBook": {"ActionName": "Select Icon EvilBook", "DisplayIcon": "evilbook", "DisplayName": "EvilBook", "Description": "Select Icon ed for Danger"},
            "BlueBook": {"ActionName": "Select Icon BlueBook", "DisplayIcon": "book", "DisplayName": "BlueBook", "Description": "Select Icon  BlueBook"},
            "RedBook": {"ActionName": "Select Icon Book", "DisplayIcon": "book", "DisplayName": "RedBook", "Description": "Select Icon  RedBook"},
            "GreenBook": {"ActionName": "Select Icon Book", "DisplayIcon": "book", "DisplayName": "GreenBook", "Description": "Select Icon  GreenBook"},
            "PurpleBook": {"ActionName": "Select Icon Book", "DisplayIcon": "book", "DisplayName": "PurpleBook", "Description": "Select Icon  PurpleBook"},
            "SpellBook": {"ActionName": "Select Icon Book", "DisplayIcon": "book", "DisplayName": "SpellBook", "Description": "Select Icon  SpellBook"},

            "Key": {"ActionName": "Select Icon  Key", "DisplayIcon": "Key", "DisplayName": "Key", "Description": "Select Icon  BlueKey"},
            "BlueKey": {"ActionName": "Select Icon BlueKey", "DisplayIcon": "Key", "DisplayName": "BlueKey", "Description": "Select Icon  BlueKey"},
            "RedKey": {"ActionName": "Select Icon Key", "DisplayIcon": "Key", "DisplayName": "RedKey", "Description": "Select Icon  RedKey"},
            "GreenKey": {"ActionName": "Select Icon Key", "DisplayIcon": "Key", "DisplayName": "GreenKey", "Description": "Select Icon  GreenKey"},
            "PurpleKey": {"ActionName": "Select Icon Key", "DisplayIcon": "Key", "DisplayName": "PurpleKey", "Description": "Select Icon  PurpleKey"},
            "JewelKey": {"ActionName": "Select Icon JewelKey", "DisplayIcon": "Key", "DisplayName": "JewelKey", "Description": "Select Icon  JewelKey"},

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

            "Campfire": {"ActionName": "Select Icon  Campfire", "DisplayIcon": "campfire", "DisplayName": "Campfire", "Description": "Campfire"},
            "Bridge": {"ActionName": "Select Icon  Bridge", "DisplayIcon": "bridge", "DisplayName": "Bridge", "Description": "Bridge"},
            "StonePath": {"ActionName": "Select Icon  StonePath", "DisplayIcon": "stonepath", "DisplayName": "StonePath", "Description": "StonePath"},
            "Castle": {"ActionName": "Select Icon  Castle", "DisplayIcon": "castle", "DisplayName": "Castle", "Description": "Castle"},
            "City": {"ActionName": "Select Icon City", "DisplayIcon": "city", "DisplayName": "City", "Description": "City"},
            "Cottage": {"ActionName": "Select Icon  Cottage", "DisplayIcon": "cottage", "DisplayName": "Cottage", "Description": "Cottage"},
            "Forest": {"ActionName": "Select Icon  Forest", "DisplayIcon": "forest", "DisplayName": "Forest", "Description": "Forest"},
            "Dungeon": {"ActionName": "Select Icon  Dungeon", "DisplayIcon": "dungeon", "DisplayName": "Dungeon", "Description": ""},
            "ExitDoor": {"ActionName": "Select Icon  ExitDoor", "DisplayIcon": "exit", "DisplayName": "Exit", "Description": "Exit from the Door"},
            "ExitGate": {"ActionName": "Select Icon  ExitGate", "DisplayIcon": "exit", "DisplayName": "Exit", "Description": "Exit from the Gate"},
            "LockedDoor": {"ActionName": "Select Icon  LockedDoor", "DisplayIcon": "lockeddoor", "DisplayName": "LockedDoor", "Description": ""},
            "LockedChest": {"ActionName": "Select Icon  LockedChest", "DisplayIcon": "lockedchest", "DisplayName": "LockedChest", "Description": ""},
            "FirePlace": {"ActionName": "Select Icon FirePlace", "DisplayIcon": "fireplace", "DisplayName": "FirePlace", "Description": ""},
            "Door": {"ActionName": "Select Icon Door", "DisplayIcon": "door", "DisplayName": "Door", "Description": ""},
            "WoodenDoor": {"ActionName": "Select Icon WoodenDoor", "DisplayIcon": "woodendoor", "DisplayName": "WoodenDoor", "Description": "WoddenDoor"},
            "Target": {"ActionName": "Select Icon Target", "DisplayIcon": "target", "DisplayName": "Target", "Description": "Target"},
            "Well": {"ActionName": "Select Icon Well", "DisplayIcon": "well", "DisplayName": "Well", "Description": "Well"},
            "Throne": {"ActionName": "Select Icon Throne", "DisplayIcon": "throne", "DisplayName": "Throne", "Description": "Throne"},
            "Chest": {"ActionName": "Select Icon Chest", "DisplayIcon": "chest", "DisplayName": "Chest", "Description": "Chest"},
            "Chair": {"ActionName": "Select Icon Cchair", "DisplayIcon": "chair", "DisplayName": "Chair", "Description": "Chair"},
            "Bed": {"ActionName": "Select Icon Bed", "DisplayIcon": "bed", "DisplayName": "Bed", "Description": "Bed"},
            "Cauldron": {"ActionName": "Select Icon Cauldron", "DisplayIcon": "cauldron", "DisplayName": "Cauldron", "Description": "Cauldron"},
            "Shoping": {"ActionName": "Select Icon Shoping", "DisplayIcon": "shopsign", "DisplayName": "Shoping", "Description": "Shoping"},
            "Ship": {"ActionName": "Select Icon  Ship", "DisplayIcon": "ship", "DisplayName": "Ship", "Description": "Ship"},
            "Anvil": {"ActionName": "Select Icon  Anvil", "DisplayIcon": "anvil", "DisplayName": "Anvil", "Description": "Anvil"},
            "Mug": {"ActionName": "Select Icon  Mug", "DisplayIcon": "mug", "DisplayName": "Mug", "Description": "Mug"},

            "SunRise": {"ActionName": "Select Icon  SunRise", "DisplayIcon": "sunrise", "DisplayName": "SunRise", "Description": "SunRice"},
            "SunSet": {"ActionName": "Select Icon  SunSet", "DisplayIcon": "sunrise", "DisplayName": "SunSet", "Description": "SunSet"},
            "Time": {"ActionName": "Select Icon  Time", "DisplayIcon": "time", "DisplayName": "Time", "Description": "Time"},
            "Tree": {"ActionName": "Select Icon  Tree", "DisplayIcon": "tree", "DisplayName": "Tree", "Description": "Tree"},
            "TimeHourGlass": {"ActionName": "Select Icon  TimeHourGlass", "DisplayIcon": "hourglass", "DisplayName": "TimeHourGlass", "Description": "TimeHourGlass"}
        }
        # --------------------------------------------------------------------------------------------------------------
        self.Icon_Attack = Icon_(self.icons["Attack"], self.Action)
        self.Icon_Talk = Icon_(self.icons["Talk"], self.Action)
        self.Icon_Accept = Icon_(self.icons["Accept"], self.Action)
        self.Icon_Anvil = Icon_(self.icons["Anvil"], self.Action)
        self.Icon_Apple = Icon_(self.icons["Apple"], self.Action)
        self.Icon_Bed = Icon_(self.icons["Bed"], self.Action)
        self.Icon_BlueBook = Icon_(self.icons["BlueBook"], self.Action)
        self.Icon_BlueKey = Icon_(self.icons["BlueKey"], self.Action)
        self.Icon_BluePotion = Icon_(self.icons["BluePotion"], self.Action)
        self.Icon_Book = Icon_(self.icons["Book"], self.Action)
        self.Icon_Bridge = Icon_(self.icons["Bridge"], self.Action)
        self.Icon_BrokenHeart = Icon_(self.icons["BrokenHeart"], self.Action)
        self.Icon_Campfire = Icon_(self.icons["Campfire"], self.Action)
        self.Icon_Castle = Icon_(self.icons["Castle"], self.Action)
        self.Icon_Cauldron = Icon_(self.icons["Cauldron"], self.Action)
        self.Icon_Chair = Icon_(self.icons["Chair"], self.Action)
        self.Icon_Chest = Icon_(self.icons["Chest"], self.Action)
        self.Icon_City = Icon_(self.icons["City"], self.Action)
        self.Icon_CloseScroll = Icon_(self.icons["CloseScroll"], self.Action)
        self.Icon_Cottage = Icon_(self.icons["Cottage"], self.Action)
        self.Icon_Door = Icon_(self.icons["Door"], self.Action)
        self.Icon_Dress = Icon_(self.icons["Dress"], self.Action)
        self.Icon_Dungeon = Icon_(self.icons["Dungeon"], self.Action)
        self.Icon_EvilBook = Icon_(self.icons["EvilBook"], self.Action)
        self.Icon_ExitDoor = Icon_(self.icons["ExitDoor"], self.Action)
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
        self.SEffect_Flute2     = SoundEffect_(self.SoundEffects["Flute2"],     self.Action)
        self.SEffect_Flute1     = SoundEffect_(self.SoundEffects["Flute1"],     self.Action)
        self.SEffect_Button     = SoundEffect_(self.SoundEffects["Button"],     self.Action)
        self.SEffect_Menu       = SoundEffect_(self.SoundEffects["Menu"],       self.Action)
        self.SEffect_Spooky     = SoundEffect_(self.SoundEffects["Spooky"],     self.Action)
        self.SEffect_Error      = SoundEffect_(self.SoundEffects["Error"],      self.Action)
        self.SEffect_Spell2     = SoundEffect_(self.SoundEffects["Spell2"],     self.Action)
        self.SEffect_Potion     = SoundEffect_(self.SoundEffects["Potion"],     self.Action)
        self.SEffect_Ominous    = SoundEffect_(self.SoundEffects["Ominous"],    self.Action)
        self.SEffect_Fireplace  = SoundEffect_(self.SoundEffects["Fireplace"],  self.Action)
        self.SEffect_DarkMagic  = SoundEffect_(self.SoundEffects["DarkMagic"],  self.Action)
        self.SEffect_Fireball   = SoundEffect_(self.SoundEffects["Fireball"],   self.Action)
        self.SEffect_Clap       = SoundEffect_(self.SoundEffects["Clap"],       self.Action)
        self.SEffect_Draw       = SoundEffect_(self.SoundEffects["Draw"],       self.Action)
        self.SEffect_Eat        = SoundEffect_(self.SoundEffects["Eat"],        self.Action)
        self.SEffect_Hammer     = SoundEffect_(self.SoundEffects["Hammer"],     self.Action)
        self.SEffect_Lock       = SoundEffect_(self.SoundEffects["Lock"],       self.Action)
        self.SEffect_Pocket     = SoundEffect_(self.SoundEffects["Pocket"],     self.Action)
        self.SEffect_Sheathe    = SoundEffect_(self.SoundEffects["Sheathe"],    self.Action)
        self.SEffect_Unlock     = SoundEffect_(self.SoundEffects["Unlock"],     self.Action)
        self.SEffect_Unpocket   = SoundEffect_(self.SoundEffects["Unpocket"],   self.Action)
        self.SEffect_Write      = SoundEffect_(self.SoundEffects["Write"],      self.Action)
        # --------------------------------- Musical Sounds ---------------------------------
        self.SEffect_Danger1    = SoundEffect_(self.SoundEffects["Danger1"],    self.Action)
        self.SEffect_Danger2    = SoundEffect_(self.SoundEffects["Danger2"],    self.Action)
        self.SEffect_Danger3    = SoundEffect_(self.SoundEffects["Danger3"],    self.Action)
        self.SEffect_Dramatic   = SoundEffect_(self.SoundEffects["Dramatic"],   self.Action)
        self.SEffect_Explorer   = SoundEffect_(self.SoundEffects["Explorer"],   self.Action)
        self.SEffect_Grief      = SoundEffect_(self.SoundEffects["Grief"],      self.Action)
        self.SEffect_Kingdom    = SoundEffect_(self.SoundEffects["Kingdom"],    self.Action)
        self.SEffect_LivelyMusic = SoundEffect_(self.SoundEffects["LivelyMusic"], self.Action)
        self.SEffect_Ominous    = SoundEffect_(self.SoundEffects["Ominous"],    self.Action)
        self.SEffect_Peaceful   = SoundEffect_(self.SoundEffects["Peaceful"],   self.Action)
        self.SEffect_Serenade   = SoundEffect_(self.SoundEffects["Serenade"],   self.Action)
        self.SEffect_Serenity   = SoundEffect_(self.SoundEffects["Serenity"],   self.Action)

        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # ===============================================  VISUAL EFFECTS  =============================================
        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # ------------------------------------ DICTIONARIES -----------------------------------------
        self.VisualEffects = {
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
        self.VEffect_Aura           = VisualEffect_(self.VisualEffects["Aura"], self.Action)
        self.VEffect_Blood          = VisualEffect_(self.VisualEffects["Blood"], self.Action)
        self.VEffect_Brew           = VisualEffect_(self.VisualEffects["Brew"], self.Action)
        self.VEffect_Blackflame     = VisualEffect_(self.VisualEffects["Blackflame"], self.Action)
        self.VEffect_Campfire       = VisualEffect_(self.VisualEffects["Campfire"], self.Action)
        self.VEffect_Death          = VisualEffect_(self.VisualEffects["Death"], self.Action)
        self.VEffect_Explosion      = VisualEffect_(self.VisualEffects["Explosion"], self.Action)
        self.VEffect_Heart          = VisualEffect_(self.VisualEffects["Heart"], self.Action)
        self.VEffect_Heartbroken    = VisualEffect_(self.VisualEffects["Heartbroken"], self.Action)
        self.VEffect_Magic          = VisualEffect_(self.VisualEffects["Magic"], self.Action)
        self.VEffect_Poof           = VisualEffect_(self.VisualEffects["Poof"], self.Action)
        self.VEffect_Poison         = VisualEffect_(self.VisualEffects["Poison"], self.Action)
        self.VEffect_Resurrection   = VisualEffect_(self.VisualEffects["Resurrection"], self.Action)
        self.VEffect_Skulls         = VisualEffect_(self.VisualEffects["Skulls"], self.Action)
        self.VEffect_Spiralflame    = VisualEffect_(self.VisualEffects["Spiralflame"], self.Action)

        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # ================================================  NARRATIONS  ================================================
        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        N_FP01 = ["Wow! This place is sooo Beautiful !!!", "There is someone standing there. Let's ask them."]
        self.N_FP01_Bob = Message_(N_FP01, self.Action)

        N_FP02 = ["Select one of Blue or Red Potions Carefully"]
        self.N_FP02_Bob_Well_Help = Message_(N_FP02, self.Action)

        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # ==================================================  DIALOGS  =================================================
        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # ------------------------------------ @ FOREST PATH @ -----------------------------------------
        self.D_FP00_Bob_Die = Message_(["Wrong Step....",
                                        "____Choose____",
                                        "[RESTART|RESTART] :::: [QUIT|QUIT]"], self.Action)
        # self.D_FP00_Bob_Die_Expressions = ["sad", "sad","sad"]

        self.D_FP01_Bob_Angel = Message_(["Bob : Hello, What place is it?",
                                  "Angel : Hello Bob this is a magical forest. Only the luckiest can come here.",
                                  "Bob : oh wow. I am here to get some powers.",
                                  "Angel : Oh then you have to finish the task to get that.",
                                  "If you ready, got to well and Select one from the potions (RED | BLUE). Remember, only one gives you Power."
                                 ], self.Action)
        self.D_FP01_Bob_Angel_Expressions = ["neutral", "happy","surprised", "sad"]

        self.D_FP02_Bob_Angel = Message_(["Bob: I have to save my wife. Can you please help me which one to select?",
                                            "Angel: Sorry young man, I am prohibited to tell that and you have to choose wisely.",
                                            "Angel: As you are here for saving life, all I can help you is 'Go Opposite Direction'."
                                          ], self.Action)

        self.D_FP02_Bob_Angel_BluePotion = Message_(["Bob: What happened now?",
                                                     "Angel: Unluckily, you got no Power.",
                                                     "Angel: But, I can give one spell use this at right time.",
                                                     "Angel: [ OmBhimBhush ]"],
                                                    self.Action
                                                    )
        self.D_FP03_Bob_Angel_RedPotion = Message_(["Bob: Oh my Goddess, I feel so Strong now. What is next Goddess?",
                                                    "Angel: Lucky, You got enoughstrength power to complete the other tasks.",
                                                    "Angel: And take this Scroll also and Go to the City.",
                                                    "Angel: You will be guided by someone there.",
                                                    "Angel: Remember, Choose the steps carefully, it's a dangerous place."],
                                                   self.Action
                                                   )

        # ------------------------------------ @ CASTLE BED ROOM @ -----------------------------------------
        self.D_CBR01_Bob_Candy_Talk_1 = Message_(["Bob: Oh! My dear Candy, what happened?",
                                 "Candy: I do not know dear, I feel like I am diying.",
                                 "Bob: Do not worry dear. I found the path to find the cure. Wait, I will all your sister Lilly.",
                                 "Candy: Okay dear!!!"], self.Action)
        self.D_CBR02_Bob_LillyS_Talk = Message_(["Bob: Lilly, Candy is sick now. Can you take care of her?",
                                                 "Bob: In sometime, I will go to bring the cure for your sister.",
                                                 "Lilly: Okay, I will look after her. You take care.",
                                                 "Bob: Tell me if you need anything.",
                                                 "Lilly: Okay!"
                                                 ], self.Action)
        self.D_CBR03_Bob_Candy_Talk_2 = Message_(["Bob: No worries, I will go, find, and bring the Cure. Lilly will take care of you till then",
                                                   "Candy: No dear, you stay with me in the last minute of me diying.",
                                                  "Bob: Do not say that, I can save you. Please let me save you.",
                                                  "Candy: Okay dear! Take care."
                                                  ], self.Action)

        # ------------------------------------ @ CITY @ -----------------------------------------
        self.D05_Bob_JimS = Message_(["Bob: Hello, I am new here.",
                             "Can you tell me how I can meet AngelOfDeath?",
                             "Jim: Oh Sorry, I don't. I am also new for this place."
                             ], self.Action)
        self.D06_Bob_JackS = Message_(["Bob: Hello, I am new here. \nCan you tell me how I can meet AngelOfDeath.",
                              "Jack: Oh yes, I knew her. She comes rarely. \nyou can wait at Fountain to meet her."
                              ], self.Action)

        self.D07_Bob_TomS = Message_(["Bob: Hello, I am new here. \nCan you tell me how I can meet AngelOfDeath.",
                             "Tom: You are not belonging here, Get out."
                             ], self.Action)
        self.D08_Bob_AngelOfDeath = Message_(["AOD: Hello young man, what's the matter.",
                                     "BOB: My wife is sick. I am looking for Angel here who can help me.",
                                     "AOD: Where are you coming from? and Who sent you here?",
                                     "BOB: Angel sent me from Forest. Please help me to find her.",
                                     "AOD: Nearby there is a fountain with Eagle Statue which has some tasks. You have to complete to meet her."
                                     ], self.Action)

        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # =============================================  LISTS for ENTITES  ============================================
        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        self.L01_Well           = [f"{self.Item_BluePotion.Name}", f"{self.Item_RedPotion.Name}"]
        self.L02_CBR_Closet     = [f"{self.Item_BlueCloth.Name}", f"{self.Item_Money.Name}"]
        # self.L03_CBR_Lilly_S  = ["Fireplace"]
        #self.L04_CBR_Door      = ["Forest"]
        self.L03_C_Fountain     = [f"{self.Item_BlueBook.Name}, Find Spell in this Book", f"{self.Item_RedBook.Name}, Find Spell in this Book", f"{self.Item_EvilBook.Name}, Find Spell in this Book", f"{self.Item_Help.Name}, Show Hint|Help"]
