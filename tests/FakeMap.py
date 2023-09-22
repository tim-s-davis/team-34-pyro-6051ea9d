from levelup.gamemap import GameMap
from levelup.position import Position
from levelup.controller import Direction

class FakeMap (GameMap):

    STUBBED_X = 3
    STUBBED_Y = 4

    def calculate_new_position(self, current_position: Position, direction: Direction) -> Position:
        return Position(self.STUBBED_X, self.STUBBED_Y)