def find_words(search_term: str):
    word_list = []
    search_term_without = search_term.replace("*", "").replace(".", "")
    with open("words.txt") as new_file:
        for word in new_file:
            word = word.strip()
            if "*" in search_term:
                if "*" == search_term[0]:
                    if word.endswith(search_term_without):
                        word_list.append(word)
                elif "*" == search_term[-1]:
                    if word.startswith(search_term_without):
                        word_list.append(word)

            if "." in search_term:
                if len(word) == len(search_term):
                    match_index = 0
                    for char in word:
                        if search_term[match_index] == ".":
                            match_index += 1
                            continue
                        elif word[match_index] == search_term[match_index]:
                            match_index += 1
                    if match_index == len(search_term):
                        word_list.append(word)
    if search_term == search_term_without:
        word_list.append(search_term)
    return word_list


if __name__ == '__main__':
    print(find_words("cat"))