#  Author Steven Yeoh
#  Copyright (c) 2019. All rights reserved.

from exercises.utils.password_generator_util import generate_password, password_generation_configuration


print("\n======================= PASSWORD GENERATOR =======================")
password_length, security_level, is_configuration_valid = password_generation_configuration()
if is_configuration_valid:
    print("Generated password: {}".format(generate_password(password_length, security_level)))
else:
    print("Password security level incorrect, Please try again.")
print("======================= PASSWORD GENERATOR =======================")

