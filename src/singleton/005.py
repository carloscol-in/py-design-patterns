"""
Singleton testability.

"""


from abc import ABC, abstractmethod
import os
import unittest


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if (cls not in cls._instances):
            cls._instances[cls] = super(
                Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=Singleton):
    def __init__(self):
        self.population = {}
        dirname = os.path.dirname(__file__)
        with open(f'{dirname}/population.txt', 'r') as f:
            lines = f.readlines()
            for i in range(0, len(lines), 2):
                self.population[lines[i].strip()] = int(lines[i + 1].strip())

class AbstractRepository(ABC):
    @abstractmethod
    def total_population(self, cities):
        """Get the total population.

        Args:
            cities (str): Cities you want to aggregate and get total population.

        Returns:
            int: Result of total population in the cities you passed as parameter.
        """

class FileRepository(AbstractRepository):
    def total_population(self, cities):
        result = 0

        for c in cities:
            result += Database().population[c]

        return result

class DummyRepository(AbstractRepository):
    def __init__(self):
        self.population = {
            'Tokyo': 3,
            'Sao Paulo': 4,
            'Mexico City': 5,
            'New York': 2
        }

    def total_population(self, cities):
        result = 0

        for c in cities:
            result += self.population[c]

        return result

class SingletonTest(unittest.TestCase):
    def test_is_singleton(self):
        db1 = Database()
        db2 = Database()
        self.assertEqual(db1, db2)

    def test_singleton_total_population(self):
        fr = DummyRepository()
        self.assertEqual(fr.total_population(['Tokyo', 'Mexico City']), 8)

if __name__ == '__main__':
    unittest.main()