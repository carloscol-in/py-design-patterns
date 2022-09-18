
from abc import ABC


class Expression(ABC):
    def print(self, b):
        return ExpressionPrinter.print(self, b)

class DoubleExpression(Expression):
    def __init__(self, value):
        self.value = value

    def print(self, buffer):
        buffer.append(str(self.value))

class AdditionExpression(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

class ExpressionPrinter:
    @staticmethod
    def print(exp, buffer):
        if isinstance(exp, DoubleExpression):
            buffer.append(str(exp.value))
        elif isinstance(exp, AdditionExpression):
            buffer.append('(')
            ExpressionPrinter.print(exp.left, buffer)
            buffer.append('+')
            ExpressionPrinter.print(exp.right, buffer)
            buffer.append(')')




if __name__ == '__main__':
    e = AdditionExpression(
        DoubleExpression(1),
        AdditionExpression(
            DoubleExpression(2),
            DoubleExpression(3)
        )
    )

    buffer = []

    e.print(buffer)

    print(''.join(buffer))