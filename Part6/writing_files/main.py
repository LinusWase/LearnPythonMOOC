import os

def creating_a_new_file():
    with open("new_file.txt", "w") as my_file:
        my_file.write("Hello there!\n")
        my_file.write("This is the second line\n")
        my_file.write("This is the last line\n")


def appending_data_to_an_existing_file():
    with open("new_file.txt", "a") as file: #"a" means append mode
        file.write("This is the 4th line\n")
        file.write("And yet another line.\n")

def writing_CSV_files():
    with open("coders.csv", "w") as file:
        file.write("Eric;Windows;Pascal;10\n")
        file.write("Matt;Linux;PHP;2\n")
        file.write("Alan;Linux;Java;17\n")
        file.write("Emily;Mac;Cobol;9\n")

    coders = []
    coders.append(["Eric", "Windows", "Pascal", 10])
    coders.append(["Matt", "Linux", "PHP", 2])
    coders.append(["Alan", "Linux", "Java", 17])
    coders.append(["Emily", "Mac", "Cobol", 9])

    with open("coders.csv", "w") as file:
        for coder in coders:
            line = f"{coder[0]};{coder[1]};{coder[2]};{coder[3]}"
            file.write(line+"\n")

    with open("coders.csv", "w") as my_file:
        for coder in coders:
            line = ""
            for value in coder:
                line += f"{value};"
            line = line[:-1]
            my_file.write(line + "\n")

def clearing_file_contents_and_deleting_files():
    with open("new_file.txt", "w") as file:
        pass

    #or

    open("new_file.txt", "w").close()

def remove_a_file():
    os.remove("new_file.txt")


def main():
    #creating_a_new_file()
    #appending_data_to_an_existing_file()
    #writing_CSV_files()
    #clearing_file_contents_and_deleting_files()
    #remove_a_file()

main()