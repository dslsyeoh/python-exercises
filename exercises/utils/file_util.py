#  Author Steven Yeoh
#  Copyright (c) 2019. All rights reserved.

import os.path


def read_file():
    if not os.path.exists("./resources"):
        os.mkdir("./resources")

    if os.path.exists("./resources/user_acc.txt"):
        return open("./resources/user_acc.txt", "r")
    else:
        return None


def save_new_user_to_file(username, password):
    file = open("./resources/user_acc.txt", "a+")
    file.write("username={}:password={}\n".format(username, password))
