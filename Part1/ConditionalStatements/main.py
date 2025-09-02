age = int(input("How old are you? "))

if age > 17:
    print("You are of age!")
    print("Here's a copy of GTA6 for you.")

print("Next customer, please!")

number = int(input("Please type in a number: "))

if number < 0:
    print("The number is negative")

if number > 0:
    print("The number is positive")

if number == 0:
    print("The number is zero.")

a = 3
condition = a < 5
print(condition)
if condition:
    print("a is less than 5")

condition = True
if condition:
    print("This is printed every time.")

    # Fix the program
    points = int(input("How many points are on your card? "))

    if points >= 100:
        points *= 1.15
        print("Your bonus is 15 %")

    if points < 100:
        points *= 1.1
        print("Your bonus is 10 %")


    print("You now have", points, "points")