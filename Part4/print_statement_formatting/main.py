number = 1/3
print(f"The number is {number:.2f}")

names =  [ "Steve", "Jean", "Katherine", "Paul" ]
for name in names:
    print(f"{name:15} centre {name:>15}")

name = "Linus"
age = 22
city = "Stockholm"
greeting = f"Hi {name}, you are {age} years of age"
print(greeting + f", and you live in {city}")