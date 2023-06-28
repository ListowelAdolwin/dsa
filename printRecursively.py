# Using recursion to print numbers

def printRecursively(n):
    if n <= 0:
        return
    print(n)
    printRecursively(n - 1)

printRecursively(20)
