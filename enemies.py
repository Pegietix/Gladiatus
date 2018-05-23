import random

import numpy

import enemy_database

''' Functions '''


# Create an enemy class
class Enemy:
    def __init__(self, name):
        self.name = name
        self.lvl = random.randint(
            (enemy_database.enemy_dict.get(self.name))[0],
            (enemy_database.enemy_dict.get(self.name))[1])

        # Generates semi-random enemy statistics - 10% more for each lvl.
        # numpy.random.normal(EV, st_dev, no. of numbers)
        self.stamina = int(
            numpy.random.normal((12 * 1.1 ** (self.lvl - 1)), 2, 1))
        self.strength = int(
            numpy.random.normal((10 * 1.1 ** (self.lvl - 1)), 2, 1))
        self.armor = int(
            numpy.random.normal((5 * 1.1 ** (self.lvl - 1)), 2, 1))
        self.dexterity = int(
            numpy.random.normal((10 * 1.1 ** (self.lvl - 1)), 2, 1))
        self.agility = int(
            numpy.random.normal((10 * 1.1 ** (self.lvl - 1)), 2, 1))
        self.charisma = int(
            numpy.random.normal((10 * 1.1 ** (self.lvl - 1)), 2, 1))
