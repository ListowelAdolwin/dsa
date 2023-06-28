# Here, we use recursion to reverse a string

def reverse(str):
    if len(str) == 1:
        return str[0]
    return reverse(str[1:len(str)]) + str[0]


print(reverse("Listowel"))
print(reverse("Hello world"))
