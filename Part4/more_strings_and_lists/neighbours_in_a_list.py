"""
Given a list of integers, let's decide that two consecutive items in the list are neighbours if their difference is 1.
So, items 1 and 2 would be neighbours, and so would items 56 and 55.

Please write a function named longest_series_of_neighbours, which looks for the longest series of neighbours within the
list, and returns its length.

For example, in the list [1, 2, 5, 4, 3, 4] the longest list of neighbours would be [5, 4, 3, 4], with a length of 4.

An example function call:

my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
print(longest_series_of_neighbours(my_list))

Sample output

4
"""

def longest_series_of_neighbours(list : list):
    longest = 1
    if len(list) == 1:
        return longest
    temp_longest = 1
    previous_number = list[0]
    list.pop(0)
    for item in list:
        if previous_number == item +1 or previous_number == item -1:
            temp_longest +=1
        elif temp_longest >= longest:
            temp_longest = 1
        previous_number = item
        if temp_longest > longest:
            longest = temp_longest
    return longest


if __name__ == '__main__':
    my_list = [1, 3, 5, 7, 10, 11, 14, 15, 19, 20, 21, 22, 23, 24, 25]
    print(longest_series_of_neighbours(my_list))