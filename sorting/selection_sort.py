#bin/usr/python3


def selection(arr):
    for i in range(len(arr)):
        minn = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minn]:
                minn = j
        arr[minn], arr[i] = arr[i], arr[minn]


arr = [2, 1, 3, 2, 5, 1, 7, 3, 9, 4]
selection(arr)
print(arr)
