def new_person(name: str, age: int):
        if len(name) != 0:
            if " " in name:
                if len(name) < 40:
                    if age > 0:
                        if age < 150:
                            person = (name, age)
                            return person

        raise ValueError





if __name__ == '__main__':
    print(new_person('Andrew', 32))