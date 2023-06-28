def find_missing_number(arr):
    """
    This function takes a number n and finds the missing from the set of numbers 1 to n.
    """
    n = len(arr)
    # The formular s = n(n + 1)/2 can be used to make the work easier.
    sum_with_missing_number = (n * (n + 1)) / 2
    sum_without_missing_number = sum(arr)
    missing_number = sum_without_missing_number - sum_with_missing_number
    return missing_number

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
print(find_missing_number(arr))
