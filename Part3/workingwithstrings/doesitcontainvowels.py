"""
Please write a program which asks the user to input a string. The program then prints out different messages if the
string contains any of the vowels a, e or o.

You may assume the input will be in lowercase entirely. Have a look at the examples below.
"""

input_string = input("Please type in a string: ")

if "a" in input_string:
    print("a found")
else:
    print("a not found")

if "e" in input_string:
    print("e found")
else:
    print("e not found")

if "o" in input_string:
    print("o found")
else:
    print("o not found")