from unittest import TestCase
from levelup.character import Character

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
        testvar = testobj.enterMap()
        self.assertEqual(testvar, 'Yes')

class TestCharacterMapPosition(TestCase):
    def test_init(self):
        testobj = Character("")
    #    stubbed_map = FakeMap()
    #    testobj.enterMap(FakeMap)
    #    testobj.getPosition() 
    #    self.assertEqual(Position, 3,4)