from copy import deepcopy

class Token:
    def __init__(self, value=0):
        self.value = value


class Memento(list):
    pass


class TokenMachine:
    def __init__(self):
        self.tokens = []
        self.changes = Memento()
        self.current = 0

    def add_token_value(self, value):
        return self.add_token(Token(value))

    def add_token(self, token):
        # todo
        self.tokens.append(token)
        return Memento(deepcopy(self.tokens))

    def revert(self, memento):
        # todo
        if memento:
            self.tokens = memento
            return memento
        return None
            