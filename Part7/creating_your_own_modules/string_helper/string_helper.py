from string import ascii_letters

def change_case(orig_string: str):
    new_string = ""
    for letter in orig_string:
        if letter.islower():
            new_string += letter.capitalize()
        else:
            new_string += letter.lower()
    return new_string


def split_in_half(orig_string: str):
    first_half = orig_string[:len(orig_string) // 2]
    second_half = orig_string[len(orig_string) // 2 :]

    return first_half, second_half


def remove_special_characters(orig_string: str):
    new_string = ""
    numbers = ["1","2","3","4","5","6","7","8","9","0"]

    for letter in orig_string:
        if (letter in ascii_letters) or (letter in numbers):
            new_string += letter
        elif letter == " ":
            new_string += " "

    return new_string
