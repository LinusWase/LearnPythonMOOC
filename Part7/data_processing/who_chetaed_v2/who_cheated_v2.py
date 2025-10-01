import csv
from datetime import datetime, timedelta


def cheaters(student: list):
    start_times_w_names = {}
    with open("start_times.csv") as new_file:
        for line in csv.reader(new_file, delimiter=";"):
            start_times_w_names[line[0]] = line[1]

    with open("submissions.csv") as my_file:
        for line in csv.reader(my_file, delimiter=";"):
            if line == student:
                    start_time = datetime.strptime(start_times_w_names[line[0]], "%H:%M")
                    end_time = datetime.strptime(line[3], "%H:%M")
                    difference = end_time - start_time
                    three_hours = timedelta(hours=3)
                    if difference > three_hours:
                        return False
                    else:
                        return True

def final_points():
    final_grade = {}
    with open("submissions.csv") as my_file:
        for line in csv.reader(my_file, delimiter=";"):
            if cheaters(line):
                if line[0] not in final_grade:
                    final_grade[line[0]] = {}
                if line[1] not in final_grade[line[0]]:
                    final_grade[line[0]][line[1]] = line[2]
                elif int(line[2]) > int(final_grade[line[0]][line[1]]):
                    final_grade[line[0]][line[1]] = line[2]

    return_dict = {}
    for key in final_grade.keys():
        total_points = 0
        for key2 in final_grade[key]:
            for value in final_grade[key][key2]:
                total_points += int(value)
        return_dict[key] = total_points

    return return_dict


if __name__ == '__main__':
    print(final_points())