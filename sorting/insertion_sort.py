#bin/usr/python3


def insertion(arr):
    for i in range(1, len(arr)):
        j = i - 1
        temp = arr[i]
        while (j >= 0 and arr[j] > temp):
            arr[j + 1], arr[j] = arr[j], arr[j + 1]
            j -= 1
        arr[j + 1], temp = temp, arr[j + 1]


arr = [4, 5, 3, 3, 2, 2, 5, 1, -3]
insertion(arr)
print(arr)
