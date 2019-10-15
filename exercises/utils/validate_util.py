#  Author Steven Yeoh
#  Copyright (c) 2019. All rights reserved.


from exercises.utils.file_util import read_file


def validate_user_input(username, password, confirm_password):
    error_dict = {}
    if not bool(username):
        error_dict["username_empty"] = "Username cannot be empty."
    elif len(username) < 5:
        error_dict["username_length"] = "Username must be at least 5 characters."
    if len(password) < 8:
        error_dict["password_length"] = "Password must be at least 8 characters."
    elif not password == confirm_password:
        error_dict["password_mismatch"] = "Password and confirm password is not match."
    return error_dict


def validate_user_credentials(username, password):
    file = read_file()
    for data in file:
        if data.split(":")[0].split("=")[1] == username and data.split(":")[1].split("=")[1].rstrip("\n") == password:
            return True
    return False


def print_errors(errors):
    for key in errors.keys():
        print(" {}".format(errors.get(key)))


def user_exists(username):
    with read_file() as file:
        if file is not None:
            for data in file:
                if data.split(":")[0].split("=")[1] == username:
                    return True
            return False
    return False
