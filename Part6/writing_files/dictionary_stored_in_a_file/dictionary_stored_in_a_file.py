def add_word_to_dictionary():
    finnish_word = input("The word in Finnish: ")
    english_word = input("The word in English: ")
    together = finnish_word + " - " + english_word
    with open("dictionary.txt", "a") as file:
        file.write(together + '\n')
    print("Dictionary entry added")

def find_word():
    search_term = input("Search term: ")
    with open("dictionary.txt") as file:
        for line in file:
            if search_term in line:
                print(line.strip())


def main():
    while True:
        print("1 - Add word, 2 - Search, 3 - Quit")
        user_input = int(input("Function: "))
        if user_input == 3:
            print("Bye!")
            break
        elif user_input == 1:
            add_word_to_dictionary()
        elif user_input == 2:
            find_word()



main()