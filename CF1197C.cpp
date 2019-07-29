#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;
const int N = 3*100010;
int arr[N];
int q[N];
int n,k;
 
#define min(a,b) ((a)<(b)?(a):(b))
int main()
{
#ifdef CODEBLOCKS
    freopen("in.txt","r",stdin);
#endif
    while(cin>>n>>k)
    {
        for(int i=0;i<n;i++)
        {
            cin>>arr[i];
            if(i>0)
            {
                q[i-1]=arr[i]-arr[i-1];
            }
        }
        sort(q,q+n-1);
        long long sum = 0;
        for(int i=0;i<n-k;i++)
        {
            sum+=q[i];
        }
        cout<<sum<<endl;
    }
    return 0;
}