"""
Please write a function named box_of_hashes, which prints out a rectangle of hash characters. The function takes one
argument, which specifies the height of the rectangle. The rectangle should be ten characters wide.

The function should call the function line from the exercise above for the actual printing out. Copy your solution to
that exercise above the code for this exercise. Please don't change anything in your line function.

Some examples of how the function should work:

box_of_hashes(5)
print()
box_of_hashes(2)

Sample output

##########
##########
##########
##########
##########

##########
##########

"""

def line(times, text):
    if text == "":
        print("*"*times)
    else:
        print(text[0]*times)

def box_of_hashes(height):
    while height > 0:
        line(10, "#")
        height -= 1

if __name__ == "__main__":
    box_of_hashes(5)
    print()
    box_of_hashes(2)
