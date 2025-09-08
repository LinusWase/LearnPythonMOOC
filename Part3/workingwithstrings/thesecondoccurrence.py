input_string = input("Please type in a string: ")
substring = input("Please type in a substring: ")

counter = 0
sum = 0

while counter < 2:
    if substring in input_string:
        index = input_string.find(substring)
        sum += index
        input_string = input_string[index+len(substring):]
        if counter == 1:
            print(f"The second occurrence of the substring is at index {sum + len(substring)}.")
        counter += 1
    else:
        print("The substring does not occur twice in the string.")
        break