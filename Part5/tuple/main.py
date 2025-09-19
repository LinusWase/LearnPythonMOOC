def tuple():
    point = (10, 20)
    print("x coordinate:", point[0])
    print("y coordinate:", point[1])

def what_is_the_purpose_of_a_tuple():
    points = {}
    points[(3,5)] = "monkey"
    points[(5, 0)] = "banana"
    points[(1, 2)] = "harpsichord"
    print((points[(3,5)]))

def minmax(my_list):
    return min(my_list), max(my_list)

my_list = [33, 5, 21, 7, 88, 312, 5]

min_value, max_value = minmax(my_list)

print(f"The smallest item is {min_value} and the greatest item is {max_value}")

if __name__ == '__main__':
    #tuple()
    what_is_the_purpose_of_a_tuple()