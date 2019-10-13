import string
import random

numbers = ''.join(map(str, [num for num in range(0, 10)]))

criteria_list = [numbers, string.ascii_lowercase, string.ascii_uppercase, string.punctuation]
security_level_dict = {"E": 2, "M": 3, "H": 4}

REPETITIVE_LIMIT = 3


def generate_password(password_length, security_level):
    generated_words = []
    old_group_index = None
    password_groups = get_password_groups(security_level)
    repetitive_count = 1
    for n in range(0, password_length):
        group_index = randomize(password_groups)
        repetitive_count = repetitive_counter_increment(old_group_index, group_index, repetitive_count)
        repetitive_count, group_index = password_algorithm(password_groups, old_group_index,
                                                           group_index, repetitive_count)
        group_items = password_groups[group_index]
        generated_words.append(group_items[randomize(group_items)])
        old_group_index = group_index
    return ''.join(map(str, generated_words))


def get_password_groups(security_level):
    return [criteria_list[index] for index in range(0, get_security_level(security_level))]


def repetitive_counter_increment(old_group_index, group_index, counter):
    if old_group_index is not None and old_group_index == group_index:
        return counter + 1
    return counter


def password_algorithm(password_groups, old_group_index, group_index, repetitive_count):
    if repetitive_count == REPETITIVE_LIMIT:
        while old_group_index is not None and old_group_index == group_index:
            group_index = randomize(password_groups)
        repetitive_count = 0
    return repetitive_count, group_index


def randomize(item):
    return random.randint(0, len(item) - 1)


def get_security_level(security_level):
    return security_level_dict.get(security_level)
