# Convert a decimal number to binary

def binary(num, result=[]):
    if not num:
        return
    digit = num % 2
    result.append(digit)
    binary(num // 2, result)
    return result[-1::-1]



def binary2(num):
    if not num:
        return 0
    return num % 2 + 10 * binary2(num // 2)

print(binary(574))
print(binary2(574))
