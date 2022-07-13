"""Question 1:
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24"""

import math

def str_int(s):
    sp = s.split(',')
    l = []
    for i in sp:
        l.append(int(i))
    return l

def int_str(l):
    s = ''
    for i in range(len(l)):
        if i < len(l) - 1:
            s = s + str(l[i]) + ','
        else:
            s = s + str(l[i])
    return s

def cal(l):
    l = str_int(l)
    ls = []
    C = 50
    H = 30
    for D in l:
        ls.append(int(math.sqrt((2*C*D)/H)))
    return int_str(ls)

s = input("Enter comma seperated sequence ")
l = cal(s)
print(l)