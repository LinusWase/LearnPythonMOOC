import string
from random import sample


def generate_password(length : int):
    character = string.ascii_lowercase[:]
    chars = sample(character, length)
    password = ""
    for i in chars:
        password += i
    return password


if __name__ == '__main__':
    for i in range(10):
        print(generate_password(8))
