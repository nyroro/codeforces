#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;
int n, I;
const int N = 4*100001;
int arr[N];
int sum[N];
int sn;
int main()
{
    #ifdef CODEBLOCKS
    freopen("in.txt", "r", stdin);
    #endif // CODEBLOCKS
    while(cin>>n>>I)
    {
        for(int i=0;i<n;i++)
        {
            cin>>arr[i];
        }
        sort(arr, arr+n);
        sn = 0;
        for(int i=0;i<n;i++)
        {
            if(i==0||arr[i]!=arr[i-1])
            {
                sum[sn] = 1;
                if(sn>0)
                {
                    sum[sn]+=sum[sn-1];
                }
                sn++;
            }
            else
            {
                sum[sn-1] ++;
            }
        }
        int k = 8*I/n;
        int K = 1;
        for(int i=0;i<k;i++)
        {
            K<<=1;
            if(K >= sn)
            {
                break;
            }
        }
        if(K>=sn)
        {
            cout<<0<<endl;
        }
        else
        {
            int ret = sum[sn-1] - sum[K-1];
            for(int i=K;i<sn;i++)
            {
                ret = min(ret, sum[sn-1]-(sum[i] - sum[i-K]));
            }
            cout<<ret<<endl;
        }
    }
    return 0;
}
