"""
In the name of Allah

Name And Family Project

authors: 

@ Amirmahdy Turani (amir1386mahdy.t@gmail.com)
@ Parsa ZahedPasha (zahedpashaparsa1387@gmail.com)
@ AmiAli Abgoun (amiraliabgon@gmail.com)

"""

from multiprocessing.sharedctypes import Value
from data import data
from random import choice

# TODO check the user_character length just is 1
user_character: str = input(">>> ")


def return_character_data(character: str) -> dict:
    """a function that give a character and return the data of that character that saved on data.py

    Args:
        character (str): charracter that user entered

    Returns:
        dict: data of character
    """
    char_data = data.get(character)  # get data of character
    # check that data isn't empty
    try:
        if char_data is None:
            raise ValueError  # raise a value error if data is empty
    except ValueError:
        print("not found any data for this character in database.")  # show error message to user
        exit()  # exit from app
    return char_data


character_data = return_character_data(user_character)


def choice_value_of_keys(dictionary: dict) -> dict:
    for key, value in dictionary.items():
        dictionary[key] = choice(value)
    return dictionary


result = choice_value_of_keys(character_data)


def show_result_to_user(result):
    # TODO show the result to user in a beauty format
    pass


# final of project

# wait for user
input("\nPress any key to continue...")

# great! wh finished it! good luck:) YA.
exit()
