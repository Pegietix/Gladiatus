import pickle

import enemy_database

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
