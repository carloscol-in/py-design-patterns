from unittest import TestCase


class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class Game:
    def __init__(self):
        # todo
        self.rat_dies = Event()
        self.rat_enters = Event()
        self.notify_rat = Event()


class Rat:
    def __init__(self, game):
        self.game = game
        self.attack = 1
        # todo
        self.game.rat_enters.append(self.rat_enters) 
        self.game.rat_dies.append(self.rat_dies)
        self.game.notify_rat.append(self.notify_rat)

        self.game.rat_enters(self)

    def __enter__(self):
        return self
        
    def __exit__(self, *args, **kwargs):
        self.game.rat_dies(self)

    def rat_enters(self, which_rat: 'Rat'):
        if self != which_rat:
            self.attack += 1
            self.game.notify_rat(which_rat)

    def rat_dies(self, _):
        self.attack -= 1

    def notify_rat(self, which_rat: 'Rat'):
        if self == which_rat:
            self.attack += 1


game = Game()

rat1 = Rat(game)
rat2 = Rat(game)

print('Rat 1', rat1.attack)
print('Rat 2', rat2.attack)

with Rat(game) as rat3:
    print(rat1.attack)
    print(rat2.attack)
    print(rat3.attack)

print(rat1.attack)
print(rat2.attack)


class Evaluate(TestCase):
    def test_single_rat(self):
        game = Game()
        rat = Rat(game)
        self.assertEqual(1, rat.attack)

    def test_two_rats(self):
        game = Game()
        rat = Rat(game)
        rat2 = Rat(game)
        self.assertEqual(2, rat.attack)
        self.assertEqual(2, rat2.attack)

    def test_three_rats_one_dies(self):
        game = Game()

        rat = Rat(game)
        self.assertEqual(1, rat.attack)

        rat2 = Rat(game)
        self.assertEqual(2, rat.attack)
        self.assertEqual(2, rat2.attack)

        with Rat(game) as rat3:
            self.assertEqual(3, rat.attack)
            self.assertEqual(3, rat2.attack)
            self.assertEqual(3, rat3.attack)

        self.assertEqual(2, rat.attack)
        self.assertEqual(2, rat2.attack)
