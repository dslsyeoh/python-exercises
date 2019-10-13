#  Author Steven Yeoh
#  Copyright (c) 2019. All rights reserved.

import time
from exercises.utils.password_generator_util import generate_password, security_level_is_valid


print("\n======================= PASSWORD GENERATOR =======================")
password_length = 0
try:
    password_length = int(input("Enter your password length: "))
except ValueError:
    password_length = 15
finally:
    print("Password security level: [E]asy, [M]edium, [H]ard")
    security_level = input("Enter your password security level: ").upper()
    if security_level_is_valid(security_level):
        print("Generating password...")
        # stimulate generate
        time.sleep(1)
        result = generate_password(password_length, security_level)
        print("Generated password: {}".format(result))
    else:
        print("Password security level incorrect, Please try again.")
print("======================= PASSWORD GENERATOR =======================")

