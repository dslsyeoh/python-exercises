#  Author Steven Yeoh
#  Copyright (c) 2019. All rights reserved.

import time
from exercises.utils.password_generator_util import generate_password, security_level_is_valid, \
    password_generation_configuration


print("\n======================= PASSWORD GENERATOR =======================")
password_length, security_level = password_generation_configuration()
if security_level_is_valid(security_level):
    print("Generating password...")
    # stimulate generate
    time.sleep(1)
    result = generate_password(password_length, security_level)
    print("Generated password: {}".format(result))
else:
    print("Password security level incorrect, Please try again.")
print("======================= PASSWORD GENERATOR =======================")

