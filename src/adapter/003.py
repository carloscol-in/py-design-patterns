class Square:
    def __init__(self, side=0):
        self.side = side


def calculate_area(rc):
    return rc.width * rc.height


class SquareToRectangleAdapter:
    def __init__(self, square):
        self.sq = square

    @property
    def height(self):
        return self.sq.side

    @property
    def width(self):
        return self.sq.side
