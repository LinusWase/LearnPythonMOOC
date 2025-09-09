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