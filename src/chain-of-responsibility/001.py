class Creature:
    def __init__(self, name, attack, defense):
        self.name = name
        self.attack = attack
        self.defense = defense
    
    def __str__(self):
        return f'{self.name} ({self.attack}/{self.defense})'

class CreatureModifier:
    def __init__(self, creature):
        self.creature = creature
        self.next_modifier = None

    def add_modifier(self, modifier):
        if self.next_modifier:
            self.next_modifier.add_modifier(modifier)
        else:
            self.next_modifier = modifier

    def handle(self):
        if self.next_modifier:
            self.next_modifier.handle()
            self.next_modifier = None

class DoubleAttackModifier(CreatureModifier):
    def handle(self):
        print(f'We\'re doubling {self.creature.name}\'s attack points.')
        self.creature.attack *= 2
        super().handle()

class IncreaseDefenseModifier(CreatureModifier):
    def __init__(self, creature, points_to_increase):
        self.points_to_increase = points_to_increase
        super().__init__(creature)

    def handle(self):
        print(f'Increasing {self.creature.name}\' defense points by {self.points_to_increase}')
        self.creature.defense += self.points_to_increase
        super().handle()

if __name__ == '__main__':
    goblin = Creature('Goblin', 1, 1)
    print(goblin)

    root = CreatureModifier(goblin)

    # this modifier is added to root's `next_modifier`.
    root.add_modifier(DoubleAttackModifier(goblin))

    # this modifier is added to last DoubleAttackModifier(goblin) modifier object.
    root.add_modifier(DoubleAttackModifier(goblin))
    
    # `handle()` is called throughout the chain of modifiers
    root.handle()

    print(goblin)

    root.add_modifier(IncreaseDefenseModifier(goblin, 2))

    root.handle()

    print(goblin)