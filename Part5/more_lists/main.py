names = ["Marlyn", "Ruth", "Paul"]
print(names)
names.append("David")
print(names)

print("Number of names on the list: ", len(names))
print("Names in alphabetical order:")
names.sort()
for name in names:
    print(name)

measurements = [-2.5, 1.1, 7.5, 14.6, 21.0, 19.2]

for measure in measurements:
    print(measure)

mean = sum(measurements) / len(measurements)

print("The mean is:", mean)

my_list = [[5,2,3], [4,1], [2,2,5,1]]
print(my_list)
print(my_list[1])
print(my_list[1][0])

persons = [["Betty", 10, 1.37], ["Peter", 7, 1.25], ["Emily", 32, 1.64], ["Alan", 39, 1.75]]

for people in persons:
    name = people[0]
    age = people[1]
    height = people[2]
    print(f"{name}: age {age} years, height {height} meters")