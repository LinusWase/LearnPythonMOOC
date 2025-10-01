import csv
from _datetime import datetime, timedelta

def cheaters():
    start_times_w_names = {}
    cheater = []
    with open("start_times.csv") as new_file:
        for line in csv.reader(new_file, delimiter=";"):
            start_times_w_names[line[0]] = line[1]
    with open("submissions.csv") as my_file:
        for line in csv.reader(my_file, delimiter=";"):
            start_time = datetime.strptime(start_times_w_names[line[0]], "%H:%M")
            end_time = datetime.strptime(line[3], "%H:%M")
            difference = end_time - start_time
            three_hours = timedelta(hours=3)
            if difference > three_hours:
                if line[0] not in cheater:
                    cheater.append(line[0])
    return cheater






if __name__ == '__main__':
    print(cheaters())