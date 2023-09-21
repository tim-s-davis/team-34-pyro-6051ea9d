import unittest
from levelup.position import Position

class TestPosition(unittest.TestCase):

    def test_initialization(self):
        testobj = Position()
        expected_x_coordinate = 0
        expected_y_coordinate = 0
        self.assertEqual(
            expected_x_coordinate,
            testobj.point[0]
        )
        self.assertEqual(
            expected_y_coordinate,
            testobj.point[1]
        )

    def test_assignment(self):
        testobj = Position()
        assigned_x = 1
        assigned_y = 1
        testobj.setPosition(assigned_x, assigned_y)
        self.assertEqual(
            assigned_x,
            testobj.point[0]
        )
        self.assertEqual(
            assigned_y,
            testobj.point[1]
        )

