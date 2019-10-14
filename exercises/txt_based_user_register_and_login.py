#  Author Steven Yeoh
#  Copyright (c) 2019. All rights reserved.

from exercises.utils.form_util import display_form

print("\n=========================== MENU ===========================")
print(" [R]egister account")
print(" [L]ogin")
user_option = input(" Enter option: ").upper()
print("=========================== MENU ===========================")
display_form(user_option)


