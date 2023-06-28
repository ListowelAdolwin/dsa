#include <iostream>
using namespace std;

void print_arr(int * arr, int lenn);
void swap_vals(int * arr, int i, int j);

int main(){
    int arr[] = {3, 4, 3, 4, 6, 7, 34, 32, 53,1000, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    int temp;
    cout<<"Before sorting: "<<endl;
    print_arr(arr, n);

    for (int pass = 0; pass < n; pass++) {
        for (int comp = 1; comp < n - pass; comp++) {
            if (arr[comp] < arr[comp - 1]){
                //swap_vals(arr, comp, comp - 1);
                temp = arr[comp];
                arr[comp] = arr[comp - 1];
                arr[comp - 1] = temp;
            }
        }
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
