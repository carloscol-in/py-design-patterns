from enum import Enum, auto
from math import cos, sin


class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'x: {self.x}, y: {self.y}'

    # *
    # * These static methods to construct an object with so
    # * many types of initializations is better.
    # *
    class PointFactory:
        def new_cartesian_point(self, x, y):
            return Point(x, y)

        def new_polar_point(self, rho, theta):
            return Point(rho * cos(theta), rho * sin(theta))

    factory = PointFactory()

if __name__ == '__main__':
    p1 = Point.factory.new_cartesian_point(3, 4)
    p2 = Point.factory.new_polar_point(5, 0.67)
    print(p1, p2)