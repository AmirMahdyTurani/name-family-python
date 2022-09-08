"""
In the name of Allah

Name And Family Project

authors: 

@ Amirmahdy Turani (amir1386mahdy.t@gmail.com)
@ Parsa ZahedPasha (zahedpashaparsa1387@gmail.com)
@ AmiAli Abgoun (amiraliabgon@gmail.com)

"""

from data import data
from random import choice

user_character = input("لطفا کاراکتر مورد نظر خود را وارد کنید: ")

if len(user_character) > 1:
    print(f"لطفا فقط یک حرف به زبان فارسی وارد کنید")
    exit()


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
        print("هیچ اطلاعاتی برای این حرف پیدا نشد.")  # show error message to user
        exit()  # exit from app
    return char_data


character_data = return_character_data(user_character)


def choice_value_of_keys(dictionary: dict) -> dict:
    for key, value in dictionary.items():
        dictionary[key] = choice(value)
    return dictionary


result = choice_value_of_keys(character_data)


def show_result_to_user(result):
    print(f" حرف:{user_character}")
    print("اسم | فامیل | شهر | کشور | رنگ | غذا | اشیاء")
    print("-------------------------------------------------")
    for word in result.values():
        print(word, end=" | ")


# final of project
show_result_to_user(result)

# wait for user
input("\n\nبرای ادامه یک دکمه را فشار دهید...")

# great! we finished it! good luck:) YA.
exit()
