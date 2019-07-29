#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;
const int N = 3*100010;
int arr[N];
long long best[N];
int n,m,k;
#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))
int main()
{
#ifdef CODEBLOCKS
    freopen("in.txt","r",stdin);
#endif
    while(cin>>n>>m>>k)
    {
        long long ret = 0;
        for(int i=0;i<n;i++)
        {
            cin>>arr[i];
            best[i] = max(0, arr[i]-k);
            ret = max(ret,best[i]);
        }

        for(int i=1;i<n;i++)
        {
            long long t = 0;
            for(int j=0;j<m &&i-j>= 0;j++)
            {
                t += arr[i-j];
                best[i] = max(best[i], t-k);
            }
            if(i>=m)
            {
                best[i] = max(best[i], t-k+best[i-m]);
            }
            ret = max(best[i], ret);
        }
        cout<<ret<<endl;
    }
    return 0;
}