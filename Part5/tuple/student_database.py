"""
In this series of exercises you will create a simple student database. Before diving in, please spend a moment reading
through the instructions and thinking about what sort of data structures are necessary for organising the data stored
by your program.

Part 1: adding students

First write a function named add_student, which adds a new student to the database. Also write a preliminary version of
the function print_student, which prints out the information of a single student.

These function are used as follows:
students = {}
add_student(students, "Peter")
add_student(students, "Eliza")
print_student(students, "Peter")
print_student(students, "Eliza")
print_student(students, "Jack")

Your program should now print out
Sample output

Peter:
 no completed courses
Eliza:
 no completed courses
Jack: no such person in the database
"""
def print_student(students: dict, name):
    if name in students:
        if students[name] == "":
            print(f"{name}:")
            print(" no completed courses")
    else:
        print(f"{name}: no such person in the database")



def  add_student(students: dict, name):
    students[name] = ""

if __name__ == '__main__':
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    print_student(students, "Peter")
    print_student(students, "Eliza")
    print_student(students, "Jack")