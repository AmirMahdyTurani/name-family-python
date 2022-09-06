"""
In the name of Allah

Name And Family Project

authors: 

@ Amirmahdy Turani (amir1386mahdy.t@gmail.com)
@ Parsa ZahedPasha (zahedpashaparsa1387@gmail.com)
@ AmiAli Abgoun (add your email)

"""

from multiprocessing.sharedctypes import Value
from data import data
from random import choice

user_character = input(">>> ")


def return_character_data(character):
    # TODO return a dictionary that contain data of character
    pass


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
