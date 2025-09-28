def add_to_file(filename : str, correct : list):
    with open(filename, "w") as file:
        for line in correct:
            file.write(line + '\n')

def filter_solutions():
    correct = []
    incorrect = []
    with open("solutions.csv") as file:
        for line in file:
            stripped_line = line.strip()
            splitted_line = stripped_line.split(";")
            if "+" in splitted_line[1]:
                new_line = splitted_line[1].split("+")
                if int(new_line[0]) + int(new_line[1]) == int(splitted_line[2]):
                    correct.append(line.strip())
                    continue
            elif "-" in splitted_line[1]:
                new_line = splitted_line[1].split("-")
                if int(new_line[0]) - int(new_line[1]) == int(splitted_line[2]):
                    correct.append(line.strip())
                    continue
            incorrect.append(line.strip())


    add_to_file("correct.csv",correct)
    add_to_file("incorrect.csv", incorrect)


if __name__ == '__main__':
    filter_solutions()