# Spell checker, version 2

In this exercise you will write an improved version of the Spell checker from the [previous part](https://programming-25.mooc.fi/part-6/1-reading-files).

Just like in the previous version, the program should ask the user to type in a line of text. Your program should then perform a spell check, and print out feedback to the user, so that all misspelled words have stars around them. Additionally, the program should print out a list of suggestions for the misspelled words.

Please have a look at the following two examples.

### Sample output

>write text: We use ptython to make a spell checker <br>

>We use *ptython* to make a spell checker <br>
>suggestions: <br>
>ptython: python, pythons, typhon <br>

### Sample output

>write text: this is acually a good and usefull program <br>

>this is *acually* a good and *usefull* program <br>
>suggestions: <br>
>acually: actually, tactually, factually<br>
>usefull: usefully, useful, museful <br>

The suggestions should be determined with the function [get_close_matches](https://docs.python.org/3/library/difflib.html#difflib.get_close_matches) from the Python standard library module 
[difflib](https://docs.python.org/3/library/difflib.html).

__NB:__ For the automatic tests to work correctly, please use the function with the "default settings". That is, please 
pass only two arguments to the function: the misspelled word, and the word list.
