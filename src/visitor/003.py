
from abc import ABC


def _qualname(obj):
    """Get the fully-qualified name of an object (including module)."""
    return obj.__module__ + '.' + obj.__qualname__


def _declaring_class(obj):
    """Get the name of the class that declared an object."""
    name = _qualname(obj)
    return name[:name.rfind('.')]


# Stores the actual visitor methods
_methods = {}


# Delegating visitor implementation
def _visitor_impl(self, arg):
    """Actual visitor method implementation."""
    method = _methods[(_qualname(type(self)), type(arg))]
    return method(self, arg)

def visitor(arg_type):
    def decorator(fn):
        declaring_class = _declaring_class(fn)
        _methods[(declaring_class, arg_type)] = fn

        return _visitor_impl

    return decorator

class Expression(ABC):
    def print(self, b):
        return ExpressionPrinter.print(self, b)

class DoubleExpression(Expression):
    def __init__(self, value):
        self.value = value
        
    def accept(self, visitor):
        visitor.visit(self)

class AdditionExpression(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

class SubtractionExpression(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right
        
    def accept(self, visitor):
        visitor.visit(self)

class ExpressionPrinter:
    def __init__(self):
        self.buffer = []

    @visitor(DoubleExpression)
    def visit(self, de):
        self.buffer.append(str(de.value))

    @visitor(AdditionExpression)
    def visit(self, ae):
        self.buffer.append('(')
        self.visit(ae.left)
        self.buffer.append('+')
        self.visit(ae.right)
        self.buffer.append(')')

    @visitor(SubtractionExpression)
    def visit(self, ae):
        self.buffer.append('(')
        self.visit(ae.left)
        self.buffer.append('-')
        self.visit(ae.right)
        self.buffer.append(')')

    def __str__(self):
        return ''.join(self.buffer)

class ExpressionEvaluator:
    def __init__(self):
        self.value = None

    @visitor(DoubleExpression)
    def visit(self, de):
        self.value = de.value

    @visitor(AdditionExpression)
    def visit(self, ae):
        self.visit(ae.left)
        temp = self.value
        self.visit(ae.right)
        self.value += temp


if __name__ == '__main__':
    e = AdditionExpression(
        DoubleExpression(1),
        AdditionExpression(
            DoubleExpression(2),
            DoubleExpression(3)
        )
    )

    printer = ExpressionPrinter()
    printer.visit(e)

    evaluator = ExpressionEvaluator()
    evaluator.visit(e)

    print(printer, '=', evaluator.value)