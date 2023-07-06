/* TIME COMPLEXITY
    BEST - O(N)
    AVERGGE - O(N^2)
    WORST - O(N^2)

    SPACE COMPLEXITY - O(N^2)
*/

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

    for (int pass = 1; pass < n; pass++) {
        int curr = pass;
        while (curr > 0){
            if (arr[curr] < arr[curr - 1]){
                temp = arr[curr];
                arr[curr] = arr[curr - 1];
                arr[curr - 1] = temp;
            }
            else {
                break;
            }
            curr--;
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
