def reading_data_from_a_file():
    with open("example.txt") as new_file:
        contents = new_file.read()
        print(contents)

def going_through_the_contents_of_a_file():
    with open("example.txt") as new_file:
        count = 0
        total_length = 0

        for line in new_file:
            line = line.replace('\n', "")
            count += 1
            print("Line",count, line)
            length = len(line)
            total_length += length

    print("Total length of lines:", total_length)


def reading_csv_files():
    text = "monkey,banana,harpsichord"
    words = text.split(",")
    for word in words:
        print(word)

    with open("grades.csv") as new_file:
        for line in new_file:
            line = line.replace('\n', "")
            parts = line.split(";")
            name = parts[0]
            grades = parts[1:]
            print("Name:", name)
            print("Grades:", grades)


def reading_the_same_file_multiple_times():
    people = []
    # read the contents of the file and store it in a list
    with open("people.csv") as new_file:
        for line in new_file:
            parts = line.split(";")
            people.append((parts[0], int(parts[1]), parts[2]))

    # print out the names
    for person in people:
        print("Name:", person[0])

    # find the oldest
    age_of_oldest = -1
    for person in people:
        name = person[0]
        age = person[1]
        if age > age_of_oldest:
            age_of_oldest = age
            oldest = name
    print("the oldest is", oldest)


def more_csv_file_processing():
    grades = {}
    with open("grades.csv") as new_file:
        for line in new_file:
            line = line.replace('\n', "")
            parts = line.split(";")
            name = parts[0]
            grades[name] = []
            for grade in parts[1:]:
                grades[name].append(int(grade))

    for name, grade_list in grades.items():
        best = max(grade_list)
        average = sum(grade_list) / len(grade_list)
        print(f"{name}: best grade {best}, average {average:.2f}")


def removing_unnecessary_lines_spaces_and_line_breaks():
    last_names = []
    with open("anotherpeople.csv") as new_file:
        for line in new_file:
            parts = line.split(";")
            if parts[0] == "first":
                continue
            last_names.append(parts[1].strip())
    print(last_names)

def combining_data_from_different_files():
    names = {}

    with open("employees.csv") as new_file:
        for line in new_file:
            parts = line.split(";")
            if parts[0] == "pic":
                continue
            names[parts[0]] = parts[1]

    salaries = {}

    with open("salaries.csv") as new_file:
        for line in new_file:
            parts = line.split(";")
            if parts[0] == "pic":
                continue
            salaries[parts[0]] = int(parts[1]) + int(parts[2])

    print("incomes:")

    for pic, name in names.items():
        if pic in salaries:
            salary = salaries[pic]
            print(f"{name:16} {salary} euros")
        else:
            print(f"{name:16} 0 euros")




if __name__ == '__main__':
    #reading_data_from_a_file()
    #going_through_the_contents_of_a_file()
    #reading_csv_files()
    #reading_the_same_file_multiple_times()
    #more_csv_file_processing()
    #removing_unnecessary_lines_spaces_and_line_breaks()
    combining_data_from_different_files()