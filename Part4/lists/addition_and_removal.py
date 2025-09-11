"""
Please write a program which asks the user to choose between addition and removal. Depending on the choice, the program
adds an item to or removes an item from the end of a list. The item that is added must always be one greater than the
last item in the list. The first item to be added must be 1.

The list is printed out in the beginning and after each operation. Have a look at the example execution below:
Sample output

The list is now []
a(d)d, (r)emove or e(x)it: d
The list is now [1]
a(d)d, (r)emove or e(x)it: d
The list is now [1, 2]
a(d)d, (r)emove or e(x)it: d
The list is now [1, 2, 3]
a(d)d, (r)emove or e(x)it: r
The list is now [1, 2]
a(d)d, (r)emove or e(x)it: d
The list is now [1, 2, 3]
a(d)d, (r)emove or e(x)it: x
Bye!
"""

my_list = []
counter = 0
while True:
    print(f"The list is now {my_list}")
    user_input = input("a(d)d, (r)emove or e(x)it: ")
    if user_input == "x":
        break
    elif user_input == "d":
        counter += 1
        my_list.insert(counter -1, counter)
    elif user_input == "r":
        my_list.remove(counter)
        counter -= 1
print("Bye!")