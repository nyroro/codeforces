#include <iostream>
#include <bits/stdc++.h>
using namespace std;
#define N 200010
int n,m;
int a[N],b[N];
long long pa[N],pb[N];

long long cal(int k, int x)
{
//    cout<<"cal"<<k<<' '<<x<<' '<<pa[x]+pb[k-x]<<endl;
    return pa[x]+pb[k-x];
}

long long gao(int k)
{
    long long ans = 0;
    int l = max(0,2*k-m);
    int r = min(k,n-k);
//    cout<<"gaob"<<k<<' '<<l<<' '<<r<<' '<<n<<' '<<k<<endl;
    while(l<=r)
    {
        int l1 = l+(r-l)/3;
        int l2 = l+(r-l)/3*2;
        if (l1 == l2)
        {
            ans = max({cal(k,l),cal(k,r)});
            if (l<r)
            {
                ans = max(ans, cal(k,l+1));
            }
            break;
        }
        long long a1 = cal(k,l1);
        long long a2 = cal(k,l2);
        ans = max(a1,a2);

        if (a1<a2)
        {
            l = l1;
        }
        else
        {
            r = l2;
        }
    }

//    cout<<"gao"<<k<<' '<<ans<<endl;
    return ans;
}

void solve()
{
    int kmax=min({n,m,(n+m)/3});
    cout<<kmax<<endl;
    sort(a,a+n);
    sort(b,b+m);
    pa[0]=0;
//    cout<<"pa";
    for(int i=0;i<n/2;i++)
    {
        if (n-i-1 == i)
        {
            break;
        }
        pa[i+1] = a[n-i-1]-a[i];
        pa[i+1]+=pa[i];
//        cout<<pa[i+1]<<' ';
    }
//    cout<<endl;
//    cout<<"pb";
    pb[0]=0;
    for(int i=0;i<m/2;i++)
    {
        if (m-i-1 == i)
        {
            break;
        }
        pb[i+1] = b[m-i-1]-b[i];
        pb[i+1]+=pb[i];
//        cout<<pb[i+1]<<' ';
    }
//    cout<<endl;
    for(int i=1;i<=kmax;i++)
    {
        if (i>1)
        {
            cout<<' ';
        }
        cout<<gao(i);
    }
    cout<<endl;
}
int main()
{
    #ifdef CODEBLOCKS
    freopen("in.txt", "r", stdin);
    #endif // CODEBLOCKS
    int t;
    cin>>t;
    for(int ti=0;ti<t;ti++)
    {
        cin>>n>>m;
        for(int i=0;i<n;i++)
        {
            cin>>a[i];
        }
        for(int i=0;i<m;i++)
        {
            cin>>b[i];
        }
        solve();
    }
    return 0;
}
