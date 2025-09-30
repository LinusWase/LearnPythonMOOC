import json

def print_persons(filename: str):
    with open(filename) as my_file:
        data = my_file.read()
    persons = json.loads(data)
    for person in persons:
        print(person["name"], person["age"], "years", "(", end="")
        counter = 1
        for hobby in person["hobbies"]:
            print(hobby, end="")
            if counter == len(person["hobbies"]):
                break
            print(", ", end="")
            counter += 1
        print(")")

if __name__ == '__main__':
    print_persons("file.json")