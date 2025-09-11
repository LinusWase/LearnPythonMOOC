"""
Please write a program which asks the user for words. If the user types in a word for the second time, the program
should print out the number of different words typed in, and exit.
Sample output

Word: once
Word: upon
Word: a
Word: time
Word: upon
You typed in 4 different words
"""

my_list = []
counter = 0
while True:
    word = input("Word: ")
    my_list.append(word)
    if word in my_list:
        my_list.remove(word)
        if word in my_list:
            print(f"You typed in {counter} different words")
            break
        my_list.append(word)
    counter += 1
