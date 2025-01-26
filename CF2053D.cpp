#include <iostream>
#include <bits/stdc++.h>

using namespace std;
const int mod=998244353;
#define N 200010
int a[N],b[N],c[N],d[N];
int qmod(int x, int q)
{
    int ret = 1;
    while(q>0)
    {
        if (q&1)
        {
            ret = 1ll*ret*x % mod;
        }
        x = 1ll*x*x %mod;
        q/=2;
    }
    return ret;
}
int main()
{
    #ifdef CODEBLOCKS
    freopen("in.txt", "r", stdin);
    #endif // CODEBLOCKS

    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr); std::cout.tie(nullptr);
    int t;
    cin>>t;
    for(int ti=0;ti<t;ti++)
    {
        int n,q;
        int o,x;
        cin>>n>>q;
        for(int i=0;i<n;i++)
        {
            cin>>a[i];
            c[i] = a[i];
        }
        for(int i=0;i<n;i++)
        {
            cin>>b[i];
            d[i] = b[i];
        }
        sort(c,c+n);
        sort(d,d+n);
        int ret = 1;
        for(int i=0;i<n;i++)
        {
            ret = 1ll*ret*min(c[i],d[i])%mod;
        }
        cout<<ret;
        for(int i=0;i<q;i++)
        {
            cin>>o>>x;
            x--;
            if(o==1)
            {
                int p=upper_bound(c,c+n,a[x])-c-1;
                if(c[p]<d[p])
                {
//                    cout<<p<<' '<<c[p]<<' '<<qmod(c[p],mod-1)<<endl;
//                cout<<ret<<' '<<1ll*ret*qmod(c[p],mod-2)%mod<<' '<<1ll*ret*qmod(c[p],mod-2)%mod*(c[p]+1)%mod<<' '<<qmod(c[p],mod-2)%mod*c[p]<<endl;
                    ret = 1ll*ret*qmod(c[p],mod-2)%mod*(c[p]+1)%mod;
                }
                a[x]++;
                c[p]++;
            }
            else
            {
                int p=upper_bound(d,d+n,b[x])-d-1;
                if(d[p]<c[p])ret = 1ll*ret*qmod(d[p],mod-2)%mod*(d[p]+1)%mod;
                b[x]++;
                d[p]++;
            }
//            cout<<"="<<endl;
//            for(int i=0;i<n;i++)
//            {
//                cout<<c[i]<<' '<<d[i]<<endl;
//            }
            cout<<" "<<ret;

//            cout<<"="<<endl;
        }

        cout<<endl;

//        cout<<"==========="<<endl;
    }
    return 0;
}
