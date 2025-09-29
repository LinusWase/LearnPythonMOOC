def read_input(string : str, lower : int, upper : int):
    while True:
        try:
            user_input = int(input(string))
            if user_input > lower and user_input < upper:
                return user_input
        except ValueError:
            pass
        print(f"You must type in an integer between {lower} and {upper}")


if __name__ == '__main__':
    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in:", number)

