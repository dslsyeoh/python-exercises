#  Author Steven Yeoh
#  Copyright (c) 2019. All rights reserved.

from exercises.utils.form_util import get_form

print("\n=========================== MENU ===========================")
print(" [R]egister account")
print(" [L]ogin")
user_option = input(" Enter your option: ").upper()
print("=========================== MENU ===========================")
get_form(user_option)


