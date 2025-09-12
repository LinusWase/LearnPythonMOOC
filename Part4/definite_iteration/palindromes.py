"""
Please write a function named palindromes, which takes a string argument and returns True if the string is a palindrome.
Palindromes are words which are spelled exactly the same backwards and forwards.

Please also write a main program which asks the user to type in words until they type in a palindrome:
Sample output

Please type in a palindrome: python
that wasn't a palindrome
Please type in a palindrome: java
that wasn't a palindrome
Please type in a palindrome: oddoreven
that wasn't a palindrome
Please type in a palindrome: neveroddoreven
neveroddoreven is a palindrome!

NB:, the main program should not be within an if __name__ == "__main__": block
"""

def palindromes(string):
    my_list = list(string)
    my_list_reverse = list(reversed(my_list))
    if my_list == my_list_reverse:
        return True
    return False

while True:
    user_input = input("Please type in a palindrome: ")
    if palindromes(user_input):
        print(f"{user_input} is a palindrome!")
        break
    print("that wasn't a palindrome")
