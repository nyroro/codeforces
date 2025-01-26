#include <iostream>
#include <map>
#include <algorithm>
using namespace std;
#define max(a,b) ((a)>(b)?(a):(b))
int main()
{
    #ifdef CODEBLOCKS
    freopen("in.txt", "r", stdin);
    #endif // CODEBLOCKS
    int t;
    #define N 100002
    int arr[N];
    cin>>t;
    map<int, int> mp;
    for (int ti=0;ti<t;ti++)
    {
        int n,k,a;
        cin>>n>>k;
        mp.clear();
        for(int i=0;i<n;i++)
        {
            cin>>a;
            mp[a]++;
        }
        int an = 0;
        for(map<int,int>::iterator it = mp.begin();it!=mp.end();it++)
        {
            arr[an++] = it->second;
        }
        sort(arr, arr+an);
        int ret = an;
        for(int i=0;i<an-1;i++)
        {
            if (k >= arr[i])
            {
                k-=arr[i];
                ret -= 1;
            }
            else
            {
                break;
            }
        }
        cout<<ret<<endl;
    }
}
