
from GlobalVariables import Variables
from Places import CastleBedroom_
testingValues = {"Name": "CastleBedRoom",
                 "Type": "CastleBedRoom",
                 "Door": f"CastleBedRoom.Door",
                 "Chest": f"CastleBedRoom.Chest",
                 "Couch": f"CastleBedRoom.Couch",
                 "Couch_Left": f"CastleBedRoom.Couch.Left",
                 "Couch_Right": f"CastleBedRoom.Couch.Right",
                 "Couch_Middle": f"CastleBedRoom.Couch.Seat",
                 "Fireplace": f"CastleBedRoom.Fireplace",
                 "Table": f"CastleBedRoom.Table",
                 "Table_Left": f"CastleBedRoom.Table.Left",
                 "Table_Right": f"CastleBedRoom.Table.Right",
                 "Table_FrontLeft": f"CastleBedRoom.Table.FrontLeft",
                 "Table_FrontRight": f"CastleBedRoom.Table.FrontRight",
                 "Table_BackLeft": f"CastleBedRoom.Table.BackLeft",
                 "Table_BackRight": f"CastleBedRoom.Table.BackRight",
                 "Chair_Right": f"CastleBedRoom.RightChair",
                 "Chair_Left": f"CastleBedRoom.LeftChair",
                 "SmallTable": f"CastleBedRoom.SmallTable",
                 "Bed": f"CastleBedRoom.Bed",
                 "Bed_Left": f"CastleBedRoom.Bed.Left",
                 "Bed_Middle": f"CastleBedRoom.Bed",
                 "Bed_Right": f"CastleBedRoom.Bed.Right",
                 "Closet": f"CastleBedRoom.Closet"
                 }

V = Variables()
cbr_Dict = V.places["CastleBedRoom"]  # {"Name": "CastleBedRoom", "Type": "CastleBedroom"}
CBR = CastleBedroom_(cbr_Dict, V.Action, "Testing")

import unittest
class TestCastleBedRoom(unittest.TestCase):

    def test_CBR_ClassVariables(self):
        for inputValue in testingValues:
            actual = eval("CBR." + inputValue)
            expected = testingValues[inputValue]
            self.assertAlmostEqual(actual, expected)

    def test_CBR_Method(self):
        actual = CBR.CreatePlace()
        expected = 'CreatePlace(CastleBedRoom, CastleBedRoom)'
        self.assertAlmostEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()

