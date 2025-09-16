"""
Please write a function named sudoku_grid_correct(sudoku: list), which takes a two-dimensional array representing a
sudoku grid as its argument. The function should use the functions from the three previous exercises to determine
whether the complete sudoku grid is filled in correctly. Copy the functions from the exercises above into your Python
code file for this exercise.

The function should check each of the nine rows, columns and 3 by 3 blocks in the grid. If all contain each of the
numbers 1 to 9 at most once, the function returns True. If a single one is filled in incorrectly, the function returns
False.

The image of a sudoku grid above these exercises has the nine blocks within the grid indicated with thicker borders.
These are the blocks the function should check, and they begin at the indexes (0, 0), (0, 3), (0, 6), (3, 0), (3, 3),
(3, 6), (6, 0), (6, 3) and (6, 6).

sudoku1 = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]
]

print(sudoku_grid_correct(sudoku1))

sudoku2 = [
  [2, 6, 7, 8, 3, 9, 5, 0, 4],
  [9, 0, 3, 5, 1, 0, 6, 0, 0],
  [0, 5, 1, 6, 0, 0, 8, 3, 9],
  [5, 1, 9, 0, 4, 6, 3, 2, 8],
  [8, 0, 2, 1, 0, 5, 7, 0, 6],
  [6, 7, 4, 3, 2, 0, 0, 0, 5],
  [0, 0, 0, 4, 5, 7, 2, 6, 3],
  [3, 2, 0, 0, 8, 0, 0, 5, 7],
  [7, 4, 5, 0, 0, 3, 9, 0, 1]
]

print(sudoku_grid_correct(sudoku2))

Sample output

False
True
"""

def check_row(sudoku: list):
    for row_item in sudoku:
        checked_number = []
        for number in row_item:
            if number > 0:
                if number not in checked_number:
                    checked_number.append(number)
                else:
                    return False
    return True

def check_column(sudoku: list):
    column_no = 0
    checked_number = []
    while True:
        for column in sudoku:
            if column[column_no] > 0:
                if column[column_no] not in checked_number:
                    checked_number.append(column[column_no])
                else:
                    return False
        column_no += 1
        checked_number = []
        if column_no == 9:
            return True

def check_block(sudoku: list):
    row_no = 0
    column_no = 0
    while True:
        while True:
            checked_numbers = []
            for row in sudoku[row_no:row_no + 3]:
                for item in row[column_no:column_no + 3]:
                    if item > 0:
                        if item not in checked_numbers:
                            checked_numbers.append(item)
                        else:
                            return False
            column_no += 3
            if row_no == 6 and column_no == 9:
                return True
            elif column_no == 9:
                break
        column_no = 0
        row_no += 3


def sudoku_grid_correct(sudoku: list):
    if check_row(sudoku) and check_column(sudoku) and check_block(sudoku):
        return True
    return False

if __name__ == '__main__':
    sudoku1 = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(sudoku_grid_correct(sudoku1))

    sudoku2 = [
        [2, 6, 7, 8, 3, 9, 5, 0, 4],
        [9, 0, 3, 5, 1, 0, 6, 0, 0],
        [0, 5, 1, 6, 0, 0, 8, 3, 9],
        [5, 1, 9, 0, 4, 6, 3, 2, 8],
        [8, 0, 2, 1, 0, 5, 7, 0, 6],
        [6, 7, 4, 3, 2, 0, 0, 0, 5],
        [0, 0, 0, 4, 5, 7, 2, 6, 3],
        [3, 2, 0, 0, 8, 0, 0, 5, 7],
        [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]

    print(sudoku_grid_correct(sudoku2))