a = [1,2,3]
print(id(a))
b = "This is a reference, too"
print(id(b))

number = 1
print(id(number))
number += 10
print(id(number))
number = 2
print(id(number))

a = [1,2,3]
b = a
b[0] = 10

print(id(a))
print(id(b))
print(a)

my_list = [1, 2, 3, 3, 5]

new_list = []
for item in my_list:
    new_list.append(item)

new_list[0] = 10
new_list.append(6)
print("the original:", my_list)
print("the copy:", new_list)

my_list = [1,2,3,4,5]
new_list = my_list[:] #Easy way to copy
my_list[0] = 10
new_list[1] = 32

print(my_list)
print(new_list)


def add_item(my_list: list):
    new_item = 10
    my_list.append(new_item)

a_list = [1,2,3]
print(a_list)
add_item(a_list)
print(a_list)