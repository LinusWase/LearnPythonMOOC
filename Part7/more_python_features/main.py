def single_line_conditionals(x : int):
    if x % 2 == 0:
        print("even")
    else:
        print("odd")

    #Can be written:
    print("even" if x%2 == 0 else "odd")

    y = 0
    if x%2 == 0:
        y += 1
    else:
        y = 0

    #Can be written:
    y = y + 1 if x%2 == 0 else 0

def an_empty_block():
    pass


if __name__ == '__main__':
    #single_line_conditionals(3)
    an_empty_block()