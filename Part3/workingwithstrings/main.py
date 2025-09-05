begin = "ex"
end = "ample"
word = begin + end
print(word)
print(word*3)

n = 10
row ="*"

while n > 0:
    print(" " * n + row)
    row += "**"
    n -= 1

input_string = input("Please type in a string: ")
print(input_string[0])
print(input_string[1])
print(input_string[3])

print("First character: " + input_string[0])
print("Last character: " + input_string[len(input_string) - 1])