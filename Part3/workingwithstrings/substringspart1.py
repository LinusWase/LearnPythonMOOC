"""
Please write a program which asks the user to type in a string. The program then prints out all the substrings which
begin with the first character, from the shortest to the longest. Have a look at the example below.
Sample output

Please type in a string: test
t
te
tes
test
"""

input_string = input("Please type in a string: ")
index = 1

while index <= len(input_string):
    print(input_string[0:index])
    index += 1