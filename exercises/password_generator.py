#  Author Steven Yeoh
#  Copyright (c) 2019. All rights reserved.

import time
from exercises.utils.password_generator_util import generate_password


print("\n======================= PASSWORD GENERATOR =======================")
password_length = int(input("Enter your password length: "))
print("Password security level: [E]asy, [M]edium, [H]ard")
security_level = input("Enter your password security level: ").upper()
if security_level is None:
    print("Password security level incorrect!, Please try again.")
else:
    print("Generating password...")
    result = generate_password(password_length, security_level)
    time.sleep(2)
    print("Generated password: {}".format(result))
print("======================= PASSWORD GENERATOR =======================")

