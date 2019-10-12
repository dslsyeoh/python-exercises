#  Author Steven Yeoh
#  Copyright (c) 2019. All rights reserved.

import random
# 0 - rock
# 1 - paper
# 2 - scissors

win_sets = [[0, 2], [1, 0], [2, 1]]
choice_dictionary = {"r": 0, "p": 1, "s": 2}


def bot_choice():
    return random.choice(["r", "p", "s"])


def format_choice(c):
    if c is "r":
        return "Rock"
    elif c is "p":
        return "Paper"
    elif c is "s":
        return "Scissors"


def evaluate(player_selection, bot_selection):

    for win_set in win_sets:
        if (win_set[0] == player_selection or win_set[0] == bot_selection) \
                and (win_set[1] == player_selection or win_set[1] == bot_selection):
            return win_set
    pass


def get_result(p_choice, b_choice):
    player_selection = choice_dictionary[p_choice]
    bot_selection = choice_dictionary[b_choice]
    win_set = evaluate(player_selection, bot_selection)
    if win_set is None:
        return "It's Draw"
    return "Player wins" if win_set[0] == player_selection and win_set[1] == bot_selection else "Bot wins"


print("\n================= ROCK PAPER SCISSORS =================")
print(" [r]ock")
print(" [p]aper")
print(" [s]cissors")
player_choice = input(" What is your choice for this round? ")
bot_choice = bot_choice()
print("================= ROCK PAPER SCISSORS =================")
print("\n======================= RESULT ========================")
print(" Player's {} vs Bot's {} ".format(format_choice(player_choice), format_choice(bot_choice)))
print(" {}".format(get_result(player_choice, bot_choice)))
print("======================= RESULT ========================\n")

