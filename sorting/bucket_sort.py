#bin/usr/python


def bucket_sort(arr):
    count = [0] * (max(arr) + 1)
    for n in arr:
        print(n)
        count[n] = count[n] + 1
    print(count)

    i = 0
    result = []
    for n in range(len(count)):
        for _ in range(count[n]):
            arr[i] = n
            i += 1
arr =[1, 5, 4, 3, 1]
bucket_sort(arr)
print(arr)
