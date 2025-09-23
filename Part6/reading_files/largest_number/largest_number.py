"""
The file numbers.txt contains integer numbers, one number per line. The contents could look like this:

2
45
108
3
-10
1100
...etc...

Please write a function named largest, which reads the file and returns the largest number in the file.

Notice that the function does not take any arguments. The file you are working with is always named numbers.txt.
"""

def largest():
    my_list = []
    with open("numbers.txt") as new_file:
        for line in new_file:
            line = int(line.replace('\n', ""))
            my_list.append(line)
    return max(my_list)





if __name__ == '__main__':
    largest()