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