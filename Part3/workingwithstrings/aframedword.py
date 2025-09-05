word = input("Word: ")
width = (28 - len(word)) // 2

print("*" * 30)
if len(word) % 2 != 0:
    print("*" + " " * width + word + " " * width + " " + "*")
else:
    print("*" + " " * width + word + " " * width + "*")
print("*" * 30)

