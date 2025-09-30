from datetime import datetime, timedelta


def main():
    filename = input("Filename: ")
    user_starting_date = input("Starting date: ")
    starting_date = datetime.strptime(user_starting_date, "%d.%m.%Y")
    orginal_starting = starting_date
    how_may_days = int(input("How many days: "))
    one_day = timedelta(days=1)
    end_days = (how_may_days - 1) * one_day + starting_date
    screen_per_day = []
    day_list = []

    for i in range(how_may_days):
        screen_time = input(f"Screen time {starting_date.strftime("%d.%m.%Y")}: ")
        screen_per_day.append(screen_time.replace(" ", "/"))
        day_list.append(starting_date.strftime("%d.%m.%Y"))
        starting_date = starting_date + one_day
    print(f"Data stored in file {filename}")

    another_list = []
    for item in screen_per_day:
        new_list = item.split("/")
        another_list += list(map(int, new_list))
    total_minutes = sum (another_list)

    starting_date = starting_date + one_day
    with open(filename, "w") as file:
        file.write(f"Time period: {orginal_starting.strftime("%d.%m.%Y")}-{end_days.strftime("%d.%m.%Y")}" + '\n')
        file.write(f"Total minutes: {total_minutes}" + '\n')
        file.write(f"Average minutes: {total_minutes/how_may_days}" + '\n')
        for i in range(how_may_days):
            file.write(f"{day_list[i]}: {screen_per_day[i]}" + '\n')

main()