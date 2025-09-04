number = int(input("Please type in a number: "))

if number < 0:
    print("The number is negative")
else:
    print("The number is positive or zero")

if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

correct = "kittycat"
password = input("Please type in the password: ")

if password == correct:
    print("Welcome")
else:
    print("Permission denied")

goal_home = int(input("Home goals scored: "))
goal_away = int(input("Away goals scored: "))

if goal_home > goal_away:
    print("The home team won!")
elif goal_home < goal_away:
    print("The away team won!")
else:
    print("It's a tie")
