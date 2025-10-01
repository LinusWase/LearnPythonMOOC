import csv
from _datetime import datetime, timedelta

def cheaters(student : str):
    start_times_w_names = {}
    with open("start_times.csv") as new_file:
        for line in csv.reader(new_file, delimiter=";"):
            start_times_w_names[line[0]] = line[1]

    with open("submissions.csv") as my_file:
        for line in csv.reader(my_file, delimiter=";"):
            if line[0] == student:
                start_time = datetime.strptime(start_times_w_names[line[0]], "%H:%M")
                end_time = datetime.strptime(line[3], "%H:%M")
                difference = end_time - start_time
                three_hours = timedelta(hours=3)
                if difference > three_hours:
                    return False
    return True

def final_points():
    final_grade = {}
    with open("submissions.csv") as my_file:
        for line in csv.reader(my_file, delimiter=";"):
            not_cheater = cheaters(line[0])
            if not_cheater:
                #dosomething




if __name__ == '__main__':
    final_points()