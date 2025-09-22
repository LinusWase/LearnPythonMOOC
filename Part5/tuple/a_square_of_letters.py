"""
This final exercise in this part is a relatively demanding problem solving task. It can be solved in many different
ways. Even though this current section in the material covers tuples, tuples are not necessarily the best way to go
about solving this.

Please write a program which prints out a square of letters as specified in the examples below. You may assume there
will be at most 26 layers.
Sample output

Layers: 3

CCCCC
CBBBC
CBABC
CBBBC
CCCCC

Sample output

Layers: 4

DDDDDDD
DCCCCCD
DCBBBCD
DCBABCD
DCBBBCD
DCCCCCD
DDDDDDD

NB: this exercise doesn't ask you to write any functions, so you should not place any code within an
if __name__ == "__main__" block.
"""
def print_letter(letters: list, user_input: int):

    #print(letters[user_input-1] * ((user_input*2) -1))
    for i in range(1, (user_input * 2)):
        print(letters[user_input-i] * ((user_input*2)-1))



def main():
    letters = []
    for i in range(65, 91): #ASCII for letters A to Z
        letters += chr(i)
    user_input = int(input("Layers: "))
    print_letter(letters, user_input)

main()