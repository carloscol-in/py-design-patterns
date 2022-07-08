class CombinationLock:
    def __init__(self, combination):
        self.status = 'LOCKED'
        # todo
        self.entry = ''
        self._combination = ''.join((str(c) for c in combination))
        
    def reset(self):
        # todo - reset lock to LOCKED state
        self.status = 'LOCKED'

    def enter_digit(self, digit):
        # todo
        self.entry += str(digit)
        
        if self.entry == self._combination:
            self.status = 'OPEN'
            return
        
        self.status = self.entry


if __name__ == '__main__':
    cl = CombinationLock([1,2,3,4,5])

    cl.enter_digit(1)
    print(cl.status)
    cl.enter_digit(2)
    print(cl.status)
    cl.enter_digit(3)
    print(cl.status)
    cl.enter_digit(4)
    print(cl.status)
    cl.enter_digit(5)
    print(cl.status)