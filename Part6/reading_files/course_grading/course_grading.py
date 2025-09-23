"""
This program works with two CSV files. One of them contains information about some students on a course:

id;first;last
12345678;peter;pythons
12345687;jean;javanese
12345699;alice;adder

The other contains the number of exercises each student has completed each week:

id;e1;e2;e3;e4;e5;e6;e7
12345678;4;1;1;4;5;2;4
12345687;3;5;3;1;5;4;6
12345699;10;2;2;7;10;2;2

As you can see above, both CSV files also have a header row, which tells you what each column contains.

Please write a program which asks the user for the names of these two files, reads the files, and then prints out the total number of exercises completed by each student. If the files have the contents in the examples above, the program should print out the following:
Sample output

Student information: students1.csv
Exercises completed: exercises1.csv
pekka peloton 21
jaana javanainen 27
liisa virtanen 35

Hint: while testing your program, you may quickly run out of patience if you always have to type in the file names at
the prompt. You might want to hard-code the user input, like so:

if False:
    # this is never executed
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
else:
    # hard-coded input
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"

The actual functionality of the program is now "hidden" in the False branch of an if statement. It will never be
executed.

Now, if you want to quickly verify the program works correctly also with user input, you can just replace False with
True:


if True:
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
else:
    # now this is the False branch, and is never executed
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"

When you have verified your program works correctly, you can remove the if structure, keeping the commands asking for
input.

NB: this exercise doesn't ask you to write any functions, so you should not place any code within an
if __name__ == "__main__" block.
"""

"""
Let's expand the program created in the previous exercise. Now also the exam points awarded to each student are 
contained in a CSV file. The contents of the file follow this format:

id;e1;e2;e3
12345678;4;1;4
12345687;3;5;3
12345699;10;2;2

In the above example the student whose student number is 12345678 was awarded 4+1+4 points in the exam, which equals a 
total of 9 points.

The program should again ask the user for the names of the files. Then the program should process the files and print 
out a grade for each student.
Sample output

Student information: students1.csv
Exercises completed: exercises1.csv
Exam points: exam_points1.csv
pekka peloton 0
jaana javanainen 1
liisa virtanen 3

Each completed exercise is counted towards exercise points, so that completing at least 10 % of the total exercices 
awards 1 point, completing at least 20 % awards 2 points, etc. Completing all 40 exercises awards 10 points. The number 
of points awarded is always an integer number.

The final grade for the course is determined based on the sum of exam and exercise points according to the following 
table:
exam points + exercise points	grade
0-14	0 (fail)
15-17	1
18-20	2
21-23	3
24-27	4
28-	5

NB: this exercise doesn't ask you to write any functions, so you should not place any code within an 
if __name__ == "__main__" block.
"""

def combine(grade_list : list):
    return sum(grade_list)

def convert_to_final_grade(total_points: int):
    if total_points >= 28:
        return 5
    elif total_points >= 24:
        return 4
    elif total_points >= 21:
        return 3
    elif total_points >= 18:
        return 2
    elif total_points >= 15:
        return 1
    else:
        return 0

def read_student_info(filename: str):
    students = {}
    with open(filename) as new_file:
        for line in new_file:
            line = line.strip()
            parts = line.split(";")
            if parts[0] == "id":
                continue
            students[parts[0]] = parts[1] + " " + parts[2]
    return students

def read_exercise_data(filename: str):
    exercise_points = {}
    with open(filename) as new_file:
        for line in new_file:
            line = line.strip()
            parts = line.split(";")
            if parts[0] == "id":
                continue
            pic = parts[0]
            total_points = sum([int(p) for p in parts[1:]])
            exercise_points[pic] = total_points // 4
    return exercise_points

def read_exam_points(filename: str):
    exam_points = {}
    with open(filename) as new_file:
        for line in new_file:
            line = line.strip()
            parts = line.split(";")
            if parts[0] == "id":
                continue
            exam_points[parts[0]] = int(parts[1])
    return exam_points

def process_course_data(student_info_file: str, exercise_data_file: str, exam_points_file: str):
    students = read_student_info(student_info_file)
    exercise_points = read_exercise_data(exercise_data_file)
    exam_points = read_exam_points(exam_points_file)

    for pic, name in students.items():
        if pic in exercise_points and pic in exam_points:
            total_points = exercise_points[pic] + exam_points[pic]
            final_grade = convert_to_final_grade(total_points)
            print(f"{name} {final_grade}")
        else:
            print(f"{name} 0")

def main():
    student_info_file = input("Student information: ")
    exercise_data_file = input("Exercises completed: ")
    exam_points_file = input("Exam points: ")

    process_course_data(student_info_file, exercise_data_file, exam_points_file)

main()