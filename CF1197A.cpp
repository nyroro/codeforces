#include <iostream>
#include <cstdio>
using namespace std;
const int N = 100010;
int arr[N];
#define min(a,b) ((a)<(b)?(a):(b))
int main()
{
#ifdef CODEBLOCKS
    freopen("in.txt","r",stdin);
#endif
    int t;
    cin>>t;
    for(int ti=0; ti<t; ti++)
    {
        int n;
        cin>>n;
        int a=-1,b=-1;
        for(int i=0; i<n; i++)
        {
            cin>>arr[i];
            if(arr[i]>a)
            {
                b=a;
                a= arr[i];
            }
            else if(arr[i]>b)
            {
                b=arr[i];
            }
        }
        int ret = min(b-1,n-2);
        if(ret<0)
            ret = 0;
        cout<<ret<<endl;
    }
    return 0;
}