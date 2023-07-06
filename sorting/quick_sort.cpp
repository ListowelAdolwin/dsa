#include <iostream>
using namespace std;

int partition(int arr[], int left, int right) {
    int pivot = left;

    while (left < right) {
        while (arr[left] <= arr[pivot])
            left++;

        while (arr[right] > arr[pivot])
            right--;

        if (left < right) {
            int temp = arr[left];
            arr[left] = arr[right];
            arr[right] = temp;
        }
    }

    int temp = arr[pivot];
    arr[pivot] = arr[right];
    arr[right] = temp;

    return right;
}

void quicksort(int arr[], int left, int right) {
    if (right - left <= 0)
        return;

    int index = partition(arr, left, right);

    quicksort(arr, left, index - 1);
    quicksort(arr, index + 1, right);
}

int main() {
    int arr[] = {34, 14, 432, 14, 124};
    int size = sizeof(arr) / sizeof(arr[0]);

    quicksort(arr, 0, size - 1);

    cout << "Sorted array: ";
    for (int i = 0; i < size; i++)
        cout << arr[i] << " ";

    return 0;
}

