# bin/usr/python


def merge_sort(arr, l, r):
    # Check if array has only one element(means it is sorted)
    if r - l + 1 <= 1:
        return arr
    #Divide the array into two
    m = (r + l) // 2
    # sort the first half
    merge_sort(arr, l, m)
    # sort the second half
    merge_sort(arr, m + 1, r)

    # Merge the two sorted halves
    merge(arr, l, r, m)
    return arr


def merge(arr, l, r, m):
    k = l
    # copy first half into a new array
    l1 = arr[l:m+1]
    # copy second half into new array
    l2 = arr[m+1:r+1]
    i, j = 0, 0
    # merge the two arrays
    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            arr[k] = l1[i]
            i += 1
        else:
            arr[k] = l2[j]
            j += 1
        k += 1
    # append l1 to the merged array if there is still l1
    while i < len(l1):
        arr[k] = l1[i]
        i += 1
        k += 1

    # append l2 to the merged array if there is still l2
    while j < len(l2):
        arr[k] = l2[j]
        j += 1
        k += 1

    return arr


arr = [3, 52, 36, 200, 2, 4, 5, 7, 23, 1000, 67]
merge_sort(arr, 0, 10)
print(arr)
