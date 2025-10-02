def single_line_conditionals(x : int):
    if x % 2 == 0:
        print("even")
    else:
        print("odd")

    #Can be written:
    print("even" if x%2 == 0 else "odd")

    y = 0
    if x%2 == 0:
        y += 1
    else:
        y = 0

    #Can be written:
    y = y + 1 if x%2 == 0 else 0

def an_empty_block():
    pass

def loops_with_else_blocks():
    my_list = [3,5,3,3,1]
    found = False
    for x in my_list:
        if x % 2 == 0:
            print("found an even number")
            found = True
            break
    if not found:
        print("there were no even numbers")

def default_parameter_values(name="Emily"):
    print("Hi there", name)

def a_variable_number_of_parameters(*my_args):
    print("You passed", len(my_args), "arguments")
    print("The sum of the arguments is", sum(my_args))

if __name__ == '__main__':
    #single_line_conditionals(3)
    #an_empty_block()
    #loops_with_else_blocks()
    #default_parameter_values()
    #default_parameter_values("Eric")
    #default_parameter_values("Matthew")
    #default_parameter_values("")
    a_variable_number_of_parameters(1,2,3,4,5)