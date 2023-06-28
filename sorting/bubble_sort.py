#bin/usr/python3


def bubble(arr):
    for i in range(len(arr)):
        for j in range(1, len(arr) - i):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
        print(f"Pass{i}:{arr}")


arr = [2, 3, 14, 5, 2, 3,1, 5, 7, 2, 9, 7,8]
bubble(arr)
print(arr)
