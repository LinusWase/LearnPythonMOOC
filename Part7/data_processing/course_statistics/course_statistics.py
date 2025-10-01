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
    url_name = "https://studies.cs.helsinki.fi/stats-mock/api/courses/****/stats".replace("****", course)
    my_request = urllib.request.urlopen(url_name)
    read_my_request = my_request.read()
    course = json.loads(read_my_request)

    total_hours = 0
    total_exercises = 0
    total_students = 0
    total_weeks = len(course.keys())
    for key, value in course.items():
        if total_students == 0:
            total_students += (course[key]["students"])
        total_hours += (course[key]["hour_total"])
        total_exercises += (course[key]["exercise_total"])

    full_info = {'weeks':total_weeks,
                 'students': total_students,
                 'hours':total_hours,
                 'hours_average':total_hours // total_students,
                 'exercises':total_exercises,
                 'exercises_average':total_exercises // total_students}
    return full_info



if __name__ == '__main__':
    print(retrieve_all())
    print(retrieve_course("docker2019"))

"""
Saker att göra:
anropa retrieve all från retrieve_course istället för att göra ett nytt anrop. 
Se till att total_hours += (courses2[f"{index}"]["hour_total"]) justeras efter vad kursen börjar på
vissa börjar på 0 andra 1 osv
"""