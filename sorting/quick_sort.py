#bin/usr/python


def partition(arr, l, r):
    pivot = l

    while (True):
        while arr[l] < arr[pivot]:
            l += 1

        while (arr[r] > arr[pivot]):
            r -= 1

        if l >= r:
            break

        else:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1

    arr[pivot], arr[r] = arr[r], arr[pivot]
     
    return r

def quick_sort(arr, l, r):
    if r - l <= 0:
        return

    index = partition(arr, l, r)

    quick_sort(arr, l, index - 1)

    quick_sort(arr, index + 1, r)



arr = [3, 5, 3, 3, 2, 2, 4, 5, 7, 23, 1]
quick_sort(arr, 0, 10)
print(arr)
