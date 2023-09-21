class Position:
    
    x = 1
    y = 2

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    
    def setPosition(self, x, y):
        newPosition = list(self.point)
        newPosition[0] = x
        newPosition[1] = y
        self.point = tuple(newPosition)