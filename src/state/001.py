import abc

class State(abc.ABC):
    def on(self, switch: 'Switch'):
        print('Light is already on.')

    def off(self, switch: 'Switch'):
        print('Light is already off.')


class OffState(State):
    def __init__(self):
        print('Light is turned off.')

    def on(self, switch: 'Switch'):
        print('Turning lights on.')
        switch.state = OnState()


class OnState(State):
    def __init__(self):
        print('Light is turned on.')

    def off(self, switch: 'Switch'):
        print('Turning lights off.')
        switch.state = OffState()


class Switch:
    state: 'State'

    def __init__(self):
        self.state = OffState()

    def on(self):
        self.state.on(self)

    def off(self):
        self.state.off(self)


if __name__ == '__main__':
    switch = Switch()

    switch.on()
    switch.off()
    switch.off()
    switch.on()
    switch.on()