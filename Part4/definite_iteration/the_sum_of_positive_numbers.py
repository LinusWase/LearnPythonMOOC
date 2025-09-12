"""
Please write a function named sum_of_positives, which takes a list of integers as its argument. The function returns
the sum of the positive values in the list.

my_list = [1, -2, 3, -4, 5]
result = sum_of_positives(my_list)
print("The result is", result)

Sample output

The result is 9
"""

def sum_of_positives(my_list):
    sum = 0
    for numbers in my_list:
        if numbers > 0:
            sum += numbers
    return sum

if __name__ == '__main__':
    my_list = [1, -2, 3, -4, 5]
    result = sum_of_positives(my_list)
    print("The result is", result)