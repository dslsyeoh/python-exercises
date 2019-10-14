#  Author Steven Yeoh
#  Copyright (c) 2019. All rights reserved.

from getpass import getpass
from exercises.utils import register_util, validate_util


def display_form(user_option):
    if user_option == "R":
        register_form()
    elif user_option == "M":
        login_form()
    else:
        print("Incorrect option, please try again.")


def register_form():
    print("\n=========================== REGISTER ===========================")
    username = input(" Enter username: ")
    password = getpass(" Password: ")
    confirm_password = getpass(" Enter confirm password: ")
    print("=========================== REGISTER ===========================\n")
    errors = validate_util.validate_user_input(username, password, confirm_password)
    validate_util.print_errors(errors) if bool(errors) else register_util.add_new_user(username, password)


def login_form():
    print("\n=========================== LOGIN ===========================")
    username = input(" Enter username: ")
    password = input(" Enter password: ")
    print("=========================== LOGIN ===========================")
