def sum_digits(num):
    assert num >= 0 and int(num) == num, "Number should be a postive integer number"
    if not num:
        return 0
    digit = num % 10
    return digit + sum_digits(num // 10)

print(sum_digits(-12))
