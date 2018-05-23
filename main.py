'''  Realtime RPG game by Piotr Goldys '''

import atexit
import pickle

from expedition import *

''' Functions '''


# Saves crucial variables
def save_game():
    with open('savefile.pkl', 'wb') as f:
        pickle.dump(name_input, f)
        pickle.dump(type_input, f)
        pickle.dump(player, f)
        pickle.dump(enemy_database.enemy_dict, f)


# Asks to load the save
def loadgame_prompt():
    new_or_old = input("Would you like to load your game?   Y/N")
    if new_or_old.title() == "Y":
        pass  # load game
    else:
        # Computing fixed variables [startup]
        enemy_database.location_number_assign()


# Choosing player name
name_input = ""


def name():
    global name_input
    name_input = input("Choose your name: ").title()
    if len(name_input) < 3:
        print("Your name is too short!")
        input()
        name()


# Choosing character type
type_input = ""


def type_creation():
    print()
    print("Character types: Warrior, Shieldman, Tank, Rogue")
    print("For details, type 'd'")
    print()

    global type_input
    type_input = input("Choose your character's type: ").title()

    if type_input == "D":  # Printing details about character types
        print(char.type_details)
        input()

    elif type_input != "D" and type_input not in char.character_types:  #
        # Wrong input
        print("Wrong input!")
        input()
        type_creation()


''' Here be dragons '''

# Asks to load the save
loadgame_prompt()

# Choosing player name
name()

# Choosing character type
type_creation()

# Creates an instance of class "Character" with selected name and type
player = char.Character(name_input, type_input)

# From now the game will save variables on exit
atexit.register(save_game)

# tests
expedition()
'''
print(player.stamina)
player.get_stats()
player.add_stat('stamina')
player.get_stats()

dropexpwork.goto_work()
print(enemy_database.location_number_dict)
expedition()


print(player.type)
print(player.armor, player.strength, player.agility)

player.get_stats()


expedition(player)
print(enemy_database.location_number_dict)
'''
