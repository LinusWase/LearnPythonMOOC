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


if __name__ == '__main__':
    #reading_data_from_a_file()
    #going_through_the_contents_of_a_file()
    reading_csv_files()