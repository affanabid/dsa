#include<iostream>
using namespace std;

int main(){
  // int n;
  // cin>>n;

  int a[7] = {2,5,3,8,8,7,6};
  int b[7+1] = {-1,-1,-1,-1,-1,-1,-1,-1};
  int min = 100;
  for (int i=0; i<7; i++){
    int digit = a[i];
    if (b[digit] == -1){
      b[digit] = i;
    }
    else{
      if (b[digit] < min){
        min = b[digit];
      }
    }
  }
  cout<<a[min]<<endl;
}