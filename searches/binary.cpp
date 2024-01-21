#include<iostream>
using namespace std;

int binarySearch(int arr[], int n, int key){
    int start = 0;
    int end = n;
    // int mid;
    while (start <= end){
        int mid = (start + end)/2;
        if (arr[mid] == key){
            return mid;
        }
        else if (arr[mid] > key){
            end = mid - 1;
        }
        else{
            start = mid+1;
        }
    }
    return -1;
}
int main(){
    int n=6;
    // cin>>n;

    int arr[n] = {5,10,2,6,9,6};
    // for (int i=0; i<n; i++){
    //     cin>>arr[i];
    // }
    cout<<binarySearch(arr, n, 2);
}