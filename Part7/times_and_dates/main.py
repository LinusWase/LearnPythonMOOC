from datetime import datetime, timedelta


def datetime_object():
    my_time = datetime.now()
    print(my_time)

    my_time = datetime(1980, 9, 30)
    print("Day:", my_time.day)
    print("Month:", my_time.month)
    print("Year:", my_time.year)

    pv1 = datetime(1980, 9, 30, 14)
    pv2 = datetime(1980, 9, 30, 21, 32, 22, 22,)
    print(pv1)
    print(pv2)

def compare_times_and_calculate_differences_between_them():
    time_now = datetime.now()
    midsummer = datetime(2025, 6, 20)

    if time_now < midsummer:
        print("It is not yet Midsummer")
    elif time_now == midsummer:
        print("Happy Midsummer!")
    elif time_now > midsummer:
        print("It is past Midsummer")

    difference = midsummer - time_now
    print("Midsummer is", difference.days, "days away")

    one_week = timedelta(days=7)
    week_from_date = midsummer + one_week

    print("A week after Midsummer it will be", week_from_date)

    long_time = timedelta(weeks=32, days=15)

    print("32 weeks and 15 days after Midsummer it will be", midsummer + long_time)

    midnight = datetime(2025, 10, 1)
    difference = midnight - time_now
    print(f"Midnight is still {difference.seconds} seconds away")


def formatting_times_and_dates():
    my_time = datetime.now()
    print(my_time.strftime("%d.%m.%Y"))
    print(my_time.strftime("%d/%m/%Y %H:%M"))

    birthday = input("Please type in your birthday in the format dd.mm.yyyy: ")
    my_time = datetime.strptime(birthday, "%d.%m.%Y")
    print(my_time)

    if my_time < datetime(2000, 1, 1):
        print("You were born in the previous millennium")
    else:
        print("You were born during this millennium")

if __name__ == '__main__':
    #datetime_object()
    #compare_times_and_calculate_differences_between_them()
    formatting_times_and_dates()