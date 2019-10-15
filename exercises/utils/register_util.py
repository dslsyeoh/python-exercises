#  Author Steven Yeoh
#  Copyright (c) 2019. All rights reserved.


from exercises.utils.file_util import save_new_user_to_file
from exercises.utils.validate_util import user_exists


def add_new_user(username, password):
    if user_exists(username):
        print(" Sorry, username has been taken.")
    else:
        save_new_user_to_file(username, password)
        print(" Successfully created user, {}.".format(username))

