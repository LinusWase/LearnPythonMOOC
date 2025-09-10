"""
Please write a function named greatest_number, which takes three arguments. The function returns the greatest in value
of the three.

An example of how the function is used:

print(greatest_number(3, 4, 1)) # 4
print(greatest_number(99, -4, 7)) # 99
print(greatest_number(0, 0, 0)) # 0
"""

def greatest_number(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c >b:
        return c
    elif a == b > c:
        return a
    elif a == c > b:
        return a
    else:
        return b


if __name__ == "__main__":
    print(greatest_number(3, 4, 1))  # 4
    print(greatest_number(99, -4, 7))  # 99
    print(greatest_number(0, 0, 0))  # 0
    print(greatest_number(1, 1, -100)) #1
    print(greatest_number(-100, 1, 1))  # 1
    print(greatest_number(1, -100, 1))  # 1
    print(greatest_number(-100, 100, -200)) # 100
