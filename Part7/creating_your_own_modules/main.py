from words import first_word, last_word
import words

def creating_your_own_modules():
    my_string = "Sheila sells seashells by the seashore"

    print(words.first_word(my_string))
    print(words.last_word(my_string))
    print(words.number_of_words(my_string))

    sentence = input("Please type in a sentence: ")

    print("The first word was: " + first_word(sentence))
    print("The last word was: " + last_word(sentence))


creating_your_own_modules()