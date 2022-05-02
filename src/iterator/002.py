
# ! Bad code
class Creature:
    def __init__(self):
        self.strength = 10
        self.intelligence = 10
        self.agility = 10

    @property
    def sum_of_stats(self):
        return self.strength + self.intelligence + self.agility

    @property
    def max_stat(self):
        return max(
            self.strength,
            self.intelligence,
            self.agility
        )

    @property
    def average_stat(self):
        return self.sum_of_stats / 3.0

# * Better code
class CreatureBetter:
    _strength = 0
    _agility = 1
    _intelligence = 2

    def __init__(self):
        self.stats = [10, 10, 10]

    @property
    def strength(self):
        return self.stats[CreatureBetter._strength]

    @strength.setter
    def strength(self, value):
        self.stats[CreatureBetter._strength] = value

    @property
    def intelligence(self):
        return self.stats[CreatureBetter._intelligence]

    @intelligence.setter
    def intelligence(self, value):
        self.stats[CreatureBetter._intelligence] = value

    @property
    def agility(self):
        return self.stats[CreatureBetter._agility]

    @agility.setter
    def agility(self, value):
        self.stats[CreatureBetter._agility] = value

    @property
    def sum_of_stats(self):
        return sum(self.stats)

    @property
    def max_stat(self):
        return max(self.stats)

    @property
    def average_stat(self):
        return self.sum_of_stats / len(self.stats)
