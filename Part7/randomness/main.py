from random import randint, sample
from random import shuffle
from random import choice
from random import seed

def generating_a_random_number():
    print("The result of the throw:", randint(1,6))

    for i in range(10):
        print("The result of the throw:", randint(1,6))


def randomizing_functions():
    words = ["atlas", "banana", "carrot"]
    shuffle(words)
    print(words)
    print(choice(words))

def lottery_numbers():
    for i in range(7):
        print(randint(1,40))

    weekly_draw = []
    while len(weekly_draw) < 7:
        new_rnd = randint(1,40)
        if new_rnd not in weekly_draw:
            weekly_draw.append(new_rnd)

    print(weekly_draw)

    #more compact version:

    number_pool = list(range(1,41))
    shuffle(number_pool)
    weekly_draw = number_pool[0:7]
    print(weekly_draw)

    #even more compact:
    number_pool = list(range(1,41))
    weekly_draw = sample(number_pool, 7)
    print(weekly_draw)

def where_do_these_random_numbers_come_from():
    seed(1337)
    #always the same "random" number
    print(randint(1,100))


def main():
    #generating_a_random_number()
    #randomizing_functions()
    #lottery_numbers()
    where_do_these_random_numbers_come_from()

main()