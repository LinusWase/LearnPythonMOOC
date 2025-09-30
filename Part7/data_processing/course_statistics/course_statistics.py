import urllib.request
import json


def retrieve_all():
    my_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    request = my_request.read()
    courses = json.loads(request)
    active_course = []
    for index in range(len(courses)):
        if courses[index]["enabled"]:
            exercise_total = sum(courses[index]["exercises"])
            full_info = (courses[index]["fullName"], courses[index]["name"], courses[index]["year"], exercise_total)
            active_course.append(full_info)

    return active_course


def retrieve_course(course: str):
    my_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    request = my_request.read()
    courses = json.loads(request)

    address = "https://studies.cs.helsinki.fi/stats-mock/api/courses/****/stats".replace("****", course)
    my_request2 = urllib.request.urlopen(address)
    request2 = my_request2.read()
    courses2 = json.loads(request2)

    total_hours = 0
    exercises_total = 0
    for index in range(len(courses2)):
        total_hours += (courses2[f"{index}"]["hour_total"])
        exercises_total += (courses2[f"{index}"]["exercise_total"])

    full_info = {}
    for index in range(len(courses)):
        if courses[index]["name"] == course:
            full_info = {'weeks': courses[index]["week"], 'students': courses2["0"]["students"], 'hours':
                total_hours, 'hours_average': total_hours // courses2["0"]["students"], 'exercises':
                             exercises_total, 'exercises_average': exercises_total // courses2["0"]["students"]}

    return full_info



if __name__ == '__main__':
    print(retrieve_all())
    print(retrieve_course("CCFUN"))

"""
Saker att göra:
anropa retrieve all från retrieve_course istället för att göra ett nytt anrop. 
Se till att total_hours += (courses2[f"{index}"]["hour_total"]) justeras efter vad kursen börjar på
vissa börjar på 0 andra 1 osv
"""