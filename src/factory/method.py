from enum import Enum, auto
from math import cos, sin


class Point:
    # ! instead of something like this
    # def __init__(self, a, b, system=CoordinateSystem.CARTESIAN):
    #     if system == CoordinateSystem.CARTESIAN:
    #         self.x = a
    #         self.y = b
    #     elif system == CoordinateSystem.POLAR:
    #         self.x = a * cos(b)
    #         self.y = a * sin(b)

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'x: {self.x}, y: {self.y}'

    # *
    # * These static methods to construct an object with so
    # * many types of initializations is better.
    # *
    
    @staticmethod
    def new_cartesian_point(x, y):
        return Point(x, y)

    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho * cos(theta), rho * sin(theta))

if __name__ == '__main__':
    p = Point(2, 3)
    p2 = Point.new_polar_point(2, 0.987)
    print(p, p2)