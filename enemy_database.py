import math

''' Enemy database '''

# { enemy_name : [enemy_possible_level (semi-random), location, kill_count] }
enemy_dict = {
    "Rat": [1, 1, "Grimwood", 0],
    "Lynx": [2, 4, "Grimwood", 0],
    "Wolf": [3, 6, "Grimwood", 0],
    "Bear": [5, 8, "Grimwood", 0],
    "Fled slave": [7, 10, "Pirate Harbour", 0],
    "Corrupt Soldier": [9, 12, "Pirate Harbour", 0],
    "Assassin": [11, 14, "Pirate Harbour", 0],
    "Captain": [13, 16, "Pirate Harbour", 0],
    "Elusive Recruit": [15, 18, "Misty Mountains", 0],
    "Harpy": [17, 20, "Misty Mountains", 0],
    "Cerberus": [19, 22, "Misty Mountains", 0],
    "Medusa": [21, 24, "Misty Mountains", 0],
    "Wild Pig": [23, 26, "Wolf Cave", 0],
    "Big Wolf": [25, 28, "Wolf Cave", 0],
    "Alphawolf": [27, 30, "Wolf Cave", 0],
    "Werewolf": [29, 32, "Wolf Cave", 0],
    "Cultist Guard": [31, 34, "Ancient Temple", 0],
    "Wererat": [33, 36, "Ancient Temple", 0],
    "Minotaur": [35, 38, "Ancient Temple", 0],
    "Minotaur Chief": [37, 40, "Ancient Temple", 0],
    "Babarian": [39, 42, "Barbarian Village", 0],
    "Babarian Warrior": [41, 44, "Barbarian Village", 0],
    "Berserker": [43, 46, "Barbarian Village", 0],
    "Babarian Chief": [45, 48, "Barbarian Village", 0],
    "Renegade Soldier": [47, 50, "Bandit Camp", 0],
    "Renegade Mercenary": [49, 52, "Bandit Camp", 0],
    "Assasinator": [51, 54, "Bandit Camp", 0],
    "Bandit Chief": [53, 56, "Bandit Camp", 0],
    "Endgame Boss": [60, 60, "Endgame Cave", 0]
}

''' Functions '''

# Giving each location its number value
location_number_dict = {}


def location_number_assign():
    location_number_counter = 0.25
    global location_number_dict

    for name, data in enemy_dict.items():
        # Math.ceil rounds up value of Endgame Cave from 7.25 to 8 (only 1
        # enemy in Endgame Cave)
        location_number_dict[data[2]] = math.ceil(location_number_counter)
        location_number_counter += 0.25

    # Reverse the dictionary to allow getting location name by number
    location_number_dict = {v: k for k, v in location_number_dict.items()}

# tests

# print(location_number_dict[1])
