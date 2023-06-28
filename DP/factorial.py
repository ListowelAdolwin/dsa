# Using recursion to find the factorial of a number

def factorial(n):
    memo = {1:1}
    def fact(n):
        if n not in memo:
            memo[n] = n * fact(n - 1)
        return memo[n]
    return fact(n)


print(factorial(421))
