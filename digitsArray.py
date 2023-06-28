def digitsArray(digits):
    n = len(digits)
    for i in range(n):
        index = n - 1 - i

        if digits[index] == 9:
            digits[index] = 0

        else:
            digits[index] += 1

    return[1] + (digits)


def main():
    digits = [1, 3, 4, 9]
    digitsArray(digits)
    print(digits)

main()
