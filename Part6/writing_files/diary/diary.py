def add_an_entry():
    diary_entry = input("Diary entry: ")
    with open("diary.txt", "a") as file:
        file.write(diary_entry + '\n')
    print("Diary saved")
    print()

def read_entries():
    print("Entries:")
    with open("diary.txt") as file:
        for line in file:
            print(line, end="")

def main():
    while True:
        print("1 - add an entry, 2 - read entries, 0 - quit")
        user_input = int(input("Function: "))
        if user_input == 0:
            print("Bye now!")
            break
        elif user_input == 1:
            add_an_entry()
        elif user_input == 2:
            read_entries()

main()