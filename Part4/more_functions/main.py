from logging import makeLogRecord


def message():
    print("This message was brought to you by a function")

message()

def greet(name):
    print("Hello there,", name)

def sum(a,b):
    print("The sum of the arguments is", a+b)

greet("Linus")
sum(3,6)

def greet_many_times(name, times):
    while times > 0:
        greet(name)
        times -= 1

greet_many_times("Linus", 3)


def my_sum(a,b):
    return a + b

result = my_sum(6,3)

print("Sum:", result)

def ask_for_name():
    name = input("What's your name? ")
    return name

name = ask_for_name()
print("Hello there,", name)

def smallest(x,y):
    if x < y:
        return  x
    return y

print(smallest(10,3))
print(smallest(2,3))

def greet(name1):
    if name1 == "":
        print("???")
        return
    print("Hello there,", name1)

greet("Emily")
greet("")
greet("Mark")

def my_sum(a, b):
    return a+b

def difference(a, b):
    return a-b

result = difference(my_sum(5, 2), my_sum(2, 3))
print("The result is", result)

def print_many_times (message : str, times : int):
    while times > 0:
        print(message)
        times -= 1

def ask_for_name() -> str:
    name = input("What's your name? ")
    return name

number = [1,2,3,4,5,6]
number.insert(0,10)
print(number)
number.insert(2,20)
print(number)

my_list = [1,2,3,4,5,6]

my_list.pop(2)
print(my_list)
my_list.pop(3)
print(my_list)

number = my_list.pop(1)
print(number)
print(my_list)

my_list.remove(4)
print(my_list)
my_list.remove(6)

my_list = [1, 2, 1, 2]

my_list.remove(1)
print(my_list)
my_list.remove(1)
print(my_list)