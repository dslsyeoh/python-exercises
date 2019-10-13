import string
import random

numbers = ''.join(map(str, [num for num in range(0, 10)]))
lowercase_words = string.ascii_lowercase
uppercase_words = string.ascii_uppercase
punctuations = string.punctuation

criteria_list = [numbers, lowercase_words, uppercase_words, punctuations]
security_level_dict = {"E": 2, "M": 3, "H": 4}


def get_password_groups(security_level):
    return [criteria_list[index] for index in range(0, get_security_level(security_level))]


def generate_password(password_length, security_level):
    generated_words = []
    password_groups = get_password_groups(security_level)
    for n in range(0, password_length):
        group_items = password_groups[randomize(password_groups)]
        generated_words.append(group_items[randomize(group_items)])
    return ''.join(map(str, generated_words))


def randomize(item):
    return random.randint(0, len(item) - 1)


def get_security_level(security_level):
    return security_level_dict.get(security_level)
