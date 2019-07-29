#include <iostream>
#include <cstdio>
using namespace std;
const int N = 2*100010;
int n;
int arr[N];
#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))
bool solve()
{
    int ti = -1;
    int t = -1;
    for(int i=0;i<n;i++)
    {
        if(arr[i] > t)
        {
            t = arr[i];
            ti = i;
        }
    }
    int a = t;
    for(int i=ti-1;i>=0;i--)
    {
        int x = arr[i];
        if(x>=a)
        {
            return false;
        }
        a = min(x, a);
    }
    a = t;
    for(int i=ti+1;i<n;i++)
    {
        int x = arr[i];
        if(x>=a)
        {
            return false;
        }
        a=min(x,a);
    }
    return true;
 
}
int main()
{
    #ifdef CODEBLOCKS
    freopen("in.txt","r",stdin);
    #endif
    while(cin>>n)
    {
 
        for(int i=0;i<n;i++)
        {
            cin>>arr[i];
        }
 
        if(solve())
        {
            cout<<"YES"<<endl;
        }
        else
        {
            cout<<"NO"<<endl;
        }
    }
 
    return 0;
}