from levelup.map import FakeMap
from levelup.character import Character
from levelup.controller import Direction
from levelup.position import Position

class FakeCharacter (Character):

    is_move_called = False
    is_enter_map_called = False
    last_move_direction = None

    def __init__(self,character_name):
        self.current_position = Position (5,5)