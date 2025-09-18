"""
Please write a function named histogram, which takes a string as its argument. The function should print out a
histogram representing the number of times each letter occurs in the string. Each occurrence of a letter should be
represented by a star on the specific line for that letter.

For example, the function call histogram("abba") should print out
Sample output

a **
b **

while histogram("statistically") should print out
Sample output

s **
t ***
a **
i **
c *
l **
y *

"""

def histogram(string):
    letters = {}
    for letter in string:
        if letter not in letters:
            letters[letter] = ""
        letters[letter] += "*"

    for key in letters:
        print(key, end="")
        print("", letters[key])

if __name__ == '__main__':
    #histogram("abba")
    histogram("statistically")