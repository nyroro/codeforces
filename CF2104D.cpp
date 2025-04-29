#include <iostream>
#include <algorithm>
using namespace std;
#define N 6000000

bool prime[N];
int plist[N];
long long ps[N];
int pn;
int a[N];
long long s[N];
void init()
{
    pn = 0;
    for(int i=2;i<N;i++)
    {
        if (!prime[i])
        {
            plist[pn++] = i;
            for(long long j=1ll*i*i;j<N;j+=i)
            {
                prime[j] = true;
            }
        }
    }
    ps[0] = plist[0];
    for (int i=1;i<pn;i++)
    {
        ps[i]=ps[i-1]+plist[i];
    }
}
void solve()
{
    int n;
    cin>>n;
    for(int i=0;i<n;i++)
    {
        cin>>a[i];
    }
    sort(a,a+n);
    s[0]=a[0];
    for (int i=1;i<n;i++)
    {
        s[i] = s[i-1]+a[i];
    }
    if (s[n-1]>=ps[n-1])
    {
        cout<<0<<endl;
        return;
    }

    int l=0;
    int r=n-1;
    int ret = n-1;
    while(l<r)
    {
//        cout<<l<<' '<<r<<endl;
        int mid = (l+r)/2;
        long long ss = s[n-1];
        if (mid > 0)
        {
            ss -= s[mid-1];
        }
        long long pp = ps[n-1-mid];
//        cout<<mid<<' '<<ss<<' '<<pp<<endl;
        if (ss>=pp)
        {
            ret = mid;
            r=mid;
        }
        else
        {
            l=mid+1;
        }
    }
    cout<<ret<<endl;
}

int main()
{
    #ifdef CODEBLOCKS
    freopen("in.txt", "r", stdin);
    #endif // CODEBLOCKS
    init();
    int t;
    cin>>t;
    for(int ti=0;ti<t;ti++)
    {
        solve();
    }
}
