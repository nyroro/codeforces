#include <iostream>
#include <cstdio>
#include <queue>
using namespace std;
int n;
const int N = 100010;
int arr[N];
int main()
{
    #ifdef CODEBLOCKS
    freopen("in.txt", "r", stdin);
    #endif // CODEBLOCKS
    while(cin>>n)
    {
        long long sum = 0;
        int m = 0;
        for(int i=0;i<n;i++)
        {
            cin>>arr[i];
            m = max(m, arr[i]);
            sum+=arr[i];
        }
        if(sum%2 == 1 || sum/2<m)cout<<"NO"<<endl;
        else cout<<"YES"<<endl;
    }
    return 0;
}