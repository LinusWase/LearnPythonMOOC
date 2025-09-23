"""
This final exercise in this part is a relatively demanding problem solving task. It can be solved in many different
ways. Even though this current section in the material covers tuples, tuples are not necessarily the best way to go
about solving this.

Please write a program which prints out a square of letters as specified in the examples below. You may assume there
will be at most 26 layers.
Sample output

Layers: 3

CCCCC
CBBBC
CBABC
CBBBC
CCCCC

Sample output

Layers: 4

DDDDDDD
DCCCCCD
DCBBBCD
DCBABCD
DCBBBCD
DCCCCCD
DDDDDDD

NB: this exercise doesn't ask you to write any functions, so you should not place any code within an
if __name__ == "__main__" block.
"""

layers = int(input("Layers: "))

side_length = (layers * 2) -1

for row in range(side_length):
    row_string = ""

    for column in range(side_length):
        min_distance = min(row, side_length - 1 - row, column, side_length - 1 - column)
        char_value = chr(ord('A') + (layers-1) - min_distance)
        row_string += char_value

    print(row_string)