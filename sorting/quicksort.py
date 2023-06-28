# Quick sort implementation

def partition(arr, left, right):
    pivot = left

    while left < right:
        while (arr[left]) <= arr[pivot]:
            left += 1
        
        while arr[right] > arr[pivot]:
            right -= 1

        if left < right:
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp

    temp = arr[pivot]
    arr[pivot] = arr[right]
    arr[right] = temp
    
    return right

def quicksort(arr, left, right):
    if right - left <= 0:
        return

    index = partition(arr, left, right)

    quicksort(arr, left, index - 1)
    quicksort(arr, index + 1, right)


arr = [34, 14, 432, 14,124]
(quicksort(arr, 0, 4))
print(arr)
