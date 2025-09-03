letter1 = input("1st letter: ")
letter2 = input("2nd letter: ") #mitten
letter3 = input("3rd letter: ")

middle_letter =""

if (letter1 > letter3 and letter1 < letter2) or (letter1 < letter3 and letter1 > letter2):
    middle_letter = letter1
elif (letter2 > letter3 and letter2 < letter1) or (letter2 < letter3 and letter2 > letter1):
    middle_letter = letter2
else:
    middle_letter = letter3


print(f"The letter in the middle is {middle_letter}")
