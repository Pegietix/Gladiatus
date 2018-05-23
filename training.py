''' Functions '''


# Player decided to train statistics
def training(char_instance):
    # Print stats and training costs
    char_instance.get_stats()
    print()
    training_costs(char_instance)


# Printing costs of training and letting player choose statistic to upgrade
def training_costs(char_instance):
    print("Choose statistic to upgrade")
    print("    [1] Stamina:   ", char_instance.stamina_cost, "gold")
    print("    [2] Strength:  ", char_instance.strength_cost, "gold")
    print("    [3] Armor:     ", char_instance.armor_cost, "gold")
    print("    [4] Dexterity: ", char_instance.dexterity_cost, "gold")
    print("    [5] Agility:   ", char_instance.agility_cost, "gold")
    print("    [6] Charisma:  ", char_instance.charisma_cost, "gold")
    training_stat(char_instance)


# Upgrading chosen statistic if requirements are met (mainly gold)
def training_stat(char_instance):
    choose_dict = {"1": "stamina", "2": "strength", "3": "armor",
                   "4": "dexterity", "5": "agility", "6": "charisma"}
    chosen_stat = input()
    training_success = 0
    if chosen_stat == "1" and char_instance.gold >= char_instance.stamina_cost:
        char_instance.add_stat("stamina")
        training_success += 1

    elif chosen_stat == "2" and char_instance.gold >= \
            char_instance.strength_cost:
        char_instance.add_stat("strength")
        training_success += 1

    elif chosen_stat == "3" and char_instance.gold >= \
            char_instance.armor_cost and \
            char_instance.armor_limit > char_instance.armor:
        char_instance.add_stat("armor")
        training_success += 1

    elif chosen_stat == "4" and char_instance.gold >= \
            char_instance.dexterity_cost:
        char_instance.add_stat("dexterity")
        training_success += 1

    elif chosen_stat == "5" and char_instance.gold >= \
            char_instance.agility_cost:
        char_instance.add_stat("agility")
        training_success += 1

    elif chosen_stat == "6" and char_instance.gold >= \
            char_instance.charisma_cost:
        char_instance.add_stat("charisma")
        training_success += 1

    elif chosen_stat == "h":
        training_success += 1
        pass  # Open help .doc

    elif chosen_stat not in ["1", "2", "3", "4", "5", "6", "h"]:
        print("Wrong input!")

    else:
        if chosen_stat == "3" and char_instance.armor_limit <= \
                char_instance.armor:
            print("You reached your armor limit!")
        else:
            print("Not enough gold!")

    if not training_success == 0:
        print("{}: +1".format(choose_dict.get(chosen_stat).title()))
