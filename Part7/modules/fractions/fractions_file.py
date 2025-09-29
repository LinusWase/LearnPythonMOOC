from fractions import Fraction

def fractionate(amount: int):
    my_list = [Fraction(1, amount)]
    return my_list * amount


if __name__ == '__main__':
    for p in fractionate(3):
        print(p)

    print()

    print(fractionate(5))