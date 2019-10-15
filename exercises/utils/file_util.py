#  Author Steven Yeoh
#  Copyright (c) 2019. All rights reserved.

import pathlib


def read_file():
    if not pathlib.Path("./resources").exists():
        pathlib.Path("./resources").mkdir()

    if pathlib.Path("./resources/user_acc.txt").exists():
        return open("./resources/user_acc.txt", "r")
    else:
        return None


def save_new_user_to_file(username, password):
    with open("./resources/user_acc.txt", "a+") as file:
        file.write("username={}:password={}\n".format(username, password))
