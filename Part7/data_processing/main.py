import csv
import json
import urllib.request

def reading_csv_files():
    with open("test.csv") as my_file:
        for line in csv.reader(my_file, delimiter=";"):
            print(line)

def reading_json_files():
    with open("courses.json") as my_file:
        data = my_file.read()

    courses = json.loads(data)
    print(courses)

    for course in courses:
        print(course["name"])

def retrieving_a_file_from_the_internet():
    my_request = urllib.request.urlopen("https://google.com")
    print(my_request.read())

def main():
    #reading_csv_files()
    #reading_json_files()
    retrieving_a_file_from_the_internet()

main()