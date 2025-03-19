#include <iostream>
#include <bits/stdc++.h>
using namespace std;
#define N 500010
int p[N];
int arr[N];
int suf[N];
struct edg
{
    int v;
    int x;
    int y;
    edg(int x, int y, int v)
    {
        this->x = x;
        this->y = y;
        this->v = v;
    }
    edg()
    {

    }
};
edg e[N*20];
bool cmp(edg a, edg b)
{
    return a.v < b.v;
}
int root(int x)
{
    if(p[p[x]]!=p[x])
    {
        p[x] = root(p[x]);
    }
    return p[x];
}
void solve()
{
    int n;
    cin>>n;
    for(int i=0;i<n;i++)
    {
        cin>>p[i];
    }
    sort(p,p+n);
    arr[0] = p[0];
    int nn = 1;
    for(int i=1;i<n;i++)
    {
        if(p[i]!=arr[nn-1])
        {
            arr[nn++] = p[i];
        }
    }
    n = nn;
    int m = arr[n-1];
    int en = 0;
    for(int i=0;i<n;i++)
    {
        int x=arr[i];
        p[i] = i;
        for(int k=1;k*x<=m;k++)
        {
            int j;
            if (k==1)
            {
                j = lower_bound(arr, arr+n, x+1) - arr;
            }
            else
            {
                j = lower_bound(arr,arr+n,k*x)-arr;
            }
            if(j<n && arr[j]/arr[i] == k)
            {
                e[en++] = edg(i,j,arr[j]%arr[i]);
            }
        }
    }
    sort(e,e+en,cmp);

    long long ret = 0;
    int cnt = 0;
    int i = 0;
    while (cnt<nn-1)
    {
        edg ce = e[i++];
        int x = ce.x;
        int y = ce.y;
        int rx = root(x);
        int ry = root(y);
        if (rx != ry)
        {
            p[rx] = ry;
            ret += ce.v;
            cnt+=1;
        }
//        cout<<"root"<<x<<' '<<y<<' '<<rx<<' '<<ry<<endl;
//        cout<<"cal"<<ret<<endl;
//        cin>>m;
    }
    cout<<ret<<endl;
}
int main()
{
    #ifdef CODEBLOCKS
    freopen("in.txt", "r", stdin);
    #endif // CODEBLOCKS
    cin.tie(0);
    cout.tie(0);
    ios_base::sync_with_stdio(0);
    int t;
    cin>>t;
    for(int i=0;i<t;i++)
    {
        solve();
    }
    return 0;
}
