#include <iostream>

using namespace std;
#define N 1010
int arr[N];
int arr2[N];
int a[N*N];
int b[N*N];
int main()
{
    #ifdef CODEBLOCKS
    freopen("in.txt", "r", stdin);
    #endif // CODEBLOCKS
    int n;
    cin>>n;
    for(int i=0;i<n;i++)
    {
        cin>>arr[i];
        arr[i]--;
    }

    for(int i=0;i<n;i++)
    {
        arr2[i] = i;
    }
    int cnt = 0;
    for (int i=n-1;i>=0;i--)
    {
        int x = arr[i];
        int j = lower_bound(arr2,arr2+i+1,x)-arr2;
//        cout<<x<<' '<<j<<endl;
        for(int k=j-1;k>=0;k--)
        {
            a[cnt]=x;
            b[cnt]=arr2[k];
            cnt++;
        }
        for(int k=0;k<j;k++)
        {
            a[cnt]=arr2[k];
            b[cnt]=x;
            cnt++;
        }
        for(int k=j+1;k<=i;k++)
        {
            a[cnt] = arr2[k];
            b[cnt] = x;
            arr2[k-1]=arr2[k];
            cnt++;
        }
    }
    cout<<cnt<<endl;
    for(int i=0;i<cnt;i++)
    {
        cout<<a[i]+1<<' '<<b[i]+1<<endl;
    }
    return 0;
}
