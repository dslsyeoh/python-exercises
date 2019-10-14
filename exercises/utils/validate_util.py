#  Author Steven Yeoh
#  Copyright (c) 2019. All rights reserved.


def validate_user_input(username, password, confirm_password):
    error_dict = {}
    if username is "":
        error_dict["username_empty"] = "Username cannot be empty."
    elif len(username) < 5:
        error_dict["username_length"] = "Username must be at least 5 characters."
    if len(password) < 8:
        error_dict["password_length"] = "Password must be at least 8 characters."
    elif not password == confirm_password:
        error_dict["password_mismatch"] = "Password and confirm password is not match."
    return error_dict


def validate_user_login(username, password):
    # read from txt file to validate username and password
    pass


def print_errors(errors):
    for key in errors.keys():
        print(" {}".format(errors.get(key)))

