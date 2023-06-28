# Here, I make use of a stack to reverse a string


def reverse(string):
    stack = []
    newStr = ""
    for s in string:
        stack.append(s)

    for i in range(len(string)):
        newStr += stack.pop()
    return newStr

print(reverse("Listowel"))
print(reverse("Hello worl"))
