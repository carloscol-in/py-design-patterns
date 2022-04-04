"""
Monostate implementation.

In a monostate implementation you put all state of an object into an static variable, but you allow creation of instances. Therefore, this instances will be sharing state.
"""

class CEO:
    __shared_state = {
        'name': 'Bob',
        'age': 30
    }

    def __init__(self):
        self.__dict__ = self.__shared_state

    def __str__(self):
        return f'{self.__shared_state["name"]} is {self.__shared_state["age"]} years old.'

class Monostate:
    _shared_state = {}

    def __new__(self, *args, **kwargs):
        # get the object by calling the super().__new__()
        obj = super(Monostate, self).__new__(self, *args, **kwargs)

        # get the object class name
        obj_type = obj.__class__.__name__

        # use this to separate states by child class
        self._shared_state.setdefault(obj_type, {})
        obj.__dict__ = self._shared_state[obj_type]

        # return obj
        return obj


class CFO(Monostate):
    def __new__(self, *args, **kwargs):
        return super().__new__(self, *args, **kwargs)

    def __init__(self):
        self.name = 'name'
        self.age = 0

    def __str__(self):
        return f'The CFO is {self.name} and is {self.age} years old'

class CTO(Monostate):
    def __init__(self):
        self.name = 'Default'
        self.age = 0

    def __str__(self):
        return f'The CTO is {self.name} and is {self.age} years old'

if __name__ == '__main__':
    """Notice how CFO and CTO object share state since both inherit from Monostate class.
    """
    cfo1 = CFO()
    cfo2 = CFO()

    cto1 = CTO()
    cto2 = CTO()

    print(cfo1)
    print(cfo2)

    cfo1.age = 35
    cfo2.name = 'Mary'
    print(cfo1)
    print(cfo2)

    cto1.name = 'Tony'

    print(cto1)
    print(cto2)

    cto2.age = 40

    print(cto1)
    print(cto2)
