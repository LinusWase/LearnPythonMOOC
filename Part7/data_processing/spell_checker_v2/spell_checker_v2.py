import difflib

def main():
    user_input = input("Write text: ")
    words = user_input.split()
    correct_word = []
    incorrect_word = []

    with open("wordlist.txt") as file:
        wordlist = {word.strip() for word in file}
        for word in words:
            if word.lower() not in wordlist:
                correct_word.append(f"*{word}*")
                incorrect_word.append(word)
            else:
                correct_word.append(word)

    for word in correct_word:
        print(word, end=" ")

    print("\nsuggestions:")
    for word in incorrect_word:
        possible = difflib.get_close_matches(f'{word}', wordlist)
        str_possible = ', '.join(possible)
        print(f"{word}: {str_possible}")

main()
