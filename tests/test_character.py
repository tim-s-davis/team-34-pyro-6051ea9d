from unittest import TestCase
from levelup.character import Character
from levelup.controller import Direction
from FakeMap import FakeMap

class TestCharacterInitWithName(TestCase):
    def test_init(self):
        ARBITRARY_NAME = "MyName"
        testobj = Character(ARBITRARY_NAME)
        self.assertEqual(ARBITRARY_NAME, testobj.name)

class TestCharacterInitWithoutName(TestCase):
    def test_init(self):
        testobj = Character("")
        self.assertEqual('Character', testobj.name)

class TestCharacterEnterMap(TestCase):
    def test_init(self):
        testobj = Character("")
        stubbed_map = FakeMap()
        testobj.enter_map(stubbed_map)
        self.assertEqual(stubbed_map, testobj.GameMap)

class TestCharacterMapPosition(TestCase):
    def test_init(self):
        testobj = Character("")
        stubbed_map = FakeMap()
        testobj.enter_map(stubbed_map)
        self.assertEqual(stubbed_map, testobj.GameMap)
        self.assertEqual(testobj.current_position, stubbed_map.starting_position)

    def test_move_updates_position(self):
        testobj = Character("")
        stubbed_map = FakeMap()
        testobj.enter_map(stubbed_map)
        
        testobj.move(Direction.EAST)

        self.assertEqual(stubbed_map.STUBBED_X, testobj.current_position.x)
        self.assertEqual(stubbed_map.STUBBED_Y, testobj.current_position.y)