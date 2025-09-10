"""
Please write three functions: first_word, second_word and last_word. Each function takes a string argument.

As their names imply, the functions return either the first, the second or the last word in the sentence they receive
as their string argument.

In each case you may assume the argument string contains at least two separate words, and all words are separated by
exactly one space character. There will be no spaces in the beginning or at the end of the argument strings.

sentence = "it was a dark and stormy python"

print(first_word(sentence)) # it
print(second_word(sentence)) # was
print(last_word(sentence)) # python

Sample output

it
was
python
"""

def first_word(sentence):
    index = sentence.find(" ")
    return sentence[:index]

def second_word(sentence):
    sentence = sentence[sentence.find(" ") + 1:]
    return sentence[:sentence.find(" ")]


def last_word(word):
    print()

if __name__ == "__main__":
    sentence = "it was a dark and stormy python"

    print(first_word(sentence))  # it
    print(second_word(sentence))  # was
    print(last_word(sentence))  # python