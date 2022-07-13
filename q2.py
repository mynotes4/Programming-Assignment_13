"""Question 2:
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] """

def str_int(s):
    sp = s.split(',')
    l = []
    for i in sp:
        l.append(int(i))
    return l

def cal(s):
    n = str_int(s)
    l = []
    for i in range(n[0]):
        l.append([])
        for j in range(n[1]):
            l[i].append(i*j)
    return l

s = input("Enter Input ")
l = cal(s)
print(l)