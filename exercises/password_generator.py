#  Author Steven Yeoh
#  Copyright (c) 2019. All rights reserved.

import string
import time

numbers = [num for num in range(0, 10)]
lowercase_words = string.ascii_lowercase
uppercase_words = string.ascii_uppercase
punctuations = string.punctuation


def identify_level(input_level):
    if input_level == "E":
        return "Easy"
    elif input_level == "N":
        return "Normal"
    elif input_level == "H":
        return "Hard"
    pass


print("\n======================= PASSWORD GENERATOR =======================")
print("Password generation level: [E]asy, [N]ormal, [H]ard")
level = identify_level(input("Enter your password generation level: ").upper())
if level is None:
    print("Password generation level is incorrect!, Please try again.")
else:
    print("Generating password...")
    time.sleep(2)
    print("Generated password: {}".format(level))
print("======================= PASSWORD GENERATOR =======================")
