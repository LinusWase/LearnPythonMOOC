"""
Please write a function named dict_of_numbers(), which returns a new dictionary. The dictionary should have the numbers
from 0 to 99 as its keys. The value attached to each key should be the number spelled out in words. Please have a look
at the example below:

numbers = dict_of_numbers()
print(numbers[2])
print(numbers[11])
print(numbers[45])
print(numbers[99])
print(numbers[0])

Sample output

two
eleven
forty-five
ninety-nine
zero

NB: Please don't formulate each spelled out number by hand. Figure out how you can use loops and dictionaries in your
solution.
"""

def dict_of_numbers():
    numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve",
               "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    new_dict = {}
    for key in range(0,20):
        if key not in new_dict:
            new_dict[key] = numbers[key]

    index = 0
    for key in range(20,100, 10):
        for number in range(0,10):
            if number == 0:
                new_dict[key] = tens[index]
            else:
                new_dict[key+number] = tens[index] + "-" + numbers[number]
        index += 1

    return new_dict

if __name__ == '__main__':
    numbers = dict_of_numbers()
    print(numbers[2])
    print(numbers[11])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])