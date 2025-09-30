from datetime import datetime

def is_it_valid(pic: str):
    try:
        if len(pic) != 11:
            return False
        if pic[6] == "+":
            year = 1800 + int(pic[4:6])
        elif pic[6] == "-":
            year = 1900 + int(pic[4:6])
        elif pic[6] == "A":
            year = 2000 + int(pic[4:6])
        else:
            return False

        month = pic[2:4].replace("0", "",)
        day = pic[0:2]
        birthday = datetime(year, int(month), int(day))

        check_valid = pic[0:10].replace("-", "").replace("+", "").replace("A","")

        char = "0123456789ABCDEFHJKLMNPRSTUVWXY"
        if char[int(check_valid) % 31] == pic[10]:
            return True
    except:
        return False


if __name__ == '__main__':
    print(is_it_valid("230827-906F"))
    print(is_it_valid("120488+246L"))
    print(is_it_valid("310823A9877"))
    print(is_it_valid("081842-720N"))