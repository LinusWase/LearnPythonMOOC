"""
Please write a function named even_numbers, which takes a list of integers as an argument. The function returns a new
list containing the even numbers from the original list.

my_list = [1, 2, 3, 4, 5]
new_list = even_numbers(my_list)
print("original", my_list)
print("new", new_list)

Sample output

original [1, 2, 3, 4, 5]
new [2, 4]
"""

def even_numbers(my_list : list):
    new_list = []
    for number in my_list:
        if number % 2 == 0:
            new_list.append(number)
    return new_list

if __name__ == '__main__':
    my_list = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
    new_list = even_numbers(my_list)
    print("original", my_list)
    print("new", new_list)

