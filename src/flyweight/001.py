import random
import string
from typing import List


class User:
    def __init__(self, name):
        self.name = name

class User2:
    strings: List = []

    def __init__(self, full_name):
        def get_or_add(s):
            if s in self.strings:
                return self.strings.index(s)
            else:
                self.strings.append(s)
                return len(self.strings) - 1

        self.names = [get_or_add(x) for x in full_name.split(' ')]

    def __str__(self):
        return ' '.join([self.strings[x] for x in self.names])

def random_string(string_length):
    chars = string.ascii_lowercase
    return ''.join(
        random.choice(chars) for _ in range(string_length)
    )

if __name__ == '__main__':
    users = []

    first_names = set([random_string(5) for _ in range(100)])
    last_names = set([random_string(5) for _ in range(100)])

    for first_name in first_names:
        for last_name in last_names:
            users.append(User2(f'{first_name} {last_name}'))

    print(f'{len(users)} users where created.')
    print(f'{len(first_names)} unique first names were stored.')
    print(f'{len(last_names)} unique last names were stored.')
    print(users[0])