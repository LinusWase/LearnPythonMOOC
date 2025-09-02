x = 3
y = 2

print(f"/ operator {x/y}")
print(f"// operator {x//y}")

input_str = input("Which year were you born? ")
year = int(input_str)
print(f"Your age at the end of the year 2025: {2025-year}")


year = int(input("Which year were you born? "))
print(f"Your age at the end of the year 2025: {2025-year}")

height = float(input("What is your height? "))
weight = float(input("What is your weight? "))

bmi = weight / (height / 100) ** 2

print(f"The bmi is {bmi}")
