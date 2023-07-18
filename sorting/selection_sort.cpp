#include <iostream>
using namespace std;

void print_arr(int * arr, int lenn);
void swap_vals(int * arr, int i, int j);

int main(){
    int arr[] = {3, 4, 6, 7, 34, 32, 53,1000, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    int temp;
    cout<<"Before sorting: "<<endl;
    print_arr(arr, n);

    for (int pass = 0; pass < n; pass++) {
        int minn = pass;
        for (int comp = pass + 1; comp < n; comp++)
            if (arr[comp] < arr[minn])
                minn = comp;

        temp = arr[minn];
        arr[minn] = arr[pass];
        arr[pass] = temp;
    }

    cout<<"After sorting: "<<endl;
    print_arr(arr, n);
    return 0;
}

void print_arr(int * arr, int lenn) {
    for (int i = 0; i < lenn; i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;
}

void swap_vals(int * arr, int i, int j){
    int temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
}
