from typing import Iterable
from abc import ABC


class Summable(Iterable, ABC):
    @property
    def sum(self):
        values = []
        for s in self:
            if type(s) == SingleValue and s.value:
                values.append(s.value)
                continue
            values.append(s)
        return sum(values)


class SingleValue(Summable):
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        yield self


class ManyValues(list, Summable):
    def __init__(self, *args):
        self.extend(args)

    def append(self, value):
        if type(value) == ManyValues:
            super(ManyValues, self).extend(value)
        else:
            super(ManyValues, self).append(value)

if __name__ == '__main__':
    s1 = SingleValue(2)
    s2 = SingleValue(4)
    mv1 = ManyValues(3, 5, s1, s2)

    print(mv1.sum)