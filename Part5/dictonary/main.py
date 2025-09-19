def using_a_dictionary():
    my_dictionary = {}

    my_dictionary["apina"] = "monkey"
    my_dictionary["banaani"] = "banana"
    my_dictionary["cembalo"] = "harpsichord"

    print(len(my_dictionary))
    print(my_dictionary)
    print(my_dictionary["apina"])

    word = input("Please type in a word: ")
    if word in my_dictionary:
        print("Translation:", my_dictionary[word])
    else:
        print("Word not found")


def what_can_be_stored_in_a_dictionary():
    results = {}
    results["Mary"] = 4
    results["Alice"] = 5
    results["Larry"] = 2

    lists = {}
    lists[5] = [1,2,3]
    lists[42] = [5,4,5,4,5]
    lists[100] = [5,2,2]

def how_key_and_values_work():
    my_dictionary = {}

    my_dictionary["suuri"] = "big"
    my_dictionary["suuri"] = "large"
    print(my_dictionary["suuri"])

def traversing_a_dictionary():
    my_dictionary = {}

    my_dictionary["apina"] = "monkey"
    my_dictionary["banaani"] = "banana"
    my_dictionary["cembalo"] = "harpsichord"

    for key in my_dictionary:
        print("key:", key)
        print("value:", my_dictionary[key])
        print()

    for key, value in my_dictionary.items():
        print("key:", key)
        print("value:", value)


# Some more advanced ways to use dictionaries

word_list = [
  "banana", "milk", "beer", "cheese", "sourmilk", "juice", "sausage",
  "tomato", "cucumber", "butter", "margarine", "cheese", "sausage",
  "beer", "sourmilk", "sourmilk", "butter", "beer", "chocolate"
]

def counts(my_list : list):
    words = {}
    for word in my_list:
        if word not in words:
            words[word] = 0
        words[word] += 1
    return words

def categorize_by_initial(my_list: list):
    groups = {}
    for word in my_list:
        initial = word[0]
        if initial not in groups:
            groups[initial] = []
        groups[initial].append(word)
    return groups
"""
groups = categorize_by_initial(word_list)

for key, value in groups.items():
    print(f"words beginning with {key}:")
    for word in value:
        print(word)
"""

def removing_keys_and_values_from_a_dictionary():
    staff = {"Alan": "lecturer", "Emily": "professor", "David": "lecturer"}
    if "Paul" in staff:
        del staff["Paul"]
        print("Deleted")
    else:
        print("This person is not a staff member")

    deleted = staff.pop("David", None)
    print(staff)
    if deleted == None:
        print("This person is not a staff member")
    else:
        print(deleted, "deleted")

    staff.clear()
    print(staff)

def using_dictionaries_for_structured_data():
    person1 = {"name": "Pippa Python", "height": 154, "weight": 61, "age": 44}
    person2 = {"name": "Peter Pythons", "height": 174, "weight": 103, "age": 31}
    person3 = {"name": "Pedro Python", "height": 191, "weight": 71, "age": 14}

    people = [person1, person2, person3]

    for person in people:
        print(person["name"])

    combined_height = 0
    for person in people:
        combined_height += person["height"]

    print("The average height is", combined_height / len(people))

if __name__ == '__main__':
    #using_a_dictionary()
    #what_can_be_stored_in_a_dictionary()
    #how_key_and_values_work()
    #traversing_a_dictionary()
    #print(counts(word_list))
    #removing_keys_and_values_from_a_dictionary()
    using_dictionaries_for_structured_data()
