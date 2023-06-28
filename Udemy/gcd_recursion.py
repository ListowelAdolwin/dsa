# The GCD of any set of numbers is the largest factor that can divide all the numbers
# e.g 4 is the GCD of 12 and 8, 5 is the GCD of 5, 10 and 20
def gcd(num1, num2):
    if num2 == 0:
        return num1
    remainder = num1 % num2
    return gcd(num2, remainder)

print(gcd(18, 48))
