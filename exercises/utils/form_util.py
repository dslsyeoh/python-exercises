#  Author Steven Yeoh
#  Copyright (c) 2019. All rights reserved.

from exercises.utils import login_util, register_util


def get_form(option):
    if option == "R":
        register_form()
    elif option == "M":
        login_form()
    else:
        print("Invalid option, please try again.")


def register_form():
    print("\n=========================== REGISTER ===========================")
    username = input(" Enter username: ")
    password = input(" Enter password: ")
    confirm_password = input(" Enter confirm password: ")
    print("=========================== REGISTER ===========================")


def login_form():
    print("\n=========================== LOGIN ===========================")
    username = input(" Enter username: ")
    password = input(" Enter password: ")
    print("=========================== LOGIN ===========================")
