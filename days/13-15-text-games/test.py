import random


class Creatures:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def defensive_roll(self):
        roll = random.randint(1, 12)
        return roll * self.level

class Dragon(Creatures):
    def __init__(self, name, level, scaliness, breaths_fire):
        super().__init__(name, level)
        self.scaliness = scaliness
        self.breaths_fire = breaths_fire

    def defensive_roll(self):
        roll = super().defensive_roll()
        value = roll * self.scaliness
        if self.breaths_fire:
            value = value * 2

        return value

class Wizard(Creatures):
    def attack(self, creature):
        my_roll = self.defensive_roll()
        their_roll = creature.defensive_roll()

        return my_roll >= their_roll

creatures = [
    Creatures('Bat', 5),
    Creatures('Toad', 1),
    Creatures('Tiger', 12),
    Dragon('Black Dragon', 50, scaliness=2, breaths_fire=False)
]

active_creature = random.choice(creatures)

hero = Wizard('Spike', 10)

print(f'Active creature Name: {active_creature.name}, value: {active_creature.level}')

print(f'Active hero: {hero.name}, level: {hero.defensive_roll()}')

if hero.attack(active_creature):
    print('Win')
else:
    print('Lose')