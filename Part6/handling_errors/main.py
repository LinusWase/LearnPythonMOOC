def input_validation():
    try:
        age = int(input("Please type in your age: "))
    except ValueError:
        age = -1

    if age >= 0 and age <= 150:
        print("That's a fine age")
    else:
        print("This is not a valid age")

def read_integer():
    while True:
        try:
            input_str = input("Please type in a integer: ")
            return int(input_str)
        except ValueError:
            print("This input is invalid")

#number = read_integer()
#print("Thank you!")
#print(number, "to the power of three is", number**3)


def read_small_integer():
    while True:
        try:
            input_str = input("Please type in a integer: ")
            number = int(input_str)
            if number < 100:
                return number
        except ValueError:
            pass

        print("This input is invalid")

#number = read_small_integer()
#print(number, "to the power of three is", number**3)

def testing(x):
    print(int(x) + 1)

#try:
#    number = input("Please type in a number: ")
#    testing(number)
#except:
#    print("Something went wrong")

def factorial(n):
    if n < 0:
        raise ValueError("The input was negative: " + str(n))
    k = 1
    for i in range (2, n + 1):
        k *= i
    return k

print(factorial(3))
print(factorial(6))
print(factorial(-1))

#if __name__ == '__main__':
    #input_validation()
    #read_integer()
    #read_small_integer()