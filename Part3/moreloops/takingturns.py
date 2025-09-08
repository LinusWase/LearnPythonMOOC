"""
Please write a program which asks the user to type in a number. The program then prints out the positive integers
between 1 and the number itself, alternating between the two ends of the range as in the examples below.
Sample output

Please type in a number: 5
1
5
2
4
3
Sample output

Please type in a number: 6
1
6
2
5
3
4
"""

number = int(input("Please type in a number: "))
original_number = number
counter = 1

while counter < number:
    print(counter)
    counter += 1
    print(number)
    number -= 1
if original_number % 2 != 0:
    print(number)