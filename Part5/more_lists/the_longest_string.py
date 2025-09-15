"""
Please write a function named longest(strings: list), which takes a list of strings as its argument. The function finds
and returns the longest string in the list. You may assume there is always a single longest string in the list.

An example of expected behaviour:


if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))

Sample output

howdydoody
"""

def longest(strings: list):
    longest_string = ""
    for item in strings:
        if len(item) > len(longest_string):
            longest_string = item
    return longest_string


if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))
