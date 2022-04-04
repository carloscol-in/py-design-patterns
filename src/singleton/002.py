"""
Implementation using a decorator.
"""

import random

def singleton(class_):
    instances = {}

    def get_instance(*args, **kwargs):
        if (class_ not in instances):
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return get_instance


@singleton
class Database:
    def __init__(self):
        i = random.randint(1, 100)
        print('id = ', i)


if __name__ == '__main__':
    db1 = Database()
    db2 = Database()

    print(db1 == db2)