"""
Please write a program which asks the user which editor they are using. The program should keep on asking until the
user types in Visual Studio Code.

Have a look at the example of expected behaviour below:
Sample output

Editor: Emacs
not good
Editor: Vim
not good
Editor: Word
awful
Editor: Atom
not good
Editor: Visual Studio Code
an excellent choice!

If the user types in Word or Notepad, the program counters with awful. Other unacceptable editor choices receive the
reply not good.

The program should be case-insensitive in its reactions. That is, the same user input in lowercase, uppercase or mixed
case should trigger the same reaction:
Sample output

Editor: NOTEPAD
awful
Editor: viSUal STudiO cODe
an excellent choice!

Hint: The simplest way to achieve this is converting all characters to the same case. The Python string method lower
converts a string to lowercase entirely. An example of its use:

mystring = "Visual Studio CODE"
if "visual studio code" == mystring.lower():
    print("this was the string I was looking for!")

NB: this exercise doesn't ask you to write any functions, so you should not place any code within an
if __name__ == "__main__" block. The same applies to any upcoming exercises that don't explicitly ask for functions.
"""

while True:
    user_input = input("Editor: ")
    user_inp_lower = user_input.lower()

    if user_inp_lower == "word" or user_inp_lower == "notepad":
        print("awful")
    elif user_inp_lower == "visual studio code":
        print("an excellent choice!")
        break
    else:
        print("not good")