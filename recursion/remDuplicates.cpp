#include<iostream>
#include<string>
using namespace std;

string removeDuplicates(string s, int i){
    if (s.length() == 0){
        return 0;
    }
    if (s[i] == s[i+1]){
        s = s.erase(0, 1); 
    }
    removeDuplicates(s, i+1);
    return s;
}
int main(){

    cout<<removeDuplicates("aaaabbcccccccddd", 0)<<endl;
}