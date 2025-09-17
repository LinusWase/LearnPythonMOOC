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


if __name__ == '__main__':
    #using_a_dictionary()
    #what_can_be_stored_in_a_dictionary()
    how_key_and_values_work()