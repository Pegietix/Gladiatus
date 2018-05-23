import char
import enemy_database


''' Variables '''


chosen_location = ""
valid_choose = [1, 2, 3, 4, 5, 6, 7, 8]  # We will be removing from this if location is unavailable


''' Functions '''

# Go on expedition
def expedition():
    global chosen_location, valid_choose
    print("Choose destination: ")
    print("    [1] Grimwood")

    # Number of undefeated enemies in locations
    not_killed_grimwood = 0
    not_killed_pirate_harbour = 0
    not_killed_misty_mountains = 0
    not_killed_wolf_cave = 0
    not_killed_ancient_temple = 0
    not_killed_barbarian_village = 0
    not_killed_bandit_camp = 0

    # Update above numbers
    for name, data in enemy_database.enemy_dict.items():
        if data[2] == "Grimwood" and data[3] == 0:
            not_killed_grimwood += 1
        if data[2] == "Pirate Harbour" and data[3] == 0:
            not_killed_pirate_harbour += 1
        if data[2] == "Misty Mountains" and data[3] == 0:
            not_killed_misty_mountains += 1
        if data[2] == "Wolf Cave" and data[3] == 0:
            not_killed_wolf_cave += 1
        if data[2] == "Ancient Temple" and data[3] == 0:
            not_killed_ancient_temple += 1
        if data[2] == "Barbarian Village" and data[3] == 0:
            not_killed_barbarian_village += 1
        if data[2] == "Bandit Camp" and data[3] == 0:
            not_killed_bandit_camp += 1

    # Prints available locations

    print("    [2] Pirate Harbour" + ("      [Unavailable]" if not_killed_grimwood != 0 else " "))
    print("    [3] Misty Mountains" + ("     [Unavailable]" if not_killed_pirate_harbour != 0 else " "))
    print("    [4] Wolf Cave" + ("           [Unavailable]" if not_killed_misty_mountains != 0 else " "))
    print("    [5] Ancient Temple" + ("      [Unavailable]" if not_killed_wolf_cave != 0 else " "))
    print("    [6] Barbarian Village" + ("   [Unavailable]" if not_killed_ancient_temple != 0 else " "))
    print("    [7] Bandit Camp" + ("         [Unavailable]" if not_killed_barbarian_village != 0 else " "))
    print("    [8] Endgame Cave" + ("        [Unavailable]" if not_killed_bandit_camp != 0 else " "))

    # Updating valid_choose with available locations
    if not_killed_bandit_camp != 0:
        if 8 in valid_choose:
            valid_choose.remove(8)
    if not_killed_barbarian_village != 0:
        if 7 in valid_choose:
            valid_choose.remove(7)
    if not_killed_ancient_temple != 0:
        if 6 in valid_choose:
            valid_choose.remove(6)
    if not_killed_wolf_cave != 0:
        if 5 in valid_choose:
            valid_choose.remove(5)
    if not_killed_misty_mountains != 0:
        if 4 in valid_choose:
            valid_choose.remove(4)
    if not_killed_pirate_harbour != 0:
        if 3 in valid_choose:
            valid_choose.remove(3)
    if not_killed_grimwood != 0:
        if 2 in valid_choose:
            valid_choose.remove(2)

    # Choose location
    chosen_location = input()
    try:
        if int(chosen_location) not in valid_choose:
            print("Location unavailable!")
            input()
            expedition()
        else:
            choose_enemy()
    except(ValueError):
        print("Location unavailable!")
        input()
        expedition()


# Check if location is available
def choose_enemy():
    global chosen_location, valid_choose

    # Temporary dictionary with enemies from chosen location
    enemy_temporary_dict = {}

    # Choose enemy from printed list of available ones
    print("Choose enemy: ")

    # Printing list of available enemies
    enemy_number_counter = 1
    valid_enemy_choose = [1, 2, 3, 4]
    for name, data in enemy_database.enemy_dict.items():
        if data[2] == enemy_database.location_number_dict[int(chosen_location)]:
            enemy_temporary_dict[enemy_number_counter] = name

            # Adding spaces for text formatting purposes
            name_reduction = ""
            name_length = 0
            reduction_counter = 20
            for n in name:
                name_length += 1
            while name_length < reduction_counter:
                name_reduction += " "
                reduction_counter -= 1

            print("    [{}] {}".format(int(enemy_number_counter), name) + name_reduction +
                 ("[Unavailable]" if enemy_number_counter >= 2
                and enemy_database.enemy_dict[enemy_temporary_dict[enemy_number_counter-1]][3] == 0 else " "))

            # Updates valid_enemy_choose:
            if enemy_number_counter >= 2 \
                    and enemy_database.enemy_dict[enemy_temporary_dict[enemy_number_counter - 1]][3] == 0:
                valid_enemy_choose.remove(int(enemy_number_counter))

            enemy_number_counter += 1

    chosen_enemy = input()

    # Check if enemy is available
    try:
        if int(chosen_enemy) not in valid_enemy_choose:
            print("Enemy unavailable!")
            input()
            expedition()
        else:
            pass    # go on expedition there
    except(ValueError):
        print("Enemy unavailable!")
        input()
        expedition()






# tests
'''
print(enemy_temporary_dict)
print(enemy_database.enemy_dict[enemy_temporary_dict[1]][2])

'''