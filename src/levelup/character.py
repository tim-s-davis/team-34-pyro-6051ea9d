from levelup.position import Position
from levelup.direction import Direction
from levelup.gamemap import GameMap

class Character:
    name = 'Character'
    current_position :Position = Position(1, 1)
    GameMap :GameMap = GameMap()

    def __init__(self, character_name):
        if character_name != "":
            self.name = character_name

    def move(self, Direction :Direction) -> None:
        self.current_position = self.GameMap.calculate_new_position(
            self.current_position, Direction)

    def enter_map(self, GameMap :GameMap):
        self.GameMap = GameMap
        self.current_position = self.GameMap.starting_position

