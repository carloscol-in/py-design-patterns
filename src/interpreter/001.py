from enum import Enum, auto


class Token:
    class Type(Enum):
        INTEGER = auto()
        PLUS = auto()
        MINUS = auto()
        LPAREN = auto()
        RPAREN = auto()

    def __init__(self, type, text):
        self.type = type
        self.text = text
    
    def __str__(self):
        return f'`{self.text}`'

def lex(input):
    result = []

    digits = []

    for i, c in enumerate(input):
        if c == '+':
            result.append(Token(Token.Type.PLUS, c))
        elif c == '-':
            result.append(Token(Token.Type.MINUS, c))
        elif c == '(':
            result.append(Token(Token.Type.LPAREN, c))
        elif c == ')':
            result.append(Token(Token.Type.RPAREN, c))
        elif c.isdigit():
            digits.append(c)
        
            if (i + 1 < len(input) and not input[i + 1].isdigit()) or (i + 1 == len(input)):
                result.append(Token(Token.Type.INTEGER, ''.join(digits)))
                digits = []

    return result


class Integer:
    def __init__(self, value):
        self.value = value


class BinaryExpression:
    class Type(Enum):
        ADDITION = auto()
        SUBTRACTION = auto()

    def __init__(self):
        self.type = None
        self.left = None
        self.right = None

    @property
    def value(self):
        if self.type == self.Type.ADDITION:
            return self.left.value + self.right.value
        else:
            return self.left.value - self.right.value


def parse(tokens):
    result = BinaryExpression()
    have_lhs = False
    i = 0
    while i < len(tokens):
        token = tokens[i]

        if token.type == Token.Type.INTEGER:
            integer = Integer(int(token.text))

            if not have_lhs:
                result.left = integer
                have_lhs = True
            else:
                result.right = integer
        elif token.type == Token.Type.PLUS:
            result.type = BinaryExpression.Type.ADDITION
        elif token.type == Token.Type.MINUS:
            result.type = BinaryExpression.Type.SUBTRACTION
        elif token.type == Token.Type.LPAREN:
            j = i
            while j < len(tokens):
                if tokens[j].type == Token.Type.RPAREN:
                    break
                j += 1
            subexpression = tokens[i+1:j]
            element = parse(subexpression)
            if not have_lhs:
                result.left = element
                have_lhs = True
            else:
                result.right = element
            i = j
        i += 1
    return result

def calc(input):
    tokens = lex(input)

    parsed = parse(tokens)

    print(f'{input} = {parsed.value}')

if __name__ == '__main__':
    calc('(23+2)-(16-5)') # 12