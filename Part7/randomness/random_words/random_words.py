from random import sample


def words(n: int, beginning: str):
    my_word_list = []
    with open("words.txt") as new_file:
        for line in new_file:
            if line[0:len(beginning)] == beginning:
                my_word_list.append(line.strip())

    if not len(my_word_list) <= n:
        chosen_words = sample(my_word_list, n)
        return chosen_words
    else:
        raise ValueError




if __name__ == '__main__':
    word_list = words(2, "zwat")
    for word in word_list:
        print(word)