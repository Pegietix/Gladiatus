import random

''' Functions '''


# XP needed to reach next lvl
def levelup(lvl):
    return 5 * (lvl ** 2) + 5 * lvl


# Adds level if XP requirements are met
def leveling(char_instance):
    while char_instance.exp >= levelup(char_instance.lvl):
        char_instance.lvl += 1
        print("Your new level is ", char_instance.lvl)


# Adds semi-random amount of gold to the player, based on enemy_lvl
def gold_drop(char_instance, enemy_lvl):
    char_instance.add_gold(
        random.randint(int(round(enemy_lvl * (1.1 ** (enemy_lvl - 1)) * 0.7)),
                       int(round(enemy_lvl * (1.1 ** (enemy_lvl - 1)) * 1.3))))


# Adds semi-random XP amount to player, based on enemy_lvl
def exp_drop(char_instance, enemy_lvl):
    char_instance.add_exp(
        random.randint(int(enemy_lvl * 0.7), int(enemy_lvl * 1.3)))


# Player choose to go to work
def goto_work():
    hours = input("How many hours would you like to spend at work? (1-8)")
    work(hours)


# Send player to work
def work(hours):
    pass
