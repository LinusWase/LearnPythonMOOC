"""
This is the very last sudoku task. This time we will create a slightly different version of the function for adding new
numbers to the grid.

The function copy_and_add(sudoku: list, row_no: int, column_no: int, number: int) takes a two-dimensional array
representing a sudoku grid, two integers referring to the row and column indexes of a single square, and a single digit

The print_sudoku function from the previous exercise could be useful for testing, and it is used in the example below:

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

grid_copy = copy_and_add(sudoku, 0, 0, 2)
print("Original:")
print_sudoku(sudoku)
print()
print("Copy:")
print_sudoku(grid_copy)

Sample output

Original:
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _

_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _

_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _

Copy:
2 _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _

_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _

_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _

Hint When dealing with nested lists you should be extra careful when copying. What all needs to be explicitly copied,
and where do changes actually have an effect? The visualisation tool is a great help here, too, although the size of
the sudoku grid will make the view less orderly than usual.
"""
#TESTING:
def print_sudoku(sudoku: list):
    outside_counter = 0
    for item in sudoku:
        counter = 0
        for numbers in item:
            counter += 1
            if numbers == 0:
                print("_", end="")
                print(" ", end="")
            else:
                print(numbers, end="")
                print(" ", end="")
            if counter == 3 or counter == 6:
                print(" ", end="")
            elif counter == 9:
                print()
        outside_counter += 1
        if outside_counter % 3 == 0:
            print()

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    new_sudoku = []
    for row in sudoku:
        new_row = row[:]
        new_sudoku.append(new_row)

    new_sudoku[row_no][column_no] = number
    return new_sudoku

if __name__ == '__main__':
    sudoku = [
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

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)