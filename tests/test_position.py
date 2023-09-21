import unittest
from levelup.position import Position

class TestPosition(unittest.TestCase):

    def test_initialization(self):
        testobj = Position(1,1)
        expected_x_coordinate = 1
        expected_y_coordinate = 1
        self.assertEqual(
            expected_x_coordinate,
            testobj.x
        )
        self.assertEqual(
            expected_y_coordinate,
            testobj.y
        )

    def test_assignment(self):
        assigned_x = 2
        assigned_y = 2
        testobj = Position(assigned_x, assigned_y)
        self.assertEqual(
            assigned_x,
            testobj.x
        )
        self.assertEqual(
            assigned_y,
            testobj.y
        )

