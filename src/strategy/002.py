import cmath

from abc import ABC


class DiscriminantStrategy(ABC):
    def calculate_discriminant(self, a, b, c):
        return ((b ** 2) - (4 * a * c))


class OrdinaryDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        # todo
        discriminant = super().calculate_discriminant(a, b, c)
        return discriminant


class RealDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        # todo
        discriminant = super().calculate_discriminant(a, b, c)
        
        if discriminant < 0:
            return float('nan')
            
        return discriminant


class QuadraticEquationSolver:
    def __init__(self, strategy):
        self.strategy = strategy

    def solve(self, a, b, c):
        """ Returns a pair of complex (!) values """
        # todo
        
        discriminant = complex(self.strategy.calculate_discriminant(a, b, c), 0)

        sqrt_disc = cmath.sqrt(discriminant)
            
        return (
            (-b + sqrt_disc) / (2 * a),
            (-b - sqrt_disc) / (2 * a)
        )


if __name__ == '__main__':
    qes = QuadraticEquationSolver(OrdinaryDiscriminantStrategy())

    result = qes.solve(4, 9, 2)

    print(result)