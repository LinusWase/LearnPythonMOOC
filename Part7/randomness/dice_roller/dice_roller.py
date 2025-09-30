from random import choice


def roll(die: str):
    if die == "A":
        return choice([3, 3, 3, 3, 3, 6])
    elif die == "B":
        return choice([2, 2, 2, 5, 5, 5])
    elif die == "C":
        return choice([1, 4, 4, 4, 4, 4])

def play(die1: str, die2: str, times: int):
    first_won = 0
    second_won = 0
    tie = 0
    for i in range(times):
        first_dice = roll(die1)
        second_dice = roll(die2)

        if first_dice > second_dice:
            first_won += 1
        elif second_dice > first_dice:
            second_won += 1
        else:
            tie += 1

    return first_won, second_won, tie



if __name__ == '__main__':
    for i in range(20):
        print(roll("A"), " ", end="")
    print()
    for i in range(20):
        print(roll("B"), " ", end="")
    print()
    for i in range(20):
        print(roll("C"), " ", end="")

    result = play("A", "C", 1000)
    print(result)
    result = play("B", "B", 1000)
    print(result)