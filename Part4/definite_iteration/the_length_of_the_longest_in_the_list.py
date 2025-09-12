"""
Please write a function named length_of_longest, which takes a list of strings as its argument. The function returns
the length of the longest string.

my_list = ["first", "second", "fourth", "eleventh"]

result = length_of_longest(my_list)
print(result)

my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

result = length_of_longest(my_list)
print(result)

Sample output

8
7
"""

def length_of_longest(my_list : list):
    longest_word = 0
    for word in my_list:
        if len(word) > longest_word:
            longest_word = len(word)
    return longest_word

if __name__ == '__main__':
    my_list = ["first", "second", "fourth", "eleventh"]

    result = length_of_longest(my_list)
    print(result)

    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = length_of_longest(my_list)
    print(result)