from dropexpwork import *

''' Variables '''

# Type details for print
type_details = "Stat base:  10\n" \
               "Warrior:    Strength +4    Dexterity +1    Armor +1\n" \
               "Shieldman:  Armor +5       Agility +1\n" \
               "Tank:       Stamina +5     Armor +1\n" \
               "Rogue:      Dexterity +2   Agility +2      Charisma +2"

# Valid character types
character_types = ["Warrior", "Shieldman", "Tank", "Rogue"]

''' Functions '''


# Creating player class
class Character:
    """
        Stats:
            stamina - HP
            strength - attack power
            armor - enemy damage reduction
            dexterity - hit chance
            agility - dodge chance
            charisma - double hit chance


    """

    # Creates character with default statistics
    def __init__(self, name, chartype, exp=1, lvl=1, stamina=10, strength=10,
                 armor=10, dexterity=10, agility=10,
                 charisma=10, gold=10, weapon=None, armor_item=None):
        self.name = name
        self.type = chartype
        self.exp = exp
        self.lvl = lvl
        self.stamina = stamina
        self.strength = strength
        self.armor = armor
        self.dexterity = dexterity
        self.agility = agility
        self.charisma = charisma
        self.gold = gold
        self.weapon = weapon
        self.armor_item = armor_item

        # Current costs of statistic upgrades
        self.stamina_cost = self.cost_of_statistic(stamina)
        self.strength_cost = int(round(2 * 1.2 ** (self.strength - 10)))
        self.armor_cost = int(round(2 * 1.2 ** (self.armor - 10)))
        self.dexterity_cost = int(round(2 * 1.2 ** (self.dexterity - 10)))
        self.agility_cost = int(round(2 * 1.2 ** (self.agility - 10)))
        self.charisma_cost = int(round(2 * 1.2 ** (self.charisma - 10)))

        # Limit of armor statistic
        self.armor_limit = int(
            round((12 + 1 * (self.lvl - 1)) * 1.02 ** (self.lvl - 1)))

        # Alters starting statistics according to chartype selection
        if self.type == "Warrior":
            self.strength = self.strength + 4
            self.dexterity += 1
            self.armor += 1

        elif self.type == "Shieldman":
            self.armor += 5
            self.agility += 1

        elif self.type == "Tank":
            self.stamina += 5
            self.armor += 1

        elif self.type == "Rogue":
            self.dexterity += 2
            self.agility += 2
            self.charisma += 2

    # Prints character statistics
    def get_stats(self):
        print("Lvl: ", str(self.lvl) + "   ", end=" ")
        print("XP: ", str(self.exp) + "/" + str(levelup(self.lvl)) + "   ",
              end=" ")
        print("Stamina: ", str(self.stamina) + "   ", end=" ")
        print("Strength: ", str(self.strength) + "   ", end=" ")
        print("Armor: ", str(self.armor) + "   ", end=" ")
        print("Dexterity: ", str(self.dexterity) + "   ", end=" ")
        print("Agility: ", str(self.agility) + "   ", end=" ")
        print("Charisma: ", str(self.charisma))

    # Adds XP
    def add_exp(self, amount):
        self.exp += amount
        print("XP: +{}".format(amount))

    # Adds gold
    def add_gold(self, amount):
        if self.gold + amount < 0:  # When gold penalty > current gold,
            # make penalty = current gold
            amount += (abs(amount) - self.gold)

        print("Gold: " + ("+" if amount > 0 else "") + str(amount))
        self.gold += amount

    # Returns cost of chosen statistic
    def cost_of_statistic(self, attribute):
        return int(round(2 * 1.2 ** (attribute - 10)))

    # Adds 1 point to chosen statistic
    def add_stat(self, stat):
        setattr(self, stat, getattr(self, stat) + 1)


# tests
test = 1
