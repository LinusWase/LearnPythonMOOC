from random import choice
import string


def generate_strong_password(length : int, numbers : bool, special_char : bool):
    password = ""
    possible_char = string.ascii_lowercase
    possible_number = string.digits
    possible_special = "!?=+-()#"
    if numbers:
        password += choice(possible_number)
        length = length - 1
    if special_char:
        password += choice(possible_special)
        length = length - 1

    for i in range(length):
        password += choice(possible_char)
    return password

if __name__ == '__main__':
    for i in range(10):
        print(generate_strong_password(8, True, True))