#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;
int n,k;
const int N = 2*100010;
int arr[N];
int main()
{
    #ifdef CODEBLOCKS
    freopen("in.txt", "r", stdin);
    #endif // CODEBLOCKS
    while(cin>>n>>k)
    {
        for(int i=0;i<n;i++)
        {
            cin>>arr[i];
        }
        if(n==1)
        {
            cout<<arr[0]+k<<endl;
            continue;
        }
        sort(arr,arr+n);
        int mid;
        mid=n/2;
        int i;
        for(i=mid;i<n-1&&k>0;i++)
        {
            long long t = 1ll*(arr[i+1]-arr[i])*(i-mid+1);
            if(k>=t)
            {
                k-=t;
                arr[mid] = arr[i+1];
            }
            else
            {
                break;
            }
        }
        arr[mid] = arr[mid]+(k/(i-mid+1));
        cout<<arr[mid]<<endl;
 
    }
    return 0;
}