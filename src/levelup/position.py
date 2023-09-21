class Position:
    point = (0,0)
    
    def setPosition(self, x, y):
        newPosition = list(self.point)
        newPosition[0] = x
        newPosition[1] = y
        self.point = tuple(newPosition)