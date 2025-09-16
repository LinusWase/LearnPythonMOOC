"""
In this exercise we will complete two more functions for the sudoku project from the previous section: print_sudoku and
add_number.

The function print_sudoku(sudoku: list) takes a two-dimensional array representing a sudoku grid as its argument. The
function should print out the grid in the format specified in the examples below.

The function add_number(sudoku: list, row_no: int, column_no: int, number:int) takes a two-dimensional array
representing a sudoku grid, two integers referring to the row and column indexes of a single square, and a single digit
between 1 and 9, as its arguments. The function should add the digit to the specified location in the grid.

sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

print_sudoku(sudoku)
add_number(sudoku, 0, 0, 2)
add_number(sudoku, 1, 2, 7)
add_number(sudoku, 5, 7, 3)
print()
print("Three numbers added:")
print()
print_sudoku(sudoku)

Sample output

_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _

_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _

_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _

Three numbers added:

2 _ _  _ _ _  _ _ _
_ _ 7  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _

_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ 3 _

_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _

Hint

Remember it is possible to call the print function without causing a line change:

print("characters ", end="")
print("without carriage returns", end="")

Sample output

characters without carriage returns

Sometimes you need just a new line, which a print statement without any argument will achieve:

print()
"""

def print_sudoku(sudoku: list):
    outside_counter = 0
    for item in sudoku:
        counter = 0
        for numbers in item:
            counter += 1
            if numbers == 0:
                print("_", end="")
            else:
                print(numbers, end="")
            if counter == 3 or counter == 6:
                print(" ", end="")
            elif counter == 9:
                print()
        outside_counter += 1
        if outside_counter % 3 == 0:
            print()





def add_number(sudoku: list, row_no: int, column_no: int, number:int):
    counter = 0
    for row in sudoku[row_no]:
        if counter == column_no:
            row = number
            print(row)
        counter += 1


if __name__ == '__main__':
    sudoku = [
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    print_sudoku(sudoku)
    add_number(sudoku, 0, 0, 2)
    #add_number(sudoku, 1, 2, 7)
    #add_number(sudoku, 5, 7, 3)
    print()
    print("Three numbers added:")
    print()
    print_sudoku(sudoku)