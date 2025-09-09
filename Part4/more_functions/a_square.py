"""
Please write a function named square, which prints out a square of characters, and takes two arguments. The first
parameter specifies the length of the side of the square. The second parameter specifies the character used to draw
the square.

The function should call the function line from the exercise above for the actual printing out. Copy your solution to
that exercise above the code for this exercise. Please don't change anything in the line function.

Some examples:

square(5, "*")
print()
square(3, "o")
"""

def line(times, text):
    if text == "":
        print("*"*times)
    else:
        print(text[0]*times)

def square(length, character):
    counter = 0
    while counter < length:
        line(length, character)
        counter += 1

if __name__ == "__main__":
    square(5, "*")
    print()
    square(3, "o")