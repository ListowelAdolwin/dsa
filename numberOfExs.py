# This program calculates the number of appearances of x in a string

def x_times(str):
    if len(str) == 1:
        if str[0] == 'x':
            return 1
        else:
            return 0


    if str[0] == 'x':
        return 1 + x_times(str[1:len(str)])
    else:
        return 0 + x_times(str[1:len(str)])


print(x_times("gexigexgex"))
print(x_times("xxxxxxxx"))
