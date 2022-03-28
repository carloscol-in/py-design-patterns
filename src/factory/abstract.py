import abc
from enum import Enum, auto


class HotDrink(abc.ABC):
    def consume(self):
        pass

class Tea(HotDrink):
    def consume(self):
        print('This tea is delicious')

class Coffee(HotDrink):
    def consume(self):
        print('This coffee tastes so good!')


class TeaFactory:
    def prepare(self, amount):
        print(f'Preparing {amount}ml of tea')
        return Tea()

class CoffeeFactory:
    def prepare(self, amount):
        print(f'Grind some beans, boild {amount}ml of water, and mix')
        return Coffee()


def make_drink(type):
    if type == "tea":
        return TeaFactory().prepare(200)
    elif type == "coffee":
        return CoffeeFactory().prepare(400)
    else:
        return None

class HotDrinkMachine:
    class AvailableDrink(Enum):
        COFFEE = auto()
        TEA = auto()

    factories = []
    initialized = False

    def __init__(self):
        if not self.initialized:
            self.initialized = True
            for d in self.AvailableDrink:
                name = d.name.capitalize()
                factory_name = f'{name}Factory'
                factory_instance = eval(factory_name)
                self.factories.append((factory_name, factory_instance))

    def make_drink(self):
        print('Available drinks')
        for i, f in enumerate(self.factories):
            print(i, f[0])

        idx = int(input(f'Please pick a drink 0 - {len(self.factories)}'))

        amount = int(input('Specify amount in ml'))

        return self.factories[idx][1]().prepare(amount)

if __name__ == "__main__":
    hdm = HotDrinkMachine()

    d = hdm.make_drink()

    d.consume()