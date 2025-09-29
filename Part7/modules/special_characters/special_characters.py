import string

def separate_characters(my_string: str):
    ascii_letters = ""
    punctuations = ""
    remaining = ""
    for letters in my_string:
        if letters in string.ascii_letters:
            ascii_letters += letters
        elif letters in string.punctuation:
            punctuations += letters
        else:
            remaining += letters
    return ascii_letters, punctuations, remaining

if __name__ == '__main__':
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])
    print(parts[1])
    print(parts[2])