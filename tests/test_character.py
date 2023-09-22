from unittest import TestCase
from levelup.character import Character
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
        testobj.enterMap(stubbed_map)
        self.assertEqual(stubbed_map, testobj.GameMap)

class TestCharacterMapPosition(TestCase):
    def test_init(self):
        testobj = Character("")
        stubbed_map = FakeMap()
        testobj.enterMap(stubbed_map)
    #    testobj.getPosition() 
    #    self.assertEqual(Position, 3,4)