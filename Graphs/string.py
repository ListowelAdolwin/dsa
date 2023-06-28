#!/usr/bin/python3

def string_manipulation(pattern):
    lenn = len(pattern)
    i = 0
    for i in range((len(pattern) - 1)):
        if pattern[i] == 'a' and pattern[i + 1] != 'b':
            pattern.insert(i + 1, 'b')

        elif pattern[i] == 'b' and pattern[i + 1] != 'c':
            pattern.insert(i + 1, 'c')

        elif pattern[i] == 'c' and pattern[i + 1] != 'a':
            pattern.insert(i + 1, 'a')
        lenn = len(pattern)
    print(pattern)



def man(str):
    result = []
    for i in range(len(str)):
        result.append(str[i])
        if str[i] == 'a' and str[i + 1] != 'b':
            result.append('b')
        elif str[i] == 'b' and str[i + 1] != 'c':
            result.append('c')
        elif str[i] == 'c' and str[i + 1] != 'a':
            result.append('a')

    print(result)
examp = "ab"
man(examp)

