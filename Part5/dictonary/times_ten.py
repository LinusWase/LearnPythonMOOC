"""
Please write a function named times_ten(start_index: int, end_index: int), which creates and returns a new dictionary.
The keys of the dictionary should be the numbers between start_index and end_index inclusive

The value mapped to each key should be the key times ten.

For example:

d = times_ten(3, 6)
print(d)

Sample output

{3: 30, 4: 40, 5: 50, 6: 60}
"""

def times_ten(start_index: int, end_index: int):
    my_dictionary = {}
    for index in range(start_index, end_index+1):
        my_dictionary[index] = index*10
    return my_dictionary



if __name__ == '__main__':
    d = times_ten(3, 6)
    print(d)