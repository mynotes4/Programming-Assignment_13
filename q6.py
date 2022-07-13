"""Question 6:
A website requires the users to input username and password to register. Write a program to
check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them
according to the above criteria. Passwords that match the criteria are to be printed, each
separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1"""

def check_password(s):
    # l = []  # l contains true or false according to following conditions
    # # l[0] = At least 1 letter between[a - z]
    # # l[1] = At least 1 number between[0 - 9]
    # # l[2] = At least 1 letter between[A - Z]
    # # l[3] = At least 1 character from [$  # @]
    # # l[4] = Length between 6 and 12
    if len(s) >=  6 and len(s) <= 12:
        pass
    else:
        return False
    for i in s:
        if i >= 'a' and i <= 'z':
            break
    else:
        return False
    for i in s:
        if i >= 'A' and i <= 'Z':
            break
    else:
        return False
    for i in s:
        if i >= '0' and i <= '9':
            break
    else:
        return False
    for i in s:
        if i in '$#@':
            break
    else:
        return False
    return True

def check_list(s):
    s = s.split(',')
    valid_password = []
    for i in s:
        if check_password(i):
            valid_password.append(i)
    return ','.join(valid_password)
s = input("Enter Input ")
print(check_list(s))