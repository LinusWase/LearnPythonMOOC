"""
Please write a program which asks the user to type in some text. Your program should then perform a spell check, and
print out feedback to the user, so that all misspelled words have stars around them. Please see the two examples below:
Sample output

Write text: We use ptython to make a spell checker

We use *ptython* to make a spell checker

Sample output

Write text: This is acually a good and usefull program

This is *acually* good and *usefull* program

The case of the letters should be irrelevant to the functioning of your program.

The exercise template includes the file wordlist.txt, which contains all the words the spell checker should accept as
correct.

NB: this exercise doesn't ask you to write any functions, so you should not place any code within an
if __name__ == "__main__" block.
"""

def main():
    user_input = input("Write text: ")
    words = user_input.split()
    correct_word = []

    with open("wordlist.txt") as file:
        wordlist = {word.strip() for word in file}
        for word in words:
            if word.lower() not in wordlist:
                correct_word.append(f"*{word}*")
            else:
                correct_word.append(word)

    for word in correct_word:
        print(word, end=" ")


main()