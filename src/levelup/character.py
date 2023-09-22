from levelup.position import Position
from levelup.direction import Direction
from levelup.gamemap import GameMap

class Character:
    name = 'Character'

    def __init__(self, character_name):
        if character_name != "":
            self.name = character_name

    def enterMap(self, GameMap :GameMap):
        self.GameMap = GameMap
        self.current_position = self.GameMap.starting_position

