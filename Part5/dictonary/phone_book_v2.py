"""
Please write an improved version of the phone book application. Each entry should now accommodate multiple phone
numbers. The application should work otherwise exactly as above, but this time all numbers attached to a name should be
printed.
Sample output

command (1 search, 2 add, 3 quit): 2
name: peter
number: 040-5466745
ok!
command (1 search, 2 add, 3 quit): 2
name: emily
number: 045-1212344
ok!
command (1 search, 2 add, 3 quit): 1
name: peter
040-5466745
command (1 search, 2 add, 3 quit): 1
name: mary
no number
command (1 search, 2 add, 3 quit): 2
name: peter
number: 09-22223333
ok!
command (1 search, 2 add, 3 quit): 1
name: peter
040-5466745
09-22223333
command (1 search, 2 add, 3 quit): 3
quitting...
"""
def option_one(number_dictionary : dict):
    search_name = input("name: ")
    if search_name in number_dictionary:
        for number in number_dictionary[search_name]:
            print(number)
    else:
        print("no number")

def option_two(number_dictionary : dict):
    name = input("name: ")
    number = input("number: ")
    if name not in number_dictionary:
        number_dictionary[name] = []
    number_dictionary[name].append(number)
    print("ok!")
    return number_dictionary


def main():
    number_dictionary = {}
    while True:
        user_input = int(input("command (1 search, 2 add, 3 quit): "))
        if user_input == 3:
            print("quitting...")
            break
        elif user_input == 2:
            option_two(number_dictionary)
        elif user_input == 1:
            option_one(number_dictionary)

main()