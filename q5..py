"""Question 5:
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
"""

def letters_count(s):
    letters = 0
    for i in s:
        if ( i >= 'a' and i <='z' ) or ( i >= 'A' and i <='Z' ):
            letters = letters + 1
    return letters

def digits_count(s):
    digits = 0
    for i in s:
        if i >= '0' and i <='9':
            digits = digits + 1
    return digits

def count(s):
    print("LETTERS",letters_count(s))
    print("DIGITS",digits_count(s))

s = input("Enter Input ")
count(s)