"""
The file fruits.csv contains names of fruits, and their prices, in the format specified in this example:

banana;6.50
apple;4.95
orange;8.0
...etc...

Please write a function named read_fruits, which reads the file and returns a dictionary based on the contents. In the
dictionary, the name of the fruit should be the key, and the value should be its price. Prices should be of type float.

NB: the function does not take any arguments. The file you are working with is always named fruits.csv.
"""

def read_fruits():
    fruits = {}
    with open("fruits.csv") as new_file:
        for line in new_file:
            parts = line.split(";")
            fruits[parts[0]] = float(parts[1])
    return fruits


if __name__ == '__main__':
    print(read_fruits())