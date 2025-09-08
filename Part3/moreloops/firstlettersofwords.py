"""
Please write a program which asks the user to type in a sentence. The program then prints out the first letter of
each word in the sentence, each letter on a separate line.

An example of expected behaviour:
Sample output

Please type in a sentence: Humpty Dumpty sat on a wall
H
D
s
o
a
w
"""

sentence = input("Please type in a sentence: ")
substring = " "

while sentence != " ":
    if substring in sentence:
        index = sentence.find(substring)
        print(sentence[:1])
        sentence = sentence[index+1:]
    else:
        print(sentence[:1])
        break

