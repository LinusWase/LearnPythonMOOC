def filter_incorrect():
    correct_numbers = []
    with open("lottery_numbers.csv") as file:
        for line in file:
            current_list = []
            new_line = line.split(";")
            week = new_line[0].split(" ")
            if week[1].isdigit():
                number_list = new_line[1].split(",")
                if len(number_list) == 7:
                    for number in number_list:
                        number = number.strip()
                        if not number.isdigit() or 1 < int(number) > 39:
                            break
                        if number in current_list:
                            break
                        current_list.append(number)
                        if len(current_list) == 7:
                            correct_numbers.append(line)
    with open("correct_numbers.csv", "w") as new_file:
        for line in correct_numbers:
            new_file.write(line)






if __name__ == '__main__':
    filter_incorrect()