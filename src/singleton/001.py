"""
This way of implemeting the Singleton pattern doesn't guard the class from calling the method __init__. Nontheless both instance db1 and db2 are the same object, because both have the same signature. But you might want to avoid that behavior in your class.
"""


import random

class Database:
    _instance = None

    def __init__(self):
        i = random.randint(1, 100)
        print('Initializing object with id = ', i)

    def __new__(cls, *args, **kwargs):
        if (not cls._instance):
            cls._instance = super(Database, cls).__new__(cls, *args, **kwargs)

        return cls._instance


if __name__ == '__main__':
    db1 = Database()
    db2 = Database()
    print(db1 == db2)