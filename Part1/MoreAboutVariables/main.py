given_name = "Linus"
family_name = "Wase"
name = given_name + " " + family_name

print(name)

word = input("Please type in a word: ")
print(word)

word = word + "!!!"
print(word)

age = 22
print(age)
print("Your age is " + str(age))
print("Your age is", age)
print(f"Your age is {age}")

name = "Linus"
city = "Stockholm"
print(f"Hi {name}, you are {age} years old. You live in {city}.")




name = "Tim Tester"
age = 20
skill1 = "python"
level1 = "beginner"
skill2 = "java"
level2 = "veteran"
skill3 = "programming"
level3 = "semiprofessional"
lower = 2000
upper = 3000

print(f"my name is {name}, I am {age} years old")
print()
print("my skills are")
print(f" - {skill1} ({level1})")
print(f" - {skill2} ({level2})")
print(f" - {skill3} ({level3})")
print()
print(f"I am looking for a job with a salary of {lower}-{upper} euros per month")

#Print on a single line
print(5, end="")
print(" + ", end="")
print(8, end="")
print(" - ", end="")
print(4, end="")
print(" = ", end="")
print(5 + 8 - 4)
