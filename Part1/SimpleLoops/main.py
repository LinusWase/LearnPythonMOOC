while True:
    number = int(input("Please type in a number, -1 to quit: "))

    if number == -1:
        break

    print(number ** 2)

print("Thanks and bye!")

while True:
    code = input("Please type in your PIN: ")
    if code == "1234":
        break
    print("Incorrect...try again")

print("Correct PIN entered!")