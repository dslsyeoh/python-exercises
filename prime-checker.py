
#  Author Steven Yeoh
#  Copyright (c) 2019. All rights reserved.

number_list = [num for num in range(1, 100)]


def prime_checker(numbers):

    prime_numbers = []

    for number in numbers:
        if number > 1:
            count = 0
            for num in range(2, number + 1):
                if count > 1:
                    break
                elif number / num % 1 == 0:
                    count += 1
            if count == 1:
                prime_numbers.append(number)
    return prime_numbers


result = prime_checker(number_list)
print("prime numbers of [1-100] = {} ".format(result))
