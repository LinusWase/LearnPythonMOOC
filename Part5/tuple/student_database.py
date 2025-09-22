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


Part 2: adding completed courses

Please write a function named add_course, which adds a completed course to the information of a specific student in the
database. The course data is a tuple consisting of the name of the course and the grade:

students = {}
add_student(students, "Peter")
add_course(students, "Peter", ("Introduction to Programming", 3))
add_course(students, "Peter", ("Advanced Course in Programming", 2))
print_student(students, "Peter")

When some courses have been added, the information printed out changes:
Sample output

Peter:
 2 completed courses:
  Introduction to Programming 3
  Advanced Course in Programming 2
 average grade 2.5

"""
def print_student(students: dict, name):
    grade_average = 0
    if name in students:
        if not students[name]:
            print(f"{name}:")
            print(" no completed courses")
        else:
            print(f"{name}:")
            print(f" {len(students[name])} completed courses:")
            for courses in students[name]:
                print(f"  {courses[0]} {courses[1]} ")
                grade_average += courses[1]
            print(f" average grade {grade_average / len(students[name])}")
    else:
        print(f"{name}: no such person in the database")



def  add_student(students: dict, name):
    students[name] = []

def add_course(students: dict, name: str, course: tuple):
    for item in students[name]:
        if course[0] in item[0]:
            if course[1] < item[1]:
                return
            students[name].remove(item)
    if course[1] == 0:
        return
    else:
        students[name].append(course)


def summary(students: dict):
    print("students", len(students.keys()))

    print(f"most courses completed {len(students[max(students)])} {max(students)}")

    name = ""
    average_grade = 0
    grade = 0
    for student in students:
        for item in range(len(students[student])):
            grade += students[student][item][1]
        if (grade / len(students[student])) > average_grade:
            average_grade = grade / (len(students[student]))
            grade = 0
            name = student
    print(f"best average grade {average_grade} {name}")

if __name__ == '__main__':
    """
    students = {}
    add_student(students, "Peter")
    add_student(students, "Emily")
    print_student(students, "Peter")
    print_student(students, "Emily")
    print_student(students, "Andy")
    """
    """
    students = {}
    add_student(students, "Peter")
    add_course(students, "Peter", ("Introduction to Programming", 3))
    add_course(students, "Peter", ("Advanced Course in Programming", 2))
    print_student(students, "Peter")
    """
    """
    students = {}
    add_student(students, "Peter")
    add_course(students, "Peter", ("Software Development Methods", 1))
    add_course(students, "Peter", ("Software Development Methods", 5))
    print_student(students, "Peter")
    """

    """
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    summary(students)
    """
    students = {}
    add_student(students, "Emily")
    add_student(students, "Peter")
    add_course(students, "Emily", ("Software Development Methods", 4))
    add_course(students, "Emily", ("Software Development Methods", 5))
    add_course(students, "Peter", ("Data Structures and Algorithms", 3))
    add_course(students, "Peter", ("Models of Computation", 0))
    add_course(students, "Peter", ("Data Structures and Algorithms", 2))
    add_course(students, "Peter", ("Introduction to Computer Science", 1))
    add_course(students, "Peter", ("Software Engineering", 3))
    summary(students)
    summary(students)