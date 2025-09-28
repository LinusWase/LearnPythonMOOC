def store_personal_data(person: tuple):
    my_list = []
    with open("people.csv", "a") as new_file:
        for item in person:
            my_list.append(item)
        new_file.write(f"{my_list[0]};{my_list[1]};{my_list[2]}\n")

if __name__ == '__main__':
    store_personal_data(("Paul Paul", 37, 175.5))