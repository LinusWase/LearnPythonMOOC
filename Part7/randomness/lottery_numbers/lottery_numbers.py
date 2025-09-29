from random import sample


def lottery_numbers(amount: int, lower: int, upper: int):
    number_pool = list(range(lower, upper))
    numbers = sample(number_pool, amount)
    numbers.sort()
    return numbers

if __name__ == '__main__':
    for number in lottery_numbers(3, 2, 22):
        print(number)