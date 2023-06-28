# Generate the fibonacci series

def fib(first, second, n):
    arr = [first, second]
    for i in range(2, n):
        curr = first + second
        arr.append(curr)
        first = second
        second = curr
    return arr

print(fib(1, 2, 20))
print(fib(1, 3, 10))
