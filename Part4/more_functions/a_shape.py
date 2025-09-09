"""
Please write a function named shape, which takes four arguments. The first two parameters specify a triangle, as above,
and the character used to draw it. The first parameter also specifies the width of a rectangle, while the third
parameter specifies its height. The fourth parameter specifies the filler character of the rectangle. The function
prints first the triangle, and then the rectangle below it.

The function should call the function line from the exercise above for the actual printing out. Copy your solution to
that exercise above the code for this exercise. Please don't change anything in the line function.

Some examples:

shape(5, "X", 3, "*")
print()
shape(2, "o", 4, "+")
print()
shape(3, ".", 0, ",")
"""

def line(times, text):
    if text == "":
        print("*"*times)
    else:
        print(text[0]*times)

def shape(width, character, height, filler):
    counter = 0
    while counter <= width:
        line(counter, character)
        counter += 1
    counter = 0
    while counter < height:
        line(width, filler)
        counter += 1

if __name__ == "__main__":
    shape(5, "X", 3, "*")
    print()
    shape(2, "o", 4, "+")
    print()
    shape(3, ".", 0, ",")