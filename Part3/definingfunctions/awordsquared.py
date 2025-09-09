"""
Please write a function named squared, which takes a string argument and an integer argument, and prints out a square
of characters as specified by the examples below.

squared("ab", 3)
print()
squared("aybabtu", 5)

Sample output

aba
bab
aba

aybab
tuayb
abtua
ybabt
uayba

"""

def squared(word, times):
    original_times = times
    total_word = word * (times * times)

    while times > 0:
        print(total_word[:original_times])
        total_word = total_word[original_times:]
        times -= 1


if __name__ == "__main__":
    squared("python", 15)
