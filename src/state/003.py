from enum import Enum, auto


class State(Enum):
    LOCKED = auto()
    FAILED = auto()
    UNLOCKED = auto()


if __name__ == '__main__':
    code = '1234'
    state = State.LOCKED
    entry = ''

    while True:
        if state == State.LOCKED:
            entry = input('Input the lock\'s code: ')

            if entry != code:
                state = State.FAILED
                continue

            state = State.UNLOCKED

        elif state == State.FAILED:
            print('\nFailed.\n')
            entry = ''
            state = State.LOCKED

        elif state == State.UNLOCKED:
            print('\nUnlocked!\n')
            break